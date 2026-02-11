"""
case_runner.py — Orquestador universal para casos de simulación.

Centraliza TODA la lógica que antes estaba duplicada en 29 validate.py:
  - Carga de datos (CSV genérico)
  - Generación de sintético estándar (forcing + ODE)
  - Construcción de CaseConfig
  - Ejecución de validación
  - Escritura de outputs

Cada caso ahora necesita:
  1. case_config.json   — TODO declarativo (datos, modelo, parámetros, fechas)
  2. ode.py             — Slim: selecciona arquetipo del catálogo
  3. validate.py         — 4 líneas: import case_runner, run_case

Opcionalmente, un caso puede tener data.py con funciones
load_real_data() o make_synthetic() que sobreescriben las genéricas.

Uso:
    # Desde NN_caso_X/src/validate.py:
    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
    from case_runner import run_case
    if __name__ == "__main__":
        run_case(os.path.dirname(__file__))
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd


# ─── Carga de datos ──────────────────────────────────────────────────────────

def _load_csv_data(csv_path: str, cfg_data: dict, start_date: str, end_date: str) -> pd.DataFrame:
    """Carga datos reales desde CSV con detección automática de columnas."""
    df = pd.read_csv(csv_path)

    # Detectar/crear columna date
    date_col = cfg_data.get("date_col", "date")
    year_col = cfg_data.get("year_col")

    if date_col in df.columns:
        df["date"] = pd.to_datetime(df[date_col])
    elif year_col and year_col in df.columns:
        df["date"] = pd.to_datetime(df[year_col].astype(int).astype(str) + "-01-01")
    elif "year" in df.columns and "date" not in df.columns:
        df["date"] = pd.to_datetime(df["year"].astype(int).astype(str) + "-01-01")
    else:
        raise ValueError(f"No se encontró columna de fecha en {csv_path}. "
                         f"Columnas: {list(df.columns)}")

    value_col = cfg_data.get("value_col", "value")
    if value_col not in df.columns:
        raise ValueError(f"Columna '{value_col}' no encontrada en {csv_path}. "
                         f"Columnas: {list(df.columns)}")

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)].copy()
    # Renombrar value_col a "value" si es diferente
    if value_col != "value":
        df = df.rename(columns={value_col: "value"})

    keep_cols = ["date", "value"]
    driver_cols = cfg_data.get("driver_cols", [])
    for dc in driver_cols:
        if dc in df.columns:
            keep_cols.append(dc)

    return df[keep_cols].dropna(subset=["date", "value"]).reset_index(drop=True)


# ─── Generación de sintético ─────────────────────────────────────────────────

def _make_standard_synthetic(cfg: dict, simulate_ode_fn, start_date: str,
                             end_date: str, seed: int = 101) -> tuple:
    """Genera datos sintéticos estándar a partir de la config."""
    rng = np.random.default_rng(seed)
    syn_cfg = cfg.get("synthetic", {})

    freq = syn_cfg.get("freq", "MS")
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    n = len(dates)
    t = np.arange(n, dtype=float)

    # Generar forcing según tipo
    forcing_cfg = syn_cfg.get("forcing", {})
    forcing = _generate_forcing(t, n, forcing_cfg, rng)

    # Simular ODE con true_params
    true_params = dict(syn_cfg.get("true_params", {}))
    true_params["forcing_series"] = forcing.tolist()
    if "p0" not in true_params:
        true_params["p0"] = forcing[0] if len(forcing) > 0 else 0.0

    sim = simulate_ode_fn(true_params, n, seed=seed + 1)
    ode_key = [k for k in sim if k != "forcing"][0]
    obs = np.array(sim[ode_key])

    # Ruido de medición
    meas_noise = float(syn_cfg.get("measurement_noise", 0.08))
    obs = obs + rng.normal(0.0, meas_noise, size=n)

    df = pd.DataFrame({"date": dates, "value": obs})

    # Meta para validación del sintético
    meta = {
        "model": cfg.get("ode_model", "mean_reversion"),
        "true_params": true_params,
        "forcing_series": forcing.tolist(),
    }

    return df, meta


def _generate_forcing(t: np.ndarray, n: int, fcfg: dict, rng) -> np.ndarray:
    """Genera serie de forzamiento según configuración."""
    ftype = fcfg.get("type", "linear_cycle")
    base = float(fcfg.get("base", 0.5))
    noise_std = float(fcfg.get("noise_std", 0.05))

    if ftype == "linear_cycle":
        slope = float(fcfg.get("slope", 0.01))
        cycle_amp = float(fcfg.get("cycle_amp", 0.3))
        cycle_period = float(fcfg.get("cycle_period", 48))
        forcing = base + slope * t + cycle_amp * np.sin(2 * np.pi * t / cycle_period)

    elif ftype == "logistic":
        amplitude = float(fcfg.get("amplitude", 1.0))
        rate = float(fcfg.get("rate", 0.01))
        cycle_amp = float(fcfg.get("cycle_amp", 0.0))
        cycle_period = float(fcfg.get("cycle_period", 48))
        forcing = base + amplitude * (1.0 - np.exp(-rate * t))
        if cycle_amp > 0:
            forcing += cycle_amp * np.sin(2 * np.pi * t / cycle_period)

    elif ftype == "constant":
        forcing = np.full(n, base)

    elif ftype == "step":
        step_time = int(fcfg.get("step_time", n // 2))
        step_value = float(fcfg.get("step_value", 1.0))
        forcing = np.full(n, base)
        forcing[step_time:] += step_value

    elif ftype == "exponential":
        rate = float(fcfg.get("rate", 0.01))
        forcing = base * np.exp(rate * t)

    else:
        # Fallback: linear
        forcing = base + 0.01 * t

    forcing += rng.normal(0.0, noise_std, n)
    return forcing


# ─── Construcción de CaseConfig ──────────────────────────────────────────────

def _build_case_config(cfg: dict):
    """Construye CaseConfig desde el JSON ampliado."""
    from hybrid_validator import CaseConfig

    dates = cfg.get("dates", {})
    thresholds = cfg.get("thresholds", {})
    extra = dict(cfg.get("extra_ode_params", {}))

    execution = cfg.get("execution", {})

    return CaseConfig(
        case_name=cfg.get("case_name", "Unknown"),
        value_col="value",  # Siempre normalizado a "value"
        series_key=cfg.get("series_key", cfg.get("ode_key", "x")),
        grid_size=execution.get("grid_size", 25),
        persistence_window=thresholds.get("persistence_window", 5),
        synthetic_start=dates.get("synthetic_start", "2000-01-01"),
        synthetic_end=dates.get("synthetic_end", "2019-12-01"),
        synthetic_split=dates.get("synthetic_split", "2012-01-01"),
        real_start=dates.get("real_start", "1990-01-01"),
        real_end=dates.get("real_end", "2022-01-01"),
        real_split=dates.get("real_split", "2006-01-01"),
        corr_threshold=thresholds.get("corr_threshold", 0.5),
        extra_base_params=extra,
        n_runs=execution.get("n_runs", 5),
        driver_cols=cfg.get("data", {}).get("driver_cols", []),
        use_topology=cfg.get("topology", {}).get("enabled", False),
        topology_type=cfg.get("topology", {}).get("type", "small_world"),
        topology_params=cfg.get("topology", {}).get("params", {}),
        feedback_strength=cfg.get("topology", {}).get("feedback_strength", 0.0),
        log_transform=cfg.get("log_transform", False),
        loe=cfg.get("loe", 3),
        ode_calibration=cfg.get("ode_calibration", True),
        abm_calibration=cfg.get("abm_calibration", True),
    )


# ─── Importación dinámica de módulos del caso ────────────────────────────────

def _import_module_from_dir(module_name: str, case_src_dir: str):
    """Importa un módulo desde el directorio src/ del caso."""
    module_path = os.path.join(case_src_dir, f"{module_name}.py")
    if not os.path.exists(module_path):
        return None
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ─── Runner principal ────────────────────────────────────────────────────────

def run_case(case_src_dir: str):
    """
    Ejecuta validación completa de un caso.

    Args:
        case_src_dir: ruta absoluta al directorio src/ del caso
    """
    from hybrid_validator import run_full_validation, write_outputs

    case_src_dir = os.path.abspath(case_src_dir)
    case_dir = os.path.dirname(case_src_dir)  # NN_caso_X/

    # 1. Leer case_config.json
    config_path = os.path.join(case_dir, "case_config.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"No se encontró {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    print(f"[case_runner] Caso: {cfg.get('case_name', 'Unknown')}", file=sys.stderr)

    # 2. Importar ABM y ODE del caso
    # Asegurar que src/ esté en el path para imports internos
    if case_src_dir not in sys.path:
        sys.path.insert(0, case_src_dir)

    abm_mod = _import_module_from_dir("abm", case_src_dir)
    ode_mod = _import_module_from_dir("ode", case_src_dir)

    if abm_mod is None:
        raise ImportError(f"No se encontró abm.py en {case_src_dir}")
    if ode_mod is None:
        raise ImportError(f"No se encontró ode.py en {case_src_dir}")

    simulate_abm_fn = abm_mod.simulate_abm
    simulate_ode_fn = ode_mod.simulate_ode

    # 3. Construir CaseConfig
    config = _build_case_config(cfg)

    # 4. Definir funciones de datos
    # Buscar overrides en data.py del caso
    data_mod = _import_module_from_dir("data", case_src_dir)

    # load_real_data
    if data_mod and hasattr(data_mod, "load_real_data"):
        load_real_fn = data_mod.load_real_data
    else:
        # Versión genérica: lee CSV
        data_cfg = cfg.get("data", {})
        csv_rel = data_cfg.get("csv", "data/dataset.csv")
        csv_path = os.path.join(case_dir, csv_rel)

        def load_real_fn(start_date, end_date, _csv=csv_path, _dcfg=data_cfg):
            return _load_csv_data(_csv, _dcfg, start_date, end_date)

    # make_synthetic
    if data_mod and hasattr(data_mod, "make_synthetic"):
        make_synthetic_fn = data_mod.make_synthetic
    else:
        def make_synthetic_fn(start_date, end_date, seed=101,
                              _cfg=cfg, _ode=simulate_ode_fn):
            return _make_standard_synthetic(_cfg, _ode, start_date, end_date, seed)

    # 5. Ejecutar validación
    is_falsification = cfg.get("is_falsification", False)

    if is_falsification:
        # Modo falsificación: solo fase real, sin sintético, sin gating
        from hybrid_validator import evaluate_phase, write_outputs
        from datetime import datetime

        print(f"[case_runner] Modo FALSIFICACIÓN", file=sys.stderr)
        real_df = load_real_fn(config.real_start, config.real_end)

        real_phase = evaluate_phase(
            config, real_df, config.real_start, config.real_end,
            config.real_split, simulate_abm_fn, simulate_ode_fn,
            param_grid=None
        )

        edi = real_phase.get("edi", {})
        val = edi.get("value", -999) if isinstance(edi, dict) else edi
        falsification_success = (val < 0.10)

        results = {
            "case": config.case_name,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "git": {"commit": "case_runner_falsification", "dirty": False},
            "phases": {"real": real_phase},
            "falsification_success": falsification_success,
        }

        # Escribir outputs
        out_dir = os.path.join(case_dir, "outputs")
        write_outputs(results, os.path.abspath(out_dir))

        print(f"\n--- {config.case_name} ---")
        print(f"  EDI: {val:.4f}" if isinstance(val, (int, float)) else f"  EDI: {val}")
        print(f"  Falsificación: {'ÉXITO' if falsification_success else 'FALLO'}")

        return results

    results = run_full_validation(
        config, load_real_fn, make_synthetic_fn,
        simulate_abm_fn, simulate_ode_fn,
    )

    # 6. Escribir outputs
    out_dir = os.path.join(case_dir, "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    # 7. Imprimir resumen
    print(f"\n--- {cfg.get('case_name', 'Unknown')} ---")
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        val = edi.get("value", "N/A") if isinstance(edi, dict) else edi
        op = phase.get("overall_pass", False)
        ei = phase.get("effective_information", "?")
        print(f"  {phase_name}: EDI={val:.4f} EI={ei:.4f} Pass={op}"
              if isinstance(val, (int, float)) and isinstance(ei, (int, float))
              else f"  {phase_name}: EDI={val} EI={ei} Pass={op}")

    return results

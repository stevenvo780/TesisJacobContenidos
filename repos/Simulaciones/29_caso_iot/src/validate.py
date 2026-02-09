"""
validate.py — 29_caso_iot (Top-Tier)

Hiperobjeto: Ecosistema IoT Global
Modelo: Bass Diffusion + Metcalfe Network Effects
Datos: World Bank (suscripciones móviles + internet + broadband + PIB)

Propiedades de hiperobjeto validadas:
- No-localidad: Adopción tecnológica es fenómeno global coordinado
- Viscosidad: Path dependency tecnológica (lock-in, switching costs)
- Phasing temporal: Diferentes regiones en diferentes fases de la S-curve
- Interobjetualidad: Cruza fronteras entre telecomunicaciones, economía, sociedad
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_data
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    cache_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    )
    df, meta = fetch_data(cache_path, start_date=start_date, end_date=end_date)
    df["date"] = pd.to_datetime(df["date"])
    print(f"[IoT] Datos cargados: {len(df)} obs, fuente={meta.get('source')}")
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=129):
    """
    Sintético calibrado a curva de adopción IoT.
    Usa ODE con patrón alpha*(f-beta*X) en espacio Z.
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Forcing sintético: crecimiento monotónico (patrón estándar)
    forcing = [0.010 * t + 0.0003 * t**1.2 for t in range(steps)]

    # ODE con parámetros en espacio Z
    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.12,
        "ode_beta": 0.02,
        "ode_metcalfe": 0.003,
        "ode_noise": 0.08,
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    obs = np.array(sim["io"]) + rng.normal(0.0, 0.15, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {
        "ode_true": {"alpha": 0.12, "beta": 0.02, "metcalfe": 0.003},
        "measurement_noise": 0.15,
    }
    return df, meta


def main():
    config = CaseConfig(
        case_name="Ecosistema IoT Global (Bass-Metcalfe)",
        value_col="value",
        series_key="io",
        grid_size=25,               # 625 agentes (regiones)
        persistence_window=8,
        synthetic_start="1980-01-01",
        synthetic_end="2022-01-01",
        synthetic_split="2005-01-01",
        real_start="1980-01-01",
        real_end="2022-01-01",
        real_split="2005-01-01",
        corr_threshold=0.65,
        ode_noise=0.03,
        base_noise=0.005,
        loe=4,                       # Level of Evidence: alto (datos sólidos, modelo validado)
        n_runs=7,
        ode_calibration=True,
        extra_base_params={
            "ode_delta": 0.005,     # Damping cuadrático: saturación
            "forcing_scale": 0.15,
            "macro_coupling": 0.40,
        },
        driver_cols=["internet_users", "broadband", "gdp_pc", "gdp_growth"],
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        sym = phase.get("symploke", {})
        visc = phase.get("viscosity", {})
        print(f"  {phase_name}: overall={phase.get('overall_pass')}"
              f" EDI={edi.get('value', 0):.4f}"
              f" CR={sym.get('cr', 0):.3f}"
              f" Viscosity={visc.get('detail', {}).get('relaxation_time', 0)}")
    print("Caso 29 IoT (Bass-Metcalfe) completo.")


if __name__ == "__main__":
    main()

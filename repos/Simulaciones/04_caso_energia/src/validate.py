"""
validate.py — Energía (Consumo Per Cápita Global)
Validación híbrida ABM+ODE con protocolo C1-C5.

Variable: EG.USE.PCAP.KG.OE (World Bank) — kg oil eq per cápita.
Drivers: gdp_growth, urban_pct, industry_pct.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_energy_data
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    df = fetch_energy_data(start_date, end_date,
                           cache_path=os.path.abspath(cache_path))
    df = df.rename(columns={"energy_use_pc": "value"})
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Drivers sintéticos INDEPENDIENTES (anti-correlados):
    # - Urban pct: tendencia ascendente (urbanización global)
    # - Industry pct: estacionario con ruido (desacoplado de urban)
    # Se omite GDP porque su peso OLS es ~0 en datos reales.
    urban_synth = [40.0 + 0.5 * t + rng.normal(0, 0.1) for t in range(steps)]
    industry_synth = [30.0 + rng.normal(0, 1.0) for _ in range(steps)]

    # Z-score drivers
    urban_arr = np.array(urban_synth)
    ind_arr = np.array(industry_synth)
    urban_z = (urban_arr - urban_arr.mean()) / (urban_arr.std() + 1e-8)
    ind_z = (ind_arr - ind_arr.mean()) / (ind_arr.std() + 1e-8)

    # Forcing combinado (pesos similares a reales: urban +1.4, ind +0.7)
    forcing = (0.65 * urban_z + 0.35 * ind_z).tolist()

    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.40,
        "ode_beta": 0.80,    # τ ≈ 1.25 años → tracking rápido, evita desfase
        "ode_noise": 0.01,
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    obs = np.array(sim["e"]) + rng.normal(0.0, 0.01, size=steps)

    df = pd.DataFrame({
        "date": dates,
        "value": obs,
        "urban_pct": urban_synth,
        "industry_pct": industry_synth,
    })
    meta = {
        "ode_true": {"alpha": 0.40, "beta": 0.80, "noise": 0.01},
        "measurement_noise": 0.01,
    }
    return df, meta


def main():
    # ── Configuración del caso ──────────────────────────────────────────
    # 32 puntos anuales (1991-2022). Split 2010: 19 training, 13 val.
    # Drivers: gdp_growth (w=+0.10), urban_pct (w=+1.44),
    #          industry_pct (w=+0.75). Todos con peso OLS positivo.
    # Forcing-obs r_val=+0.724.
    config = CaseConfig(
        case_name="Energía (Consumo Per Cápita)",
        value_col="value",
        series_key="e",
        grid_size=25,
        persistence_window=5,
        corr_threshold=0.5,
        synthetic_start="1980-01-01",
        synthetic_end="2019-01-01",
        synthetic_split="2000-01-01",
        real_start="1990-01-01",
        real_end="2023-01-01",
        real_split="2010-01-01",
        extra_base_params={
            "ode_alpha": 0.15,
            "ode_beta": 0.08,
        },
        ode_calibration=True,
        driver_cols=["urban_pct", "industry_pct"],
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        if isinstance(edi, dict):
            print(f"  {phase_name}: EDI={edi.get('value', 'N/A'):.3f}")
        else:
            print(f"  {phase_name}: EDI={edi:.3f}")
        print(f"    overall_pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

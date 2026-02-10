"""
validate.py — Salinización de Suelos
Validación híbrida ABM+ODE con protocolo C1-C5.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_arable_land
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    cache_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "wb_arable_land.csv"))
    df, _ = fetch_arable_land(cache_path, start_year=int(start_date[:4]), end_year=int(end_date[:4]))
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Forcing: irrigación creciente (intensificación agrícola global)
    # 0.008*t: tendencia lineal ~0.8%/año (FAO 2021: expansión irrigación global)
    # 0.0003*t^1.2: aceleración por retroalimentación (más irrigación → más salinización → abandono → más presión)
    forcing = [0.008 * t + 0.0003 * t**1.2 for t in range(steps)]
    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.05,    # Tasa acumulación salina (~5%/año; Qadir et al. 2014)
        "ode_beta": 0.015,    # Tasa lavado natural (~1.5%/año; Hillel 2000)
        "ode_inflow": 0.05,   # Alias para accumulation_decay
        "ode_decay": 0.015,   # Alias para accumulation_decay
        "ode_noise": 0.015,   # Variabilidad interanual
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.04, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"inflow": 0.05, "decay": 0.015}, "measurement_noise": 0.04}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Salinización de Suelos (Richards-Solute)",
        value_col="value",
        series_key="sl",
        grid_size=50,             # 50×50 = 2500 agentes (antes 25×25=625)
        persistence_window=5,
        synthetic_start="1961-01-01",
        synthetic_end="2022-01-01",
        synthetic_split="2005-01-01",
        real_start="1961-01-01",
        real_end="2022-01-01",
        real_split="2005-01-01",
        base_noise=0.002,
        corr_threshold=0.65,
        ode_noise=0.015,
        loe=3,
        n_runs=15,                # 15 réplicas (antes 7) — 32 cores disponibles
        ode_calibration=True,
        extra_base_params={
            # ode_gamma=0.02: feedback bilineal evaporación × salinidad
            #   (Rhoades et al. 1992: relación no-lineal observada)
            "ode_gamma": 0.02,
            "forcing_scale": 0.10,   # Sensibilidad ABM a driver externo
            "macro_coupling": 0.35,  # Acoplamiento macro→micro (moderado-alto)
        },
        # Freshwater withdrawal (WB ER.H2O.FWTL.ZS) como driver multivariado:
        #   Qadir et al. (2014): extracción de agua es correlato directo de
        #   salinización secundaria por riego excesivo.
        driver_cols=["freshwater_withdrawal"],
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
        print(f"  {phase_name}: overall={phase.get('overall_pass')}"
              f" EDI={edi.get('value', 0):.3f} CR={sym.get('cr', 0):.3f}"
              f" C1={phase.get('c1_convergence')}")
    print("Validación completa.")


if __name__ == "__main__":
    main()

"""
validate.py — Ciclo del Fósforo
Validación híbrida ABM+ODE con protocolo C1-C5.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_fertilizer_consumption
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    cache_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "wb_fertilizer_consumption.csv"))
    df, _ = fetch_fertilizer_consumption(cache_path, start_year=int(start_date[:4]), end_year=int(end_date[:4]))
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Forcing: uso creciente de fertilizantes fosfatados
    # 0.012*t: tendencia secular ~1.2%/año (Cordell et al. 2009: crecimiento demanda P)
    # 0.0004*t^1.3: aceleración por intensificación agrícola (FAO 2020)
    forcing = [0.012 * t + 0.0004 * t**1.3 for t in range(steps)]
    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.07,   # Input fertilizantes (~7%/año; Cordell 2009)
        "ode_beta": 0.02,    # Sedimentación irreversible (~2%/año; Carpenter 2005)
        "ode_inflow": 0.07,  # Alias para accumulation_decay
        "ode_decay": 0.02,   # Alias para accumulation_decay
        "ode_noise": 0.018,  # Variabilidad interanual
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.04, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"inflow": 0.07, "decay": 0.02}, "measurement_noise": 0.04}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Ciclo del Fósforo (Carpenter Biogeoquímico)",
        value_col="value",
        driver_cols=[],  # Dataset univariado (WorldBank AG.CON.FERT.ZS)
        series_key="ph",
        grid_size=25,
        persistence_window=5,
        synthetic_start="1960-01-01",
        synthetic_end="2022-01-01",
        synthetic_split="2005-01-01",
        real_start="1960-01-01",
        real_end="2022-01-01",
        real_split="2005-01-01",
        corr_threshold=0.65,
        ode_noise=0.018,
        base_noise=0.003,
        loe=3,
        n_runs=7,
        ode_calibration=True,
        extra_base_params={
            # ode_gamma=0.02: feedback bilineal runoff×concentración
            #   (Carpenter & Bennett 2011: eutrofización no-lineal)
            "ode_gamma": 0.02,
            "forcing_scale": 0.10,   # Sensibilidad ABM a driver externo
            "macro_coupling": 0.40,  # Acoplamiento macro→micro alto
        },
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

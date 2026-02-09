"""validate.py — Caso 10: Justicia Algorítmica.

Modelo híbrido: ODE logística forzada + ABM Deffuant de opinión.
Datos: Índice de Estado de Derecho (World Justice Project / World Bank).
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
    df, _ = fetch_data(cache_path, start_date=start_date, end_date=end_date)
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    # Forcing: presión institucional con inercia (Acemoglu & Robinson 2012)
    # Crecimiento lento que refleja reformas legales graduales
    forcing = [0.005 * t + 0.001 * t**1.1 for t in range(steps)]
    true_params = {
        "p0": 0.0, "t0": 0.0,
        "ode_alpha": 0.02,   # Cambio institucional lento (τ ≈ 50 meses)
        "ode_beta": 0.01,    # Resistencia al cambio (path dependence)
        "ode_noise": 0.03,   # Variabilidad política
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.04, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.02, "beta": 0.01}, "measurement_noise": 0.04}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Justicia Algorítmica",
        value_col="value",
        series_key="j",
        grid_size=20, # Spatial consensus matters here
        persistence_window=12,
        synthetic_start="2005-01-01",
        synthetic_end="2023-12-01",
        synthetic_split="2016-01-01",
        real_start="1963-01-01",
        real_end="2023-01-01",
        real_split="2005-01-01",
        corr_threshold=0.6,
        extra_base_params={"abm_epsilon": 0.2, "abm_mu": 0.3},
        driver_cols=[],  # CSV solo tiene date, value
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

"""
validate.py — Riesgo Biológico Global
Validación híbrida ABM+ODE con protocolo C1-C5.
Dominio: Bioseguridad
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

    # Forcing: presión zoonótica creciente (Woolhouse 2005, urbanización/deforestación)
    forcing = [0.006 * t + 0.3 * (1.0 if t % 48 < 6 else 0.0) for t in range(steps)]  # Brotes periódicos
    true_params = {
        "p0": 0.1, "ode_r": 0.06, "ode_k": 2.0,  # Riesgo biológico: logístico con techo
        "ode_delta": 0.025, "ode_gamma": 0.10,
        "ode_noise": 0.03, "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.06, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"r": 0.06, "K": 2.0, "delta": 0.025, "gamma": 0.10}, "measurement_noise": 0.06}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Riesgo Biológico Global (Woolhouse Zoonotic)",
        value_col="value",
        series_key="b",
        grid_size=25,
        persistence_window=12,
        synthetic_start="2000-01-01",
        synthetic_end="2023-12-01",
        synthetic_split="2014-01-01",
        real_start="2000-01-01",
        real_end="2023-12-01",
        real_split="2014-01-01",
        corr_threshold=0.60,
        ode_noise=0.03,
        base_noise=0.004,
        loe=4,
        n_runs=7,
        ode_calibration=False,
        extra_base_params={
            "ode_r": 0.06,       # Tasa de emergencia zoonótica
            "ode_k": 2.0,       # Techo de riesgo biológico global
            "ode_delta": 0.025,  # Contención/respuesta sanitaria
            "ode_gamma": 0.10,   # Sensibilidad a forcing zoonótico
            "forcing_scale": 0.10,
            "macro_coupling": 0.25,
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
        if isinstance(edi, dict):
            print(f"  {phase_name}: EDI={edi.get('value', 'N/A'):.3f}")
        else:
            print(f"  {phase_name}: EDI={edi:.3f}")
        print(f"    overall_pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

"""
validate.py — 18_caso_urbanizacion

Hyperobject: Urbanización global.
Observable: % población urbana mundial (World Bank).
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


# ── Carga de datos reales ────────────────────────────────────────
def load_real_data(start_date, end_date):
    csv = os.path.join(os.path.dirname(__file__), "..", "data", "wb_urbanization.csv")
    df = pd.read_csv(csv, parse_dates=["date"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)].copy()
    df = df[["date", "value"]].dropna(subset=["date", "value"]).reset_index(drop=True)
    return df


# ── Generador sintético ─────────────────────────────────────────
def make_synthetic(start_date, end_date, seed=101):
    """Señal mensual: urbanización % (34-57) con tendencia logística + ruido."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    n = len(dates)
    t = np.arange(n, dtype=float)

    # Forcing: tendencia logística suavizada centrada en ~44%
    mid = n / 2
    forcing = 34.0 + 23.0 / (1.0 + np.exp(-0.02 * (t - mid)))
    forcing += rng.normal(0, 0.2, n)

    # Observable: mean_reversion dX = α*(F - β*X)
    obs = np.zeros(n)
    obs[0] = forcing[0]
    alpha_s, beta_s = 0.06, 1.0
    for i in range(1, n):
        obs[i] = obs[i - 1] + alpha_s * (forcing[i] - beta_s * obs[i - 1]) + rng.normal(0, 0.15)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {
        "model": "mean_reversion_synthetic",
        "true_params": {
            "forcing_scale": 1.0,
            "macro_coupling": 0.30,
            "damping": 0.05,
            "ode_alpha": 0.05,
            "ode_beta": 0.50,
        },
        "forcing_series": forcing.tolist(),
    }
    return df, meta


def main():
    config = CaseConfig(
        case_name="Urbanización Global",
        value_col="value",
        series_key="u",
        grid_size=25,
        persistence_window=5,
        synthetic_start="2000-01-01",
        synthetic_end="2019-12-01",
        synthetic_split="2012-01-01",
        real_start="1960-01-01",
        real_end="2022-01-01",
        real_split="2000-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "ode_alpha": 0.05,
            "ode_beta": 0.50,
        },
        driver_cols=[],
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    print("\n--- Validation Results ---")
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        val = edi.get("value", "N/A") if isinstance(edi, dict) else edi
        print(f"  {phase_name}: EDI={val:.4f} Pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

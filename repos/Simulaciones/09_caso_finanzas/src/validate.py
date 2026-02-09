"""validate.py — Caso 09: Finanzas (SPY).

Validación del mercado financiero (S&P 500) como hiperobjeto.
Modelo: ODE Heston simplificado + ABM Brock-Hommes espacial.

Resultado histórico: EDI ≈ 0.05 → RECHAZADO (reflexividad/aliasing temporal).
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_spy_monthly
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    """Descarga SPY mensual + drivers macro (VIX, FedFunds, CPI, credit spread)."""
    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "spy_monthly.csv")
    df = fetch_spy_monthly(start_date, end_date, cache_path=os.path.abspath(cache_path))
    df = df.rename(columns={"price": "value"})
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    """Genera serie sintética con ODE Heston para fase de control."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)

    forcing = [0.01 * t for t in range(steps)]
    true_params = {
        "p0": 0.0, "ode_alpha": 0.08, "ode_beta": 0.03,
        "ode_noise": 0.02, "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k != "forcing"][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.08, "beta": 0.03}, "measurement_noise": 0.05}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Finanzas (SPY)",
        value_col="value",
        series_key="x",
        grid_size=1,
        persistence_window=12,
        synthetic_start="2000-01-01",
        synthetic_end="2019-12-01",
        synthetic_split="2010-01-01",
        real_start="1990-01-01",
        real_end="2024-12-31",
        real_split="2011-01-01",
        corr_threshold=0.7,
        extra_base_params={},  # sentiment_scale eliminado (ABM no lo lee)
        driver_cols=["vix", "fedfunds", "inflation", "credit_spread", "volume"],
        use_topology=True,
        topology_type="small_world",
        topology_params={"k": 4, "p": 0.1},
        feedback_strength=0.05,
        loe=5,
    )

    print("--- Finanzas (SPY) ---")
    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {}).get("value", 0)
        print(f"  {phase_name}: EDI={edi:.3f}")
    print("Validación completa.")


if __name__ == "__main__":
    main()

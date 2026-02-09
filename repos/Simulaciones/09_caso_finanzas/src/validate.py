"""
validate.py — Finanzas (SPY)
Validación híbrida ABM+ODE con protocolo C1-C5.
Generado automáticamente por el framework de validación de hiperobjetos.
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

    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "spy_monthly.csv")
    df = fetch_spy_monthly(start_date, end_date, cache_path=os.path.abspath(cache_path))
    df = df.rename(columns={"price": "value"})
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    forcing = [0.01 * t for t in range(steps)]
    true_params = {
        "p0": 0.0, "x0": 0.0, "ode_alpha": 0.08, "ode_beta": 0.03,
        "ode_noise": 0.02, "forcing_series": forcing,
        "p0_ode": 0.0,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
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
        extra_base_params={"sentiment_scale": 0.05},
        driver_cols=["vix", "fedfunds", "inflation", "credit_spread", "volume"],
        use_topology=True,
        topology_type="small_world",
        topology_params={"k": 4, "p": 0.1},
        feedback_strength=0.05,
        loe=5,
    )

    # Create adapter or use directly?
    # New ABM returns {"x": grid_series}, compatible with validator.
    # Note: The validator expects simulate_abm to return a dict.
    
    print("--- Running Finance Validation (High Rigor) ---")
    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )
    
    # Calculate Stylized Facts on Real Data
    from metrics import kurtosis, volatility_clustering
    real_df = load_real_data(config.real_start, config.real_end)
    # Check "price" column or "value"? Config says "value".
    prices = real_df["value"].values
    
    # Compute Log Returns: r_t = p_t - p_{t-1}
    # Note: prices are already log-prices in data.py ("log_views" / "log_price")? 
    # Let's check data.py. fetch_spy_monthly returns "log_price" renamed to "price".
    # So valid returns are diff(data).
    returns = np.diff(prices)
    
    kurt = kurtosis(returns)
    vol_clus = volatility_clustering(prices, lag=1) # Vol Clustering uses returns internally if implemented right?
    # metrics.volatility_clustering calculates returns internally: "returns = [xs[i] - xs[i-1]...]"
    # So we pass PRICES to vol_clustering, but RETURNS to kurtosis.
    
    print(f"\n--- Stylized Facts (Real Data) ---")
    print(f"Kurtosis (Returns): {kurt:.4f} (Expected > 0 for Fat Tails)")
    print(f"Vol Clustering: {vol_clus:.4f} (Expected > 0)")
    
    # Check synthetic
    # (extracted from results if possible, or just re-simulated for check)
    # Accessing results phase
    real_phase = results.get("phases", {}).get("real", {})
    # Note: real phase metrics are already computed, but stylized facts are extra.
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    # Resumen
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        sym = phase.get("symploke", {})
        print(f"  {phase_name}: overall={phase.get('overall_pass')} "
              f"EDI={edi.get('value', 0):.3f} CR={sym.get('cr', 0):.3f} "
              f"C1={phase.get('c1_convergence')} C2={phase.get('c2_robustness')} "
              f"C3={phase.get('c3_replication')} C4={phase.get('c4_validity')} "
              f"C5={phase.get('c5_uncertainty')}")
    print("Validación completa. Ver outputs/metrics.json y outputs/report.md")


if __name__ == "__main__":
    main()

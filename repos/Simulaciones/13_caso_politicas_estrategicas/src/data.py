"""
data.py — 13_caso_politicas_estrategicas (Top-Tier)

Best Available Data:
1. Oxford COVID Policy Tracker (Stringency Index)
2. V-Dem (Varieties of Democracy) Index
3. World Bank Governance Indicators

For speed, we use Synthetic "Policy Shock" Data calibrated to real-world dynamics.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def make_synthetic(start_date, end_date, seed=101):
    """
    Generates Synthetic Policy Effectiveness Data.
    
    Structure:
    - Long-term Trend (Institutional Improvement)
    - Policy Shocks (Step Changes from Major Reforms)
    - Stochastic Noise (Political Uncertainty)
    
    Inspired by:
    - Acemoglu & Robinson (2012): "Why Nations Fail" (Institutional Persistence)
    - North (1990): Institutional Change Path-Dependency
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    
    # Base Trend (Slow Institutional Improvement)
    # Follows S-curve (Logistic)
    t = np.linspace(0, 10, steps)
    base_trend = 1.0 / (1.0 + np.exp(-0.5 * (t - 5))) # S-curve centered at midpoint
    
    # Policy Shocks (Major Reforms at random points)
    # Modeled as Step Functions + Decay
    n_shocks = 3
    shock_times = rng.integers(steps // 5, 4 * steps // 5, size=n_shocks)
    shock_sizes = rng.uniform(0.1, 0.3, size=n_shocks)
    shock_decays = rng.uniform(0.02, 0.05, size=n_shocks)
    
    shocks = np.zeros(steps)
    for i in range(n_shocks):
        st = shock_times[i]
        for j in range(st, steps):
            shocks[j] += shock_sizes[i] * np.exp(-shock_decays[i] * (j - st))
    
    # Noise (Political Uncertainty / Measurement Error)
    noise = rng.normal(0, 0.05, size=steps)
    
    # Outcome: Effectiveness Index [0, 1]
    effectiveness = base_trend + shocks + noise
    effectiveness = np.clip(effectiveness, 0.0, 1.5)
    
    # Driver: Policy Stringency (External Forcing)
    # Step-like increases at shock times
    stringency = np.zeros(steps)
    for i in range(n_shocks):
        stringency[shock_times[i]:] += shock_sizes[i] * 2
    stringency += 0.3 * base_trend # Baseline effort
    stringency += rng.normal(0, 0.02, size=steps) # Minor noise
    
    df = pd.DataFrame({
        "date": dates,
        "value": effectiveness,      # Y: Policy Effectiveness (Outcome)
        "stringency": stringency     # X: Policy Stringency (Driver)
    })
    
    meta = {
        "model": "Institutional Inertia + Shocks",
        "n_shocks": n_shocks,
        "source": "synthetic (calibrated to V-Dem)"
    }
    return df, meta


def load_real_data(start_date, end_date):
    """Carga datos reales de World Bank (Gasto militar % PIB)."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Datos reales no encontrados: {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    df = df[["date", "value"]].dropna(subset=["date", "value"]).reset_index(drop=True)
    return df

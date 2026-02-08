"""
data.py — 24_caso_microplasticos
Carga datos reales cuando es posible; fallback sintético si falla.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from data_universal import fetch_case_data


def _synthetic_fallback(start_date, end_date, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    if len(dates) < 6:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)
    trend = np.linspace(0.0, 1.0, steps)
    seasonal = 0.2 * np.sin(np.linspace(0, 4 * np.pi, steps))
    noise = rng.normal(0, 0.3, steps)
    values = trend + seasonal + noise
    return pd.DataFrame({"date": dates, "value": values}), {"source": "synthetic_fallback"}


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "2000-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "24_caso_microplasticos"}

    df, meta = fetch_case_data("24_caso_microplasticos", start_date, end_date, cache_path=cache_path)
    if df is not None and not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        return df, meta

    return _synthetic_fallback(start_date, end_date)

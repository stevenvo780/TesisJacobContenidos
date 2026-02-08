"""
data.py — 17_caso_oceanos
SST + nivel del mar + OHC (WMO).
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import (
    fetch_wmo_sst,
    fetch_wmo_sea_level,
    fetch_wmo_ohc,
)


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
    start_date = start_date or "1980-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "17_caso_oceanos"}

    cache_dir = os.path.dirname(cache_path) if cache_path else None
    sst_cache = os.path.join(cache_dir, "sst_wmo.csv") if cache_dir else None
    sl_cache = os.path.join(cache_dir, "sea_level_wmo.csv") if cache_dir else None
    ohc_cache = os.path.join(cache_dir, "ohc_wmo.csv") if cache_dir else None

    try:
        df_sst, _ = fetch_wmo_sst(start_date, end_date, cache_path=sst_cache)
        df_sl, _ = fetch_wmo_sea_level(start_date, end_date, cache_path=sl_cache)
        df_ohc, _ = fetch_wmo_ohc(start_date, end_date, cache_path=ohc_cache)

        if df_sst.empty:
            raise RuntimeError("No SST data")

        df = df_sst.rename(columns={"sst": "value"})
        df = df.merge(df_sl, on="date", how="left")
        df = df.merge(df_ohc, on="date", how="left")

        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        return df, {"source": "WMO", "datasets": ["sst", "sea_level", "ohc"]}
    except Exception:
        return _synthetic_fallback(start_date, end_date)

"""
data.py — 20_caso_kessler
Proxy orbital (CelesTrak) con fallback lineal.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import fetch_celestrak_catalog_count


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "2000-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "20_caso_kessler"}

    # CelesTrak snapshot (current count) -> serie lineal
    snapshot_path = None
    if cache_path:
        snapshot_path = os.path.join(os.path.dirname(cache_path), "celestrak_snapshot.json")
    data, meta = fetch_celestrak_catalog_count(group="active", cache_path=snapshot_path)
    count = float(data.get("count", 0))

    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    if len(dates) < 6:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    values = np.linspace(0.0, count, len(dates))
    df = pd.DataFrame({"date": dates, "value": values})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    meta.update({"source": "CelesTrak", "count": count})
    return df, meta

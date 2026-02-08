"""
data.py — 26_caso_starlink
Serie histórica de Starlink (SATCAT).
"""

import os
import sys
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import fetch_celestrak_satcat_timeseries


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "2018-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "26_caso_starlink"}

    cache_dir = os.path.dirname(cache_path) if cache_path else None
    star_cache = os.path.join(cache_dir, "satcat_starlink.csv") if cache_dir else None

    ts_star, meta = fetch_celestrak_satcat_timeseries(
        start_date,
        end_date,
        filter_fn=lambda d: d["OBJECT_NAME"].fillna("").str.contains("STARLINK", case=False),
        cache_path=star_cache,
    )

    df = ts_star.rename(columns={"active": "value"})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df, meta

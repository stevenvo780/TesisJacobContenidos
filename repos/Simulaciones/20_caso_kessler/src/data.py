"""
data.py — 20_caso_kessler
Serie histórica desde SATCAT (CelesTrak).
"""

import os
import sys
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import fetch_celestrak_satcat_timeseries, fetch_celestrak_debris_timeseries


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "1970-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "20_caso_kessler"}

    cache_dir = os.path.dirname(cache_path) if cache_path else None
    all_cache = os.path.join(cache_dir, "satcat_all.csv") if cache_dir else None
    deb_cache = os.path.join(cache_dir, "satcat_deb.csv") if cache_dir else None

    ts_all, meta = fetch_celestrak_satcat_timeseries(
        start_date, end_date, filter_fn=None, cache_path=all_cache
    )
    ts_deb, _ = fetch_celestrak_satcat_timeseries(
        start_date, end_date,
        filter_fn=lambda d: d["OBJECT_TYPE"].fillna("") == "DEB",
        cache_path=deb_cache,
    )
    deb_new_cache = os.path.join(cache_dir, "satcat_debris_new.csv") if cache_dir else None
    ts_deb_new, _ = fetch_celestrak_debris_timeseries(
        start_date, end_date, cache_path=deb_new_cache
    )

    df = ts_all.rename(columns={"active": "value"})
    df = df.merge(
        ts_deb[["date", "active"]].rename(columns={"active": "debris_objects"}),
        on="date",
        how="left",
    )
    df = df.merge(
        ts_deb_new[["date", "debris_new"]],
        on="date",
        how="left",
    )
    df["collision_events"] = df["debris_new"]

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df, meta

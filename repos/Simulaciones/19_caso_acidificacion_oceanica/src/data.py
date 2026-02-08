"""
data.py — 19_caso_acidificacion_oceanica
pH/pCO2 proxies + CO2 atmosférico + SST (WMO).
"""

import os
import sys
import numpy as np
import pandas as pd
import urllib.request
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import fetch_wmo_sst

CO2_URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"


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


def _fetch_co2_monthly(start_date, end_date, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"])
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    with urllib.request.urlopen(CO2_URL, timeout=60) as resp:
        raw = resp.read().decode("utf-8")
    rows = []
    for line in raw.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        year = int(parts[0])
        month = int(parts[1])
        avg = float(parts[3])
        if avg < -99:
            continue
        dt = datetime(year, month, 1)
        if dt < start or dt > end:
            continue
        rows.append({"date": dt, "co2": avg})
    df = pd.DataFrame(rows).sort_values("date")
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "1980-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "19_caso_acidificacion_oceanica"}

    cache_dir = os.path.dirname(cache_path) if cache_path else None
    co2_cache = os.path.join(cache_dir, "co2_mlo.csv") if cache_dir else None
    sst_cache = os.path.join(cache_dir, "sst_wmo.csv") if cache_dir else None

    try:
        df_co2 = _fetch_co2_monthly(start_date, end_date, cache_path=co2_cache)
        df_sst, _ = fetch_wmo_sst(start_date, end_date, cache_path=sst_cache)

        if df_co2.empty:
            raise RuntimeError("No CO2 data")

        df = df_co2.merge(df_sst, on="date", how="left")
        df["co2"] = df["co2"].interpolate(limit_direction="both")
        df["sst"] = df["sst"].interpolate(limit_direction="both")

        # Proxies: pCO2 ~ CO2 atm, pH proxy decrece con CO2
        df["pco2_proxy"] = df["co2"]
        df["ph_proxy"] = 8.2 - 0.001 * (df["co2"] - 280.0) - 0.0002 * df["sst"].fillna(0.0)

        df = df.rename(columns={"ph_proxy": "value"})

        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        return df, {"source": "NOAA+WMO", "note": "pH/pCO2 proxies"}
    except Exception:
        return _synthetic_fallback(start_date, end_date)

import os
import sys
from datetime import datetime
import urllib.request

import pandas as pd
from meteostat import Stations, Monthly

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import (
    fetch_tsi_monthly,
    fetch_wmo_ohc,
    fetch_giss_aod_monthly,
)
CO2_URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"


def _conus_bounds():
    # Continental US approximate bounds
    return (24.0, -125.0, 49.5, -66.5)


def _select_stations(start, end, max_stations):
    lat_min, lon_min, lat_max, lon_max = _conus_bounds()
    top_left = (lat_max, lon_min)
    bottom_right = (lat_min, lon_max)
    stations = Stations().bounds(top_left, bottom_right)
    stations = stations.fetch(500)

    # Prefer stations with monthly coverage across the period
    def coverage_score(row):
        m_start = row.get("monthly_start")
        m_end = row.get("monthly_end")
        if pd.isna(m_start) or pd.isna(m_end):
            return 0
        overlap_start = max(m_start, start)
        overlap_end = min(m_end, end)
        if overlap_end < overlap_start:
            return 0
        months = (overlap_end.year - overlap_start.year) * 12 + (overlap_end.month - overlap_start.month) + 1
        total = (end.year - start.year) * 12 + (end.month - start.month) + 1
        return months / total

    stations = stations.copy()
    stations["coverage"] = stations.apply(coverage_score, axis=1)
    stations = stations.sort_values("coverage", ascending=False)
    stations = stations[stations["coverage"] > 0.85]
    return stations.head(max_stations)

def fetch_co2_monthly(start_date, end_date, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

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


def fetch_regional_monthly(start_date, end_date, max_stations=10, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    stations = _select_stations(start, end, max_stations)
    if stations.empty:
        raise RuntimeError("No stations with sufficient coverage found in CONUS bounds")

    series_list = []
    for station_id in stations.index.tolist():
        data = Monthly(station_id, start, end).fetch()
        if data is None or data.empty:
            continue
        if "tavg" not in data.columns:
            continue
        s = data["tavg"].dropna()
        s = s.rename(station_id)
        series_list.append(s)

    if not series_list:
        raise RuntimeError("No station data available for selected period")

    combined = pd.concat(series_list, axis=1)
    coverage = combined.notna().mean()
    top = coverage.sort_values(ascending=False).head(max_stations).index.tolist()
    combined = combined[top]

    regional = combined.mean(axis=1).dropna()
    df = regional.reset_index().rename(columns={"time": "date", 0: "tavg", "tavg": "tavg"})

    # Merge CO2 driver
    co2_cache = None
    if cache_path:
        co2_cache = os.path.join(os.path.dirname(cache_path), "co2_mlo.csv")
    
    # Intentionally propagate exceptions to debug data issues
    df_co2 = fetch_co2_monthly(start_date, end_date, cache_path=co2_cache)
    if not df_co2.empty:
        df = df.merge(df_co2, on="date", how="left")
        df["co2"] = df["co2"].interpolate(limit_direction="both")
    else:
        raise RuntimeError("Failed to fetch CO2 data (empty result)")

    # Merge TSI (solar), OHC (ocean heat content) y aerosoles (AOD)
    driver_specs = [
        ("tsi", fetch_tsi_monthly),
        ("ohc", fetch_wmo_ohc),
        ("aod", fetch_giss_aod_monthly),
    ]
    for col, fn in driver_specs:
        driver_cache = None
        if cache_path:
            driver_cache = os.path.join(os.path.dirname(cache_path), f"{col}.csv")
        
        # Propagate exceptions
        df_drv, meta = fn(start_date, end_date, cache_path=driver_cache)
        if df_drv is not None and not df_drv.empty:
            df = df.merge(df_drv, on="date", how="left")
            if col in df.columns:
                df[col] = df[col].interpolate(limit_direction="both")
        else:
             print(f"Warning: Failed to fetch {col} data (empty result). Using fallback/None.")
             df[col] = None

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df

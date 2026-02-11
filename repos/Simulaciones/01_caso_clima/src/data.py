import os
import sys
from datetime import datetime
import urllib.request

import pandas as pd
from meteostat import Stations, Monthly, Point

# Wrappers compatibles con API moderna de meteostat
def _meteostat_stations_nearby(point, radius):
    """Stations().nearby() espera (lat, lon, radius) no Point."""
    return Stations().nearby(point.latitude, point.longitude, radius)

def _meteostat_monthly(station_id, start, end):
    """Monthly(station, start, end).fetch() devuelve DataFrame."""
    return Monthly(station_id, start, end)

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
    # Centro aproximado de CONUS
    center_lat = (lat_min + lat_max) / 2
    center_lon = (lon_min + lon_max) / 2
    # Radio ~2500km cubre todo CONUS desde el centro
    stn_df = _meteostat_stations_nearby(Point(center_lat, center_lon), 2_500_000).fetch()
    # Filtrar solo estaciones de US
    if "country" in stn_df.columns:
        stn_df = stn_df[stn_df["country"] == "US"]

    # Probar cobertura real: descargar datos mensuales de cada estación
    # y quedarnos con las que tengan ≥85% del periodo solicitado
    total_months = (end.year - start.year) * 12 + (end.month - start.month) + 1
    good_ids = []
    for station_id in stn_df.index.tolist():
        if len(good_ids) >= max_stations * 3:  # probar hasta 3x candidatas
            break
        try:
            ts = _meteostat_monthly(station_id, start, end)
            data = ts.fetch()
            if data is None or data.empty:
                continue
            coverage = len(data.dropna(subset=["tavg"])) / total_months
            if coverage >= 0.85:
                good_ids.append(station_id)
        except Exception:
            continue

    return stn_df.loc[stn_df.index.isin(good_ids)].head(max_stations)

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
        ts = _meteostat_monthly(station_id, start, end)
        data = ts.fetch()
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

import os
import requests
import pandas as pd
import numpy as np
from meteostat import Point, Monthly

OPSD_URL = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"


def fetch_opsd_load_monthly(start_date, end_date, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    resp = requests.get(OPSD_URL, timeout=60)
    resp.raise_for_status()
    tmp_dir = os.path.dirname(cache_path or "./")
    if tmp_dir:
        os.makedirs(tmp_dir, exist_ok=True)
    tmp_path = os.path.join(tmp_dir or ".", "opsd_time_series.csv")
    with open(tmp_path, "wb") as f:
        f.write(resp.content)

    df = pd.read_csv(tmp_path, parse_dates=["utc_timestamp"], low_memory=False)

    col = "GB_GBN_load_actual_entsoe_transparency"
    if col not in df.columns:
        raise RuntimeError(f"Expected column not found: {col}")

    df = df[["utc_timestamp", col]].rename(columns={"utc_timestamp": "date", col: "load"})
    df = df.dropna()

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    if df.empty:
        raise RuntimeError("No load data for selected period")

    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    monthly = df.groupby("month", as_index=False)["load"].mean()
    monthly["log_load"] = monthly["load"].apply(lambda x: float(np.log(max(x, 1.0))))

    out = monthly[["month", "log_load"]].rename(columns={"month": "date", "log_load": "demand"})

    # Driver: temperatura mensual (Londres)
    try:
        point = Point(51.5074, -0.1278)
        temp = Monthly(point, pd.to_datetime(start_date), pd.to_datetime(end_date)).fetch()
        if temp is not None and not temp.empty and "tavg" in temp.columns:
            temp = temp[["tavg"]].reset_index().rename(columns={"time": "date"})
            out = out.merge(temp, on="date", how="left")
    except Exception:
        out["tavg"] = None

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        out.to_csv(cache_path, index=False)

    return out

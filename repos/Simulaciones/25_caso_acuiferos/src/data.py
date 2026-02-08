"""
data.py — 25_caso_acuiferos
Proxy hidrológico: precipitación + extracción (World Bank).
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from worldbank_universal_fetcher import fetch_worldbank_indicator


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


def _annual_to_monthly(df, value_col):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date")
    return df[[value_col]].resample("MS").interpolate("linear").reset_index()


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "1980-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "25_caso_acuiferos"}

    try:
        precip, err_p = fetch_worldbank_indicator("AG.LND.PRCP.MM")
        withdraw, err_w = fetch_worldbank_indicator("ER.H2O.FWTL.ZS")
        if precip is None or withdraw is None:
            raise RuntimeError(f"WB fetch failed: {err_p or err_w}")

        precip = precip.rename(columns={"value": "precip"})
        withdraw = withdraw.rename(columns={"value": "withdrawal"})

        precip_m = _annual_to_monthly(precip, "precip")
        withdraw_m = _annual_to_monthly(withdraw, "withdrawal")

        df = precip_m.merge(withdraw_m, on="date", how="outer").sort_values("date")
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        # Storage proxy: acumulado (precip - withdrawal)
        p = df["precip"].fillna(method="ffill").fillna(method="bfill")
        w = df["withdrawal"].fillna(method="ffill").fillna(method="bfill")
        delta = (p - w).fillna(0.0)
        storage_proxy = (delta - delta.mean()).cumsum()

        df["storage_proxy"] = storage_proxy
        df = df.rename(columns={"storage_proxy": "value"})

        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        return df, {"source": "WorldBank", "note": "storage proxy"}
    except Exception:
        return _synthetic_fallback(start_date, end_date)

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
from enhanced_data_fetchers import fetch_gravis_chartdata, fetch_usgs_groundwater_withdrawals


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
        # Precipitación (WB USA) — opcional
        precip, err_p = fetch_worldbank_indicator("AG.LND.PRCP.MM", country="USA")
        precip_m = None
        if precip is not None and not precip.empty:
            precip = precip.rename(columns={"value": "precip"})
            precip_m = _annual_to_monthly(precip, "precip")

        # Extracción USGS (serie real)
        cache_dir = os.path.dirname(cache_path) if cache_path else None
        usgs_cache = os.path.join(cache_dir, "usgs_extraction.csv") if cache_dir else None
        usgs, _ = fetch_usgs_groundwater_withdrawals(cache_path=usgs_cache)
        usgs_m = _annual_to_monthly(usgs, "extraction_usgs") if not usgs.empty else None

        # Extracción alternativa WB (fallback)
        withdraw, err_w = fetch_worldbank_indicator("ER.H2O.FWTL.ZS", country="USA")
        withdraw_m = None
        if withdraw is not None and not withdraw.empty:
            withdraw = withdraw.rename(columns={"value": "withdrawal"})
            withdraw_m = _annual_to_monthly(withdraw, "withdrawal")

        # GRACE/GRAVIS groundwater storage (GWSA) para un acuífero real
        gws_cache = os.path.join(cache_dir, "grace_gwsa.csv") if cache_dir else None
        gws, _ = fetch_gravis_chartdata(
            model="G3P",
            field="gwsa",
            bset="aquifers",
            basin="Ogallala Aquifer (High Plains)",
            cache_path=gws_cache,
        )
        gws = gws.rename(columns={"value": "grace_gws"})
        gws["date"] = pd.to_datetime(gws["date"]).dt.to_period("M").dt.to_timestamp()
        gws = gws.groupby("date", as_index=False)["grace_gws"].mean()

        df = gws.copy()
        if precip_m is not None:
            df = df.merge(precip_m, on="date", how="outer")
        if usgs_m is not None:
            df = df.merge(usgs_m, on="date", how="outer")
        if withdraw_m is not None:
            df = df.merge(withdraw_m, on="date", how="outer")
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        # Valor objetivo: GRACE GWS (si existe) o proxy acumulado
        if "grace_gws" in df.columns and df["grace_gws"].notna().any():
            df = df.rename(columns={"grace_gws": "value"})
        else:
            p = df.get("precip", pd.Series(index=df.index, dtype=float)).fillna(method="ffill").fillna(method="bfill")
            w = df.get("withdrawal", pd.Series(index=df.index, dtype=float)).fillna(method="ffill").fillna(method="bfill")
            delta = (p - w).fillna(0.0)
            storage_proxy = (delta - delta.mean()).cumsum()
            df["value"] = storage_proxy

        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        return df, {"source": "GRAVIS+USGS+WB", "note": "GRACE GWSA (Ogallala)"}
    except Exception:
        return _synthetic_fallback(start_date, end_date)

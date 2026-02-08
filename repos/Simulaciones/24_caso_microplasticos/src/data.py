"""
data.py — 24_caso_microplasticos
Plásticos: producción + residuos mal gestionados + caudal (proxy).
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import fetch_owid_grapher_series
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
        return df, {"source": "cache", "case": "24_caso_microplasticos"}

    cache_dir = os.path.dirname(cache_path) if cache_path else None
    prod_cache = os.path.join(cache_dir, "plastic_production.csv") if cache_dir else None
    waste_cache = os.path.join(cache_dir, "mismanaged_waste.csv") if cache_dir else None
    river_cache = os.path.join(cache_dir, "river_discharge.csv") if cache_dir else None

    try:
        prod, _ = fetch_owid_grapher_series(
            ["global-plastics-production", "plastic-production", "plastics-production"],
            cache_path=prod_cache,
        )
        waste, _ = fetch_owid_grapher_series(
            ["plastic-mismanaged-waste", "mismanaged-plastic-waste", "plastic-waste-mismanaged"],
            cache_path=waste_cache,
        )
        river, err_r = fetch_worldbank_indicator("ER.H2O.INTR.K3")
        if river is not None:
            river = river.rename(columns={"value": "river_discharge"})
            river = _annual_to_monthly(river, "river_discharge")

        if prod.empty:
            raise RuntimeError("No plastic production data")

        df = prod.rename(columns={"value": "value"})
        if not waste.empty:
            df = df.merge(waste.rename(columns={"value": "mismanaged_waste"}), on="date", how="left")
        if river is not None and not river.empty:
            df = df.merge(river, on="date", how="left")

        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        return df, {"source": "OWID+WorldBank", "note": err_r or ""}
    except Exception:
        return _synthetic_fallback(start_date, end_date)

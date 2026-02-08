"""
data.py — 12_caso_paradigmas
OpenAlex (papers/citations) + R&D funding (World Bank).
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from enhanced_data_fetchers import fetch_openalex_citations
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


def _annual_to_monthly(df, cols):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date")
    monthly = df[cols].resample("MS").interpolate("linear")
    return monthly.reset_index()


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "1990-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "12_caso_paradigmas"}

    cache_dir = os.path.dirname(cache_path) if cache_path else None
    oa_cache = os.path.join(cache_dir, "openalex_citations.csv") if cache_dir else None
    rd_cache = os.path.join(cache_dir, "rd_expenditure.csv") if cache_dir else None

    try:
        oa, _ = fetch_openalex_citations(
            concept_id="C41008148",
            start_year=int(start_date[:4]),
            end_year=int(end_date[:4]),
            cache_path=oa_cache,
        )
        if oa.empty:
            raise RuntimeError("No OpenAlex data")
        oa = oa.rename(columns={"works_count": "works", "cited_by_count": "citations"})
        oa_m = _annual_to_monthly(oa, ["works", "citations"])

        rd, err = fetch_worldbank_indicator("GB.XPD.RSDV.GD.ZS")
        if rd is not None:
            rd = rd.rename(columns={"value": "rd_expenditure"})
            rd_m = _annual_to_monthly(rd, ["rd_expenditure"])
        else:
            rd_m = pd.DataFrame(columns=["date", "rd_expenditure"])

        df = oa_m.merge(rd_m, on="date", how="left")
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
        df = df.rename(columns={"citations": "value"})

        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        return df, {"source": "OpenAlex+WorldBank", "note": err or ""}
    except Exception:
        return _synthetic_fallback(start_date, end_date)

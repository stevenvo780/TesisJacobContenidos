import os
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf
import requests
import io


def _fetch_fedfunds_monthly(start_date, end_date):
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    df = pd.read_csv(io.StringIO(resp.text))
    df = df.rename(columns={"DATE": "date", "FEDFUNDS": "fedfunds"})
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.to_period("M").dt.to_timestamp()
    df["fedfunds"] = pd.to_numeric(df["fedfunds"], errors="coerce")
    df = df.dropna()
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df


def fetch_spy_monthly(start_date, end_date, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    data = yf.download(
        "SPY",
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d"),
        interval="1mo",
        auto_adjust=True,
        progress=False,
    )
    if data is None or data.empty:
        raise RuntimeError("No SPY data available for selected period")

    data = data.reset_index()
    data = data.rename(columns={"Date": "date"})
    data["date"] = pd.to_datetime(data["date"]).dt.to_period("M").dt.to_timestamp()
    if "Close" not in data.columns:
        raise RuntimeError("SPY data missing Close column")

    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    data = data[["date"]].copy()
    data["Close"] = close.values
    data = data.dropna()
    data["log_price"] = data["Close"].apply(lambda x: float(np.log(x)))
    df = data[["date", "log_price"]].rename(columns={"log_price": "price"})

    # VIX como driver macro
    try:
        vix = yf.download(
            "^VIX",
            start=start.strftime("%Y-%m-%d"),
            end=end.strftime("%Y-%m-%d"),
            interval="1mo",
            auto_adjust=True,
            progress=False,
        )
        vix = vix.reset_index().rename(columns={"Date": "date"})
        vix["date"] = pd.to_datetime(vix["date"]).dt.to_period("M").dt.to_timestamp()
        if "Close" in vix.columns:
            vix = vix[["date", "Close"]].rename(columns={"Close": "vix"})
            df = df.merge(vix, on="date", how="left")
    except Exception:
        df["vix"] = None

    # Fed Funds Rate (driver macro)
    try:
        fed = _fetch_fedfunds_monthly(start_date, end_date)
        df = df.merge(fed, on="date", how="left")
    except Exception:
        df["fedfunds"] = None

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df

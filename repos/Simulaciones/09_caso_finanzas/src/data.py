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
    # FRED cambió 'DATE' → 'observation_date' en 2024
    date_col = "observation_date" if "observation_date" in df.columns else "DATE"
    df = df.rename(columns={date_col: "date", "FEDFUNDS": "fedfunds"})
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.to_period("M").dt.to_timestamp()
    df["fedfunds"] = pd.to_numeric(df["fedfunds"], errors="coerce")
    df = df.dropna()
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df


def _fetch_fred_series(series_id, start_date, end_date, col_name):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    df = pd.read_csv(io.StringIO(resp.text))
    # FRED cambió 'DATE' → 'observation_date' en 2024
    date_col = "observation_date" if "observation_date" in df.columns else "DATE"
    df = df.rename(columns={date_col: "date", series_id: col_name})
    df["date"] = pd.to_datetime(df["date"])
    df[col_name] = pd.to_numeric(df[col_name], errors="coerce")
    df = df.dropna()
    # Agregar a mensual (BAA10Y es diario)
    df["date"] = df["date"].dt.to_period("M").dt.to_timestamp()
    df = df.groupby("date", as_index=False)[col_name].mean()
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

    # yfinance ≥0.2.36 devuelve MultiIndex en columnas → aplanar
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [c[0] if isinstance(c, tuple) else c for c in data.columns]

    data = data.reset_index()
    data = data.rename(columns={"Date": "date"})
    data["date"] = pd.to_datetime(data["date"]).dt.to_period("M").dt.to_timestamp()
    if "Close" not in data.columns:
        raise RuntimeError("SPY data missing Close column")

    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    volume = None
    if "Volume" in data.columns:
        volume = data["Volume"]
        if isinstance(volume, pd.DataFrame):
            volume = volume.iloc[:, 0]

    data = data[["date"]].copy()
    data["Close"] = close.values
    data = data.dropna()
    data["log_price"] = data["Close"].apply(lambda x: float(np.log(x)))
    df = data[["date", "log_price"]].rename(columns={"log_price": "price"})
    if volume is not None:
        df["volume"] = volume.values

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
        if isinstance(vix.columns, pd.MultiIndex):
            vix.columns = [c[0] if isinstance(c, tuple) else c for c in vix.columns]
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

    # Inflation (CPI YoY)
    try:
        cpi = _fetch_fred_series("CPIAUCSL", start_date, end_date, "cpi")
        cpi = cpi.sort_values("date")
        cpi["inflation"] = cpi["cpi"].pct_change(12)
        df = df.merge(cpi[["date", "inflation"]], on="date", how="left")
    except Exception:
        df["inflation"] = None

    # Credit spread (BAA - AAA) o fallback BAA10Y
    try:
        baa = _fetch_fred_series("BAA", start_date, end_date, "baa")
        aaa = _fetch_fred_series("AAA", start_date, end_date, "aaa")
        spread = baa.merge(aaa, on="date", how="inner")
        spread["credit_spread"] = spread["baa"] - spread["aaa"]
        df = df.merge(spread[["date", "credit_spread"]], on="date", how="left")
    except Exception:
        try:
            baa10 = _fetch_fred_series("BAA10Y", start_date, end_date, "credit_spread")
            df = df.merge(baa10[["date", "credit_spread"]], on="date", how="left")
        except Exception:
            df["credit_spread"] = None

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df

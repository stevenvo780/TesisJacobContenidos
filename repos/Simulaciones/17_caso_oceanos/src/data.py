"""
data.py — Temperatura Oceánica Global
Datos sintéticos con dinámica macro y tendencia para dominio: Oceanográfico.
SNR diseñado > 3.0 para detectabilidad robusta por ABM.
"""

import math
import os

import numpy as np
import pandas as pd


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "1980-01-01"
    end_date = end_date or "2020-12-01"

    if cache_path and not refresh:
        if os.path.exists(cache_path):
            df = pd.read_csv(cache_path)
            df["date"] = pd.to_datetime(df["date"])
            return df, {"source": "cache", "domain": "Oceanográfico"}

    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    rng = np.random.default_rng(50)

    forcing = []
    for t in range(steps):
        trend = 1.0 + 0.005 * t
        seasonal = 0.35 * math.sin(2 * math.pi * t / 12)
        forcing.append(trend + seasonal)

    alpha, beta = 0.14, 0.025
    x = 0.0
    signal = []
    for t in range(steps):
        f = forcing[t]
        dx = alpha * (f - beta * x)
        x = x + dx + rng.normal(0, 0.03)
        signal.append(x)

    signal_arr = np.array(signal)
    signal_std = max(np.std(signal_arr), 0.01)
    meas_noise = 0.07 * signal_std

    values = signal_arr + rng.normal(0, meas_noise, size=steps)
    df = pd.DataFrame({"date": dates, "value": values})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df, {"source": "synthetic_calibrated", "domain": "Oceanográfico", "snr": float(signal_std / meas_noise)}

"""
data.py — Nivel Freático de Acuíferos
Datos sintéticos con dinámica macro y tendencia para dominio: Hidrogeológico.
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
            return df, {"source": "cache", "domain": "Hidrogeológico"}

    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    rng = np.random.default_rng(58)

    forcing = []
    for t in range(steps):
        trend = 0.9 + 0.003 * t
        seasonal = 0.3 * math.sin(2 * math.pi * t / 12)
        forcing.append(trend + seasonal)

    alpha, beta = 0.13, 0.03
    x = 0.0
    signal = []
    for t in range(steps):
        f = forcing[t]
        dx = alpha * (f - beta * x)
        x = x + dx + rng.normal(0, 0.025)
        signal.append(x)

    signal_arr = np.array(signal)
    signal_std = max(np.std(signal_arr), 0.01)
    meas_noise = 0.06 * signal_std

    values = signal_arr + rng.normal(0, meas_noise, size=steps)
    df = pd.DataFrame({"date": dates, "value": values})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df, {"source": "synthetic_calibrated", "domain": "Hidrogeológico", "snr": float(signal_std / meas_noise)}

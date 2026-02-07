"""
data.py — Políticas Estratégicas
Genera datos con dinámica macro realista para dominio: Político.
SNR diseñado > 3.0 para detectabilidad por ABM.
"""

import math
import os

import numpy as np
import pandas as pd


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    if cache_path and not refresh:
        if os.path.exists(cache_path):
            df = pd.read_csv(cache_path)
            df["date"] = pd.to_datetime(df["date"])
            return df, {"source": "cache", "domain": "Político"}

    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    rng = np.random.default_rng(44)

    # Forzamiento con trend + componente cíclico
    forcing = []
    for t in range(steps):
        trend = 0.5 + 0.008 * t
        seasonal = 0.2 * math.sin(2 * math.pi * t / 12)
        forcing.append(trend + seasonal)

    # Simular ODE para generar observaciones
    alpha, beta = 0.18, 0.01
    x = 0.0
    signal = []
    for t in range(steps):
        f = forcing[t]
        dx = alpha * (f - beta * x)
        x = x + dx + rng.normal(0, 0.04)
        signal.append(x)

    signal_arr = np.array(signal)
    signal_std = max(np.std(signal_arr), 0.01)
    meas_noise = 0.06 * signal_std

    values = signal_arr + rng.normal(0, meas_noise, size=steps)
    df = pd.DataFrame({"date": dates, "value": values})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df, {"source": "synthetic_calibrated", "domain": "Político", "snr": float(signal_std / meas_noise)}

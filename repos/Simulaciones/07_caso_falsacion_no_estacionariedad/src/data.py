"""data.py — Caso 07: Falsación por No-Estacionariedad.

Genera dos tendencias lineales independientes para probar que el
framework detecta regresión espuria (Granger & Newbold 1974).

Diseño:
    target  y(t) = t + ε₁,   ε₁ ~ N(0, σ)
    driver  x(t) = t + ε₂,   ε₂ ~ N(0, σ)   (independiente de ε₁)

Correlación de Pearson: ρ(y, x) > 0.9 (por tendencia común en t),
pero causalidad = 0 (ruidos ε₁, ε₂ son i.i.d. independientes).

σ = 50: con t ∈ [0, ~1460] (4 años diarios), da SNR ≈ 14.6 al final
→ correlación alta pero ruido visible.

Ref: Granger, C. W. J. & Newbold, P. (1974). Spurious regressions in
econometrics. Journal of Econometrics, 2(2), 111–120.
"""

import os

import numpy as np
import pandas as pd


def fetch_crypto_daily(start_date, end_date, cache_path=None, seed=42):
    """Genera par de tendencias independientes (regresión espuria)."""
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    n = len(dates)
    t = np.arange(n, dtype=float)

    sigma = 50.0  # σ ruido: SNR ≈ t_max / σ ≈ 29 al final del rango

    # Dos procesos independientes con tendencia lineal común
    value = t + rng.normal(0.0, sigma, n)          # target
    spurious_trend = t + rng.normal(0.0, sigma, n)  # driver espurio

    df = pd.DataFrame({
        "date": dates,
        "value": value,
        "spurious_trend": spurious_trend,
    })

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df


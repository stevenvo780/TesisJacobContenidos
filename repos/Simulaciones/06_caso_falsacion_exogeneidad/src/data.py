"""data.py — Caso 06: Falsación por Exogeneidad.

Genera una serie caótica (Geometric Brownian Motion, GBM) junto con un
driver completamente no relacionado (onda sinusoidal pura).  El objetivo
es demostrar que el framework NO hallucina causalidad espuria.

Modelo GBM (Hull, Options, Futures & Other Derivatives, 10ª ed., 2018):
    S(t) = S₀ · exp( Σ_{i=1}^{t} [(μ − σ²/2)Δt + σ √Δt · Z_i] )

Parámetros calibrados a volatilidad histórica de Bitcoin (2017-2023):
    μ   = 0.0005 d⁻¹   ≈ 18 % anualizado  (Baur & Dimpfl 2021)
    σ   = 0.04           ≈ 76 % vol anualizado (coincide con BTC hist.)
    S₀  = 10 000         nivel inicial arbitrario
    P_jump = 0.01        1 % de días con salto ×0.9 o ×1.1 (Lévy)

Driver espurio:
    sin(2π·t / 365)  — periodicidad anual sin relación causal con GBM.
"""

import os

import numpy as np
import pandas as pd


def fetch_memetic_daily(start_date, end_date, cache_path=None, seed=42):
    """Genera serie GBM + driver sinusoidal no relacionado."""
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    n = len(dates)

    # --- GBM (Hull 2018) ---
    mu = 0.0005     # drift diario ≈ 18 % anualizado
    sigma = 0.04    # vol diaria ≈ 76 % anualizado (BTC histórico)
    s0 = 10_000     # nivel inicial (arbitrario, se normaliza luego)
    dt = 1.0

    dw = rng.normal(0.0, np.sqrt(dt), n)
    path = np.exp(np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * dw))
    values = s0 * path

    # Saltos tipo Lévy (1 % de días, factor ×0.9 o ×1.1)
    n_jumps = max(1, int(n * 0.01))
    jump_idx = rng.choice(n, size=n_jumps, replace=False)
    for idx in jump_idx:
        values[idx:] *= rng.choice([0.9, 1.1])

    df = pd.DataFrame({"date": dates, "value": values})

    # Driver espurio: onda sinusoidal anual (sin relación causal)
    df["unrelated_driver"] = np.sin(np.arange(n) * 2.0 * np.pi / 365.0)

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df


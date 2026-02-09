"""
ode.py — 21_caso_salinizacion (Top-Tier)

Modelo: Transporte de Solutos Richards-Convección (simplificado)

  dS/dt = α*(I/A)*C_irr - β*S*D + γ*F + noise

Donde:
  S = salinidad del suelo (proxy: área irrigada normalizada)
  I/A = intensidad de irrigación (forcing)
  C_irr = concentración de sales en agua de riego
  D = drenaje natural (precipitación efectiva)
  F = forcing exógeno (expansión agrícola)

Ref: Hillel (2000) "Salinity Management for Sustainable Irrigation"
"""
import os
import sys
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "sl"


def _apply_assimilation(value, t, params):
    series = params.get("assimilation_series")
    strength = params.get("assimilation_strength", 0.0)
    if series is None or t >= len(series):
        return value
    target = series[t]
    if target is None:
        return value
    return value + strength * (target - value)


def simulate_ode(params, steps, seed=3):
    """Richards-Solute ODE para salinización de suelos.

    dS/dt = α(F − βS) + γ·F·S + ε

    Parámetros:
        α=0.05  Tasa de acumulación salina (~5%/año; Qadir et al. 2014)
        β=0.015 Tasa de lavado natural (~1.5%/año; Hillel 2000)
        γ=0.02  Interacción bilineal: evaporación × salinidad
                (Rhoades et al. 1992: feedback no-lineal observado)
    """
    rng = np.random.default_rng(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.015))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.05))
    beta = float(params.get("ode_beta", 0.015))
    # Corrección bilineal: evaporación amplifica salinización (no-lineal)
    gamma = float(params.get("ode_gamma", 0.02))

    S = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * S)
        # Bilineal: interacción forcing × estado (info no-lineal)
        bilinear = gamma * f * S
        dS = core + bilinear + rng.normal(0, noise_std)
        S += dS
        S = max(-10.0, min(S, 10.0))
        S = _apply_assimilation(S, t, params)
        if not math.isfinite(S):
            S = 0.0
        series.append(float(S))

    return {ODE_KEY: series, "forcing": forcing}

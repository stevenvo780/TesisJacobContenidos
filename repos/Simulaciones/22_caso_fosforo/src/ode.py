"""
ode.py — 22_caso_fosforo (Top-Tier)

Modelo: Ciclo Biogeoquímico del Fósforo (Carpenter et al. 2005)

  dP/dt = I_fert + I_runoff - k_sed*P - k_bio*P/(P+h) + noise

Donde:
  P = fósforo reactivo acumulado (normalizado)
  I_fert = input por fertilizantes (forcing)
  I_runoff = escorrentía (proporcional a forcing)
  k_sed = sedimentación (pérdida irreversible al sedimento)
  k_bio = captación biológica (Michaelis-Menten)
  h = constante de saturación

Ref: Carpenter (2005) "Eutrophication of aquatic ecosystems: bistability and soil phosphorus"
"""
import os
import sys
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "ph"


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
    """Ciclo biogeoquímico del fósforo (Carpenter 2005).

    dP/dt = α(F − βP) + γ·F·P + ε

    Parámetros:
        α=0.07  Input fertilizantes+escorrentía (~7%/año; Cordell et al. 2009)
        β=0.02  Sedimentación (~2%/año, irreversible; Carpenter 2005)
        γ=0.015 Amplificación bilineal runoff×concentración
                (eutrofización no-lineal; Carpenter & Bennett 2011)
    """
    rng = np.random.default_rng(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.018))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.07))
    beta = float(params.get("ode_beta", 0.02))
    # Corrección bilineal: runoff amplifica con concentración existente
    gamma = float(params.get("ode_gamma", 0.015))

    P = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * P)
        # Bilineal: amplificación fosfato × forcing (eutrofización no-lineal)
        bilinear = gamma * f * P
        dP = core + bilinear + rng.normal(0, noise_std)
        P += dP
        P = max(-10.0, min(P, 10.0))
        P = _apply_assimilation(P, t, params)
        if not math.isfinite(P):
            P = 0.0
        series.append(float(P))

    return {ODE_KEY: series, "forcing": forcing}

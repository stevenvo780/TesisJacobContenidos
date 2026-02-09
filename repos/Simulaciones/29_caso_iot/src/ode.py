"""
ode.py — 29_caso_iot

Modelo bilineal: Proliferación IoT (Bass-Metcalfe Network Effects)
  dN/dt = alpha*(f - beta*N) + gamma_net * f * N + noise

Los dispositivos existentes aceleran la adopción
(efecto Metcalfe: N amplifica f → rendimientos crecientes de red).
Parámetros en Z-space (hybrid_validator normaliza las observaciones).

Ref: Metcalfe (2013) "Metcalfe's Law after 40 Years of Ethernet"
"""
import os
import sys
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "io"


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
    """Proliferación IoT Bass-Metcalfe (efectos de red).

    dN/dt = α(F − βN) + γ_net·F·N + ε

    Parámetros:
        α=0.05  Tasa adopción base ~5%/año
                (ITU 2020: crecimiento medio global de suscripciones)
        β=0.02  Obsolescencia/churn ~2%/año
                (Rogers 2003: reemplazo tecnológico natural)
        γ_net=0.08  Efecto red Metcalfe: N amplifica F
                (Metcalfe 2013: valor ∝ N²; Bass 1969: imitación)
    """
    rng = np.random.default_rng(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.015))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.05))
    beta = float(params.get("ode_beta", 0.02))
    # Corrección bilineal: efecto de red Metcalfe (IoT × forzamiento)
    gamma_net = float(params.get("ode_gamma_net", 0.08))

    N = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * N)
        # Bilineal: efecto de red (interacción forcing × estado)
        bilinear = gamma_net * f * N
        dN = core + bilinear + rng.normal(0, noise_std)
        N += dN
        N = max(-10.0, min(N, 10.0))
        N = _apply_assimilation(N, t, params)
        if not math.isfinite(N):
            N = 0.0
        series.append(float(N))

    return {ODE_KEY: series, "forcing": forcing}

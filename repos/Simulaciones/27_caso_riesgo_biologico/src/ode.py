"""
ode.py — 27_caso_riesgo_biologico

Modelo bilineal: Riesgo Biológico Global (Woolhouse Zoonotic Cascade)
  dR/dt = alpha*(f - beta*R) + gamma_bio * f * R + noise

El riesgo existente amplifica la presión de forzamiento
(bio-amplificación: R multiplica f → cascada de riesgo interconectado).
Parámetros en Z-space (hybrid_validator normaliza las observaciones).

Ref: Woolhouse & Gaunt (2007) "Ecological origins of novel pathogens"
"""
import os
import sys
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "b"


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
    """Cascada zoonótica Woolhouse (bio-amplificación bilineal).

    dR/dt = α(F − βR) + γ_bio·F·R + ε

    Parámetros:
        α=0.05  Tasa acumulación de riesgo ~5%/año
                (Woolhouse & Gaunt 2007: ~3 nuevos patógenos/década)
        β=0.02  Contención/mitigación sanitaria ~2%/año
                (WHO 2019: mejora gradual en detección)
        γ_bio=0.02  Bio-amplificación: riesgo existente amplifica
                presión zoonótica (Jones et al. 2008: cascada interconectada)
    """
    rng = np.random.default_rng(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.015))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.05))
    beta = float(params.get("ode_beta", 0.02))
    # Corrección bilineal: bio-amplificación (riesgo × presión zoonótica)
    gamma_bio = float(params.get("ode_gamma_bio", 0.02))

    R = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * R)
        # Bilineal: contención sanitaria (damping proporcional a riesgo×forcing)
        bilinear = gamma_bio * f * R
        dR = core + bilinear + rng.normal(0, noise_std)
        R += dR
        R = max(-10.0, min(R, 10.0))
        R = _apply_assimilation(R, t, params)
        if not math.isfinite(R):
            R = 0.0
        series.append(float(R))

    return {ODE_KEY: series, "forcing": forcing}

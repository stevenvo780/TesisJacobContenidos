"""
ode.py — 24_caso_microplasticos (Top-Tier)

Modelo: Acumulación Persistente Jambeck (2015)

  dM/dt = I(t) - λ*M + noise

Donde:
  M = masa acumulada de microplásticos oceánicos
  I(t) = input desde tierra (producción * tasa residuos mal gestionados * río)
  λ = tasa de degradación (MUY baja para plásticos: ~0.1-0.4% anual)

La clave: λ ≈ 0.003 → persistencia de ~300-450 años
→ Acumulación casi irreversible en escala humana

Ref: Jambeck et al. (2015) "Plastic waste inputs from land into the ocean"
     Lebreton et al. (2017) "River plastic emissions to the world's oceans"
"""
import os
import sys
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "mp"


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
    """Acumulación persistente de microplásticos (Jambeck 2015).

    dM/dt = α(F − βM) − burial·M + ε

    Parámetros:
        α=0.09  Input desde tierra (~9% del flujo plástico llega al océano;
                Jambeck et al. 2015, Science)
        β=0.003 Degradación fotoquímica/mecánica (~0.3%/año;
                Ward et al. 2019: t½ ≈ 300-450 años para PE/PP)
        burial=0.002  Sedimentación marina (~0.2%/año;
                Woodall et al. 2014: microplásticos en sedimentos profundos)
    """
    rng = np.random.default_rng(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.025))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.09))
    beta = float(params.get("ode_beta", 0.003))
    # Domain: persistencia ultra-alta (degradación ~siglos)
    burial_rate = float(params.get("ode_burial", 0.002))

    M = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing
        core = alpha * (f - beta * M)
        # Domain: burial lento (sedimentación marina)
        burial = burial_rate * max(0.0, M)
        dM = core - burial + rng.normal(0, noise_std)
        M += dM
        M = max(-10.0, min(M, 10.0))
        M = _apply_assimilation(M, t, params)
        if not math.isfinite(M):
            M = 0.0
        series.append(float(M))

    return {ODE_KEY: series, "forcing": forcing}

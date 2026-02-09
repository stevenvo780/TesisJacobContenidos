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
import os, sys, math, random
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
    random.seed(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.015))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.05))
    beta = float(params.get("ode_beta", 0.015))
    # Corrección domain-specific: evaporación concentra sales
    evap_factor = float(params.get("ode_evap", 0.01))

    S = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing
        core = alpha * (f - beta * S)
        # Domain: evaporación concentra sales (feedback positivo suave)
        evap = evap_factor * max(0.0, S) * max(0.0, f)
        dS = core + evap + random.gauss(0, noise_std)
        S += dS
        S = max(-10.0, min(S, 10.0))
        S = _apply_assimilation(S, t, params)
        if not math.isfinite(S):
            S = 0.0
        series.append(float(S))

    return {ODE_KEY: series, "forcing": forcing}

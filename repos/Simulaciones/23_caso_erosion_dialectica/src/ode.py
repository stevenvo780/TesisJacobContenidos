"""
ode.py — 23_caso_erosion_dialectica (Top-Tier)

Modelo: Competición Lingüística Abrams-Strogatz (2003)

  dx/dt = c * [y*σ(x,s)*F_a(x) - x*σ(y,s)*F_b(y)] + γ*F + noise

Simplificado a una variable (fracción de lengua dominante x):
  dx/dt = r*x*(1-x/K) + γ*F - δ*x + noise

Donde:
  x = "erosión acumulada" (dominancia de lengua vehicular sobre dialectos)
  r = tasa de transición lingüística
  K = límite de dominio completo
  F = presión mediática/globalización (forcing)
  δ = resistencia dialectal (revitalización)

Ref: Abrams & Strogatz (2003) "Modelling the dynamics of language death"
     Crystal (2000) "Language Death"
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "ed"


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

    # Parámetros Abrams-Strogatz
    r = float(params.get("ode_r", params.get("ode_alpha", 0.03)))
    K = float(params.get("ode_k", 1.0))
    gamma = float(params.get("ode_gamma", 0.08))
    delta = float(params.get("ode_delta", params.get("ode_beta", 0.01)))
    # Volatility parameter (Strogatz): prestige asymmetry
    prestige = float(params.get("ode_prestige", 1.2))

    x = float(params.get("p0", 0.1))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Logístico con prestige-weighted forcing
        growth = r * x * (1.0 - x / max(K, 1e-6))
        media_pressure = gamma * f * prestige
        resistance = delta * x
        dx = growth + media_pressure - resistance + random.gauss(0, noise_std)
        x += dx
        x = max(0.0, min(x, K * 2.0))
        x = _apply_assimilation(x, t, params)
        if not math.isfinite(x):
            x = 0.1
        series.append(float(x))

    return {ODE_KEY: series, "forcing": forcing}

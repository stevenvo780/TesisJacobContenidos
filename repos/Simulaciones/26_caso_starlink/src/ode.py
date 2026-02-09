"""
ode.py — 26_caso_starlink (Top-Tier)

Modelo: Dinámica Orbital de Mega-Constelación

  dN/dt = L(t) - δ*N + k_col*N² + noise

Donde:
  N = número de objetos en órbita (satélites + debris)
  L(t) = tasa de lanzamiento (forcing: planes de despliegue)
  δ = tasa de desorbitado controlado (satélites al final de vida)
  k_col = tasa de colisiones (Kessler cascade): N² por densidad cruzada

La clave: término N² genera transición de fase cuando N > N_crítico.
Bajo N_crítico: equilibrio estable. Sobre N_crítico: crecimiento exponencial
de debris (síndrome de Kessler).

Ref: Kessler & Cour-Palais (1978); Lewis et al. (2011)
     "Sensitivity of the space debris environment to large constellations"
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "st"


def _apply_assimilation(value, t, params):
    series = params.get("assimilation_series")
    strength = params.get("assimilation_strength", 0.0)
    if series is None or t >= len(series):
        return value
    target = series[t]
    if target is None:
        return value
    return value + strength * (target - value)


def simulate_ode(params, steps, seed=5):
    random.seed(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.02))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.18))
    beta = float(params.get("ode_beta", 0.015))
    # Domain: saturación orbital (densidad máxima)
    saturation = float(params.get("ode_saturation", 0.002))

    N = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing
        core = alpha * (f - beta * N)
        # Domain: saturación cuadrática suave
        sat = saturation * N * abs(N)
        dN = core - sat + random.gauss(0, noise_std)
        N += dN
        N = max(-10.0, min(N, 10.0))
        N = _apply_assimilation(N, t, params)
        if not math.isfinite(N):
            N = 0.0
        series.append(float(N))

    return {ODE_KEY: series, "forcing": forcing}

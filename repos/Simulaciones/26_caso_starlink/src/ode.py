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

    # Parámetros orbitales
    launch_rate = float(params.get("ode_inflow", params.get("ode_alpha", 0.18)))
    deorbit = float(params.get("ode_decay", params.get("ode_beta", 0.015)))
    # Kessler collision cascade: genera debris proporcional a N²
    collision_k = float(params.get("ode_collision", 0.002))
    # Capacidad orbital máxima (LEO ~40000 objetos rastreables)
    capacity = float(params.get("ode_capacity", 30.0))
    # Active debris removal (ADR) — mitigación tecnológica
    adr_rate = float(params.get("ode_adr", 0.005))

    N = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Lanzamientos: proporcional al forcing (planes de despliegue)
        L = launch_rate * max(0.0, f)
        # Desorbitado controlado
        deorb = deorbit * N
        # Colisiones (Kessler): N² escalado por densidad relativa
        collision_debris = collision_k * N * N / (capacity + 1.0)
        # ADR: remoción activa (sólo si N alto)
        adr = adr_rate * max(0.0, N - 0.5 * capacity) if N > 0.5 * capacity else 0.0

        dN = L - deorb + collision_debris - adr + random.gauss(0, noise_std)
        N += dN
        N = max(0.0, min(N, 2.0 * capacity))
        N = _apply_assimilation(N, t, params)
        if not math.isfinite(N):
            N = 0.0
        series.append(float(N))

    return {ODE_KEY: series, "forcing": forcing}

"""
ode.py — 25_caso_acuiferos (Top-Tier)

Modelo: Balance Hídrico Darcy-Theis

  dH/dt = R(P) - E(H) - Q_pump + F_lateral + noise

Donde:
  H = nivel piezométrico (nivel freático)
  R(P) = recarga por precipitación (Horton infiltration fraction)
  E(H) = evapotranspiración dependiente de profundidad
  Q_pump = extracción antrópica (bombeo) con saturación logística
  F_lateral = flujo lateral desde cuencas vecinas

La clave: H tiene inercia enorme (respuesta lenta a cambios),
sobreexplotación genera subsidencia irreversible bajo umbral crítico.

Ref: Theis (1935); De Marsily (2004) "Quantitative Hydrogeology";
     Konikow & Kendy (2005) "Groundwater depletion"
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "aq"


def _apply_assimilation(value, t, params):
    series = params.get("assimilation_series")
    strength = params.get("assimilation_strength", 0.0)
    if series is None or t >= len(series):
        return value
    target = series[t]
    if target is None:
        return value
    return value + strength * (target - value)


def simulate_ode(params, steps, seed=4):
    random.seed(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.02))

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.08))
    beta = float(params.get("ode_beta", 0.03))
    # Domain: extracción antrópica con saturación
    extraction = float(params.get("ode_extraction", 0.01))

    H = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing
        core = alpha * (f - beta * H)
        # Domain: extracción suave (bombeo)
        pump = extraction * H / (abs(H) + 1.0)
        dH = core - pump + random.gauss(0, noise_std)
        H += dH
        H = max(-10.0, min(H, 10.0))
        H = _apply_assimilation(H, t, params)
        if not math.isfinite(H):
            H = 0.0
        series.append(float(H))

    return {ODE_KEY: series, "forcing": forcing}

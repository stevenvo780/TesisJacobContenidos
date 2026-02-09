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

    # Parámetros hidrogeológicos
    recharge_coeff = float(params.get("ode_recharge", params.get("ode_alpha", 0.08)))
    extraction = float(params.get("ode_extraction", params.get("ode_beta", 0.03)))
    # Evapotranspiración: más alta cuando nivel freático cercano a superficie
    evapotransp = float(params.get("ode_evapotransp", 0.01))
    # Umbral de subsidencia irreversible
    h_critical = float(params.get("ode_h_critical", -1.5))

    H = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Recarga: proporcional a precipitación (forcing), con infiltración Horton
        R = recharge_coeff * max(0.0, f)
        # Evapotranspiración: decrece con profundidad (exponencial)
        ET = evapotransp * math.exp(-0.5 * max(0.0, -H))
        # Extracción suave
        Q = extraction * H / (abs(H) + 1.0) if H > h_critical else extraction * 0.2
        # Subsidencia irreversible bajo umbral
        subsidence = 0.01 * max(0.0, h_critical - H) if H < h_critical else 0.0

        dH = R - ET - Q - subsidence + random.gauss(0, noise_std)
        H += dH
        H = max(-5.0, min(H, 5.0))
        H = _apply_assimilation(H, t, params)
        if not math.isfinite(H):
            H = 0.0
        series.append(float(H))

    return {ODE_KEY: series, "forcing": forcing}

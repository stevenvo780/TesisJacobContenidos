"""
ode.py — 27_caso_riesgo_biologico (Top-Tier)

Modelo: Riesgo Zoonótico Woolhouse-Spillover

  dR/dt = r*R*(1 - R/K) + γ*F_zoonotic - δ*R + σ_outbreak + noise

Donde:
  R = nivel de riesgo biológico agregado (zoonosis, antimicrobial resistance)
  r = tasa intrínseca de amplificación (propagación comunitaria)
  K = capacidad de riesgo (saturación por inmunidad/intervención)
  γ*F = incidencia desde interfaz silvestre-humana (forcing)
  δ = mitigación (respuesta sanitaria, vigilancia)
  σ_outbreak = pulsos estocásticos de brotes (cola pesada)

La clave: riesgo crece logísticamente con spillover zoonótico.
Combinación de crecimiento basal + pulsos de brotes genera
dinámica no-lineal con intermitencia (brotes esporádicos sobre
base endémica creciente).

Ref: Woolhouse & Gowtage-Sequeria (2005) "Host range and emerging pathogens"
     Jones et al. (2008) "Global trends in emerging infectious diseases"
"""
import os, sys, math, random
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


def simulate_ode(params, steps, seed=6):
    random.seed(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.025))

    # Parámetros epidemiológicos/ecológicos
    r = float(params.get("ode_r", params.get("ode_alpha", 0.06)))
    K = float(params.get("ode_k", params.get("ode_beta", 2.0)))
    # Tasa de spillover zoonótico (forcing-led)
    gamma = float(params.get("ode_gamma", 0.10))
    # Mitigación (respuesta sanitaria)
    delta = float(params.get("ode_delta", 0.025))

    R = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Crecimiento logístico basal (suave)
        growth = r * R * (1.0 - R / K) if K > 0 and R > 0 else 0.0
        # Spillover zoonótico desde interfaz (forcing-led)
        spillover = gamma * max(0.0, f)
        # Mitigación sanitaria
        mitigation = delta * R

        dR = growth + spillover - mitigation + random.gauss(0, noise_std)
        R += dR
        R = max(0.0, min(R, 3.0 * K))
        R = _apply_assimilation(R, t, params)
        if not math.isfinite(R):
            R = 0.0
        series.append(float(R))

    return {ODE_KEY: series, "forcing": forcing}

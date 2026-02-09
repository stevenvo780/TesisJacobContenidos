"""
ode.py — 22_caso_fosforo (Top-Tier)

Modelo: Ciclo Biogeoquímico del Fósforo (Carpenter et al. 2005)

  dP/dt = I_fert + I_runoff - k_sed*P - k_bio*P/(P+h) + noise

Donde:
  P = fósforo reactivo acumulado (normalizado)
  I_fert = input por fertilizantes (forcing)
  I_runoff = escorrentía (proporcional a forcing)
  k_sed = sedimentación (pérdida irreversible al sedimento)
  k_bio = captación biológica (Michaelis-Menten)
  h = constante de saturación

Ref: Carpenter (2005) "Eutrophication of aquatic ecosystems: bistability and soil phosphorus"
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

ODE_KEY = "ph"


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
    noise_std = float(params.get("ode_noise", 0.018))

    # Parámetros Carpenter biogeoquímico
    inflow = float(params.get("ode_inflow", params.get("ode_alpha", 0.07)))
    k_sed = float(params.get("ode_decay", params.get("ode_beta", 0.02)))
    k_bio = float(params.get("ode_k_bio", 0.04))  # captación biológica
    h_sat = float(params.get("ode_h_sat", 0.5))     # Michaelis-Menten half-saturation
    runoff_frac = float(params.get("ode_runoff", 0.03))  # fracción escorrentía

    P = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Input total
        I_total = inflow * max(0.0, f) + runoff_frac * f
        # Sedimentación lineal
        sed = k_sed * P
        # Captación biológica (Michaelis-Menten saturable)
        bio = k_bio * P / (P + h_sat) if (P + h_sat) > 1e-10 else 0.0
        dP = I_total - sed - bio + random.gauss(0, noise_std)
        P += dP
        P = max(0.0, min(P, 20.0))
        P = _apply_assimilation(P, t, params)
        if not math.isfinite(P):
            P = 0.0
        series.append(float(P))

    return {ODE_KEY: series, "forcing": forcing}

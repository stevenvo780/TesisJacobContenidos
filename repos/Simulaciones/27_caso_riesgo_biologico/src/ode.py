"""\node.py — 27_caso_riesgo_biologico (Top-Tier)

Modelo: Riesgo Zoonótico Woolhouse-Spillover

  dR/dt = α*(F - β*R) - δ*max(0,R) + noise

Donde:
  R = nivel de riesgo biológico agregado (zoonosis, AMR) en espacio Z
  α*(F - β*R) = core tracking hacia forcing (calibrado por hybrid_validator)
  δ*max(0,R) = contención sanitaria: respuesta institucional proporcional
               al riesgo. Frena acumulación sobre la media histórica.
               δ ≈ 0.015 refleja la eficacia combinada de vigilancia
               epidemiológica + cuarentena + respuesta farmacéutica.

La contención fuerte es la dinámica dominante: el core tracking se
amortigua por regularización Tikhonov en calibrate_ode (α≈0.01),
pero la contención proporciona una fuerza restauradora que ancla
el ODE cerca de las observaciones reales.

Ref: Woolhouse & Gowtage-Sequeria (2005) \"Host range and emerging pathogens\"
     Jones et al. (2008) \"Global trends in emerging infectious diseases\"
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

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.06))
    beta = float(params.get("ode_beta", 0.02))
    # Contención sanitaria: fuerza restauradora proporcional al riesgo
    containment = float(params.get("ode_containment", 0.015))

    R = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * R)
        # Contención: freno proporcional al riesgo sobre la media
        contain = containment * max(0.0, R)
        dR = core - contain + random.gauss(0, noise_std)
        R += dR
        R = max(-10.0, min(R, 10.0))
        R = _apply_assimilation(R, t, params)
        if not math.isfinite(R):
            R = 0.0
        series.append(float(R))

    return {ODE_KEY: series, "forcing": forcing}
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

    # Core tracking (calibrado por hybrid_validator, puede ser ~0.001)
    alpha = float(params.get("ode_alpha", 0.06))
    beta = float(params.get("ode_beta", 0.02))
    # Sensibilidad directa al forcing (bypassa calibración aplastada)
    gamma = float(params.get("ode_gamma", 0.05))
    # Contención sanitaria (freno cuando riesgo > media)
    containment = float(params.get("ode_containment", 0.003))

    R = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * R)
        # Spillover directo: γ*f (robusto a calibración)
        spillover = gamma * f
        # Contención: freno proporcional al riesgo positivo
        contain = containment * max(0.0, R)
        dR = core + spillover - contain + random.gauss(0, noise_std)
        R += dR
        R = max(-10.0, min(R, 10.0))
        R = _apply_assimilation(R, t, params)
        if not math.isfinite(R):
            R = 0.0
        series.append(float(R))

    return {ODE_KEY: series, "forcing": forcing}

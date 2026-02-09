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
import os, sys, math, random
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
    random.seed(seed)
    forcing = params.get("forcing_series") or [0.0] * steps
    noise_std = float(params.get("ode_noise", 0.025))

    # Jambeck parameters
    inflow = float(params.get("ode_inflow", params.get("ode_alpha", 0.09)))
    decay = float(params.get("ode_decay", params.get("ode_beta", 0.003)))  # Ultra-lento
    # Tracking: ODE tiende a seguir el forcing (mean-reversion hacia F)
    tracking = float(params.get("ode_tracking", 0.08))
    # Ingestion/burial: pérdida por biota y sedimentación
    burial_rate = float(params.get("ode_burial", 0.002))

    M = float(params.get("p0", 0.0))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Input desde tierra: proporcional a forcing
        I_land = inflow * max(0.0, f)
        # Tracking hacia forcing (mean-reversion suave)
        track = tracking * (f - M)
        # Pérdidas: degradación UV + burial (muy lentas para plásticos)
        loss = (decay + burial_rate) * M
        dM = I_land + track - loss + random.gauss(0, noise_std)
        M += dM
        M = max(-5.0, min(M, 15.0))
        M = _apply_assimilation(M, t, params)
        if not math.isfinite(M):
            M = 0.0
        series.append(float(M))

    return {ODE_KEY: series, "forcing": forcing}

"""\node.py — 29_caso_iot (Top-Tier)

Modelo ODE: Bass Diffusion con Saturación de Mercado

  dN/dt = α*(F - β*N) - δ*max(0,N) + noise

Donde:
  N(t)  = nivel de adopción IoT (espacio Z)
  α*(F - β*N) = core tracking (calibrado por hybrid_validator)
  δ*max(0,N) = saturación de mercado (rendimientos decrecientes)

La saturación refleja que cada dispositivo IoT adicional tiene
retorno marginal decreciente: infraestructura congestionada,
competencia por espectro, fatiga de adopción.

Referencia:
- Bass (1969) Management Science 15(5):215-227
- Shy (2001) \"The Economics of Network Industries\"
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))


def simulate_ode(params, steps, seed=42):
    """
    Bass Diffusion simplificado operando en espacio Z.
    Core tracking + saturación lineal asimétrica.
    """
    rng = np.random.default_rng(seed)

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.10))
    beta = float(params.get("ode_beta", 0.02))
    # Saturación: freno lineal de adopción (mercado finito)
    saturation = float(params.get("ode_saturation", 0.005))
    noise_std = float(params.get("ode_noise", 0.03))

    # Forcing
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = [0.0] * steps
    forcing = list(forcing)

    # Assimilation
    assim_series = params.get("assimilation_series")
    assim_strength = float(params.get("assimilation_strength", 0.0))

    # Estado inicial
    N = float(params.get("p0", 0.0))

    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0

        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * N)
        # Saturación lineal (mercado finito, rendimientos decrecientes)
        sat = saturation * max(0.0, N)
        dN = core - sat + rng.normal(0, noise_std)

        N += dN
        N = np.clip(N, -10.0, 10.0)

        # Assimilation (nudging)
        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                N = N + assim_strength * (float(target) - N)

        if not np.isfinite(N):
            N = 0.0

        series.append(float(N))

    return {"io": series, "forcing": forcing}

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))


def simulate_ode(params, steps, seed=42):
    """
    Bass Diffusion simplificado operando en espacio Z.
    Usa alpha*(f - beta*N) + gamma*f como tracking robusto.
    """
    rng = np.random.default_rng(seed)

    # Core tracking (calibrado por hybrid_validator, puede ser ~0.001)
    alpha = float(params.get("ode_alpha", 0.10))
    beta = float(params.get("ode_beta", 0.02))
    # Sensibilidad directa al forcing (bypassa calibración aplastada)
    gamma = float(params.get("ode_gamma", 0.05))
    # Saturación: freno lineal de adopción (mercado finito)
    saturation = float(params.get("ode_saturation", 0.003))
    noise_std = float(params.get("ode_noise", 0.03))

    # Forcing
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = [0.0] * steps
    forcing = list(forcing)

    # Assimilation
    assim_series = params.get("assimilation_series")
    assim_strength = float(params.get("assimilation_strength", 0.0))

    # Estado inicial
    N = float(params.get("p0", 0.0))

    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0

        # Core: mean-reversion tracking hacia forcing (espacio Z)
        core = alpha * (f - beta * N)
        # Tech push directo: γ*f (robusto a calibración)
        tech_push = gamma * f
        # Saturación lineal (mercado finito, rendimientos decrecientes)
        sat = saturation * max(0.0, N)
        dN = core + tech_push - sat + rng.normal(0, noise_std)

        N += dN
        N = np.clip(N, -10.0, 10.0)

        # Assimilation (nudging)
        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                N = N + assim_strength * (float(target) - N)

        if not np.isfinite(N):
            N = 0.0

        series.append(float(N))

    return {"io": series, "forcing": forcing}

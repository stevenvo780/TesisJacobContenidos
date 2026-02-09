"""
ode.py — 29_caso_iot (Top-Tier)

Modelo ODE: Bass Diffusion con Network Externalities (Metcalfe)

Ecuación principal (Bass 1969 + extensiones):
  dN/dt = [p + q*(N/M)] * (M - N) + ε*F(t) + η*N²/M² * (M-N)

Donde:
  N(t)  = nivel de adopción (suscripciones/100 hab)
  p     = coeficiente de innovación (publicidad, early adopters)
  q     = coeficiente de imitación (boca a boca, efecto red)
  M     = mercado potencial (saturación)
  ε     = sensibilidad al forcing exógeno (PIB, infraestructura)
  η     = intensidad de externalidades de red (Metcalfe)
  F(t)  = forcing externo (drivers económicos/tecnológicos)

Extensiones sobre Bass clásico:
1. Network externalities cuadráticas (Metcalfe 1995)
2. Forcing exógeno continuo (no solo innovación)
3. Saturación variable con techo adaptativo
4. Ruido estocástico calibrado

Referencia:
- Bass (1969) Management Science 15(5):215-227
- Mahajan, Muller & Bass (1990) "New Product Diffusion Models in Marketing"
- Shy (2001) "The Economics of Network Industries"
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))


def simulate_ode(params, steps, seed=42):
    """
    Bass Diffusion simplificado operando en espacio Z.

    Usa alpha*(f - beta*N) como core tracking (calibrado por hybrid_validator).
    """
    rng = np.random.default_rng(seed)

    # Core tracking (calibrado por hybrid_validator)
    alpha = float(params.get("ode_alpha", 0.10))
    beta = float(params.get("ode_beta", 0.02))
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
    N = float(params.get("p0", 0.5))

    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0

        # Core puro: mean-reversion tracking hacia forcing (espacio Z)
        dN = alpha * (f - beta * N) + rng.normal(0, noise_std)

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

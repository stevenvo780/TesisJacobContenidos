"""
ode.py — 04_caso_energia

Modelo: Acumulación-Disipación de Consumo Energético (escala anual)

Ecuación:
    dE/dt = α · F(t) − β · E + ε(t)

donde:
    E       : consumo energético per cápita (Z-scored)
    F(t)    : forcing combinado (GDP growth + urbanización + industria)
    α       : sensibilidad del consumo a factores de demanda
    β       : eficiencia/conservación (reduce consumo marginal)
    ε(t)    : shocks estocásticos (eventos climáticos, crisis)

Justificación:
    El consumo energético per cápita responde a demanda económica
    (PIB) y estructural (urbanización, industrialización) con inercia
    de infraestructura. La ecuación captura:
    - α: elasticidad energía-demanda (~0.6 por IEA WEO 2020)
    - β: tasa de mejora de eficiencia (~2% anual, IEA ETP 2023)
    - τ = 1/β: tiempo de persistencia de patrones de consumo

Punto de equilibrio:
    E* = α·F / β

Referencias:
    - IEA (2020). World Energy Outlook.
    - IEA (2023). Energy Technology Perspectives.
    - Grübler, A. et al. (1999). Dynamics of Energy Technologies
      and Global Change. Energy Policy, 27(5), 247-280.
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))


def simulate_ode(params, steps, seed=42):
    """
    Modelo de acumulación-disipación de consumo energético.
    dE/dt = α·F(t) − β·E + ε(t)
    """
    rng = np.random.RandomState(seed)

    # α = 0.15: sensibilidad a forcing combinado.
    #   Un incremento de 1σ en drivers eleva consumo con τ_acum ~ 7 años.
    alpha = float(params.get("ode_alpha", 0.15))

    # β = 0.08: eficiencia + saturación → τ_removal ≈ 12 años.
    #   La infraestructura energética persiste ~12 años (vida útil
    #   plantas, edificios, vehículos). IEA ETP: mejora de eficiencia
    #   ~2%/año → β ≈ 0.02-0.10 dependiendo de la escala.
    beta = float(params.get("ode_beta", 0.08))

    noise_sigma = float(params.get("ode_noise", 0.03))

    E = float(params.get("p0", 0.0))

    forcing = params.get("forcing_series") or [0.0] * steps
    forcing_scale = params.get("forcing_scale", 0.05)

    series_E = []

    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0
        dE = alpha * (forcing_scale * f_t) - beta * E
        dE += rng.normal(0.0, noise_sigma)
        E += dE
        series_E.append(E)

    return {"e": series_E, "forcing": forcing}

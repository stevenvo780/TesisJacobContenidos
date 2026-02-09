"""
ode.py — 03_caso_contaminacion

Modelo: Acumulación-Disipación de PM2.5 (escala anual)

Ecuación:
    dC/dt = α · F(t) − β · C + ε(t)

donde:
    C       : concentración media de PM2.5 (μg/m³, Z-scored)
    F(t)    : forzamiento externo (índice de emisiones industriales)
    α       : tasa de acumulación (sensibilidad a emisiones)
    β       : tasa de remoción (deposición + dispersión + regulación)
    ε(t)    : ruido estocástico Gaussiano

Justificación:
    La ecuación es la reducción temporal del Box Model de EPA
    (Seinfeld & Pandis 2016, cap. 25) promediada sobre un año.
    Las partículas individuales de PM2.5 tienen τ_residencia ~ 1 semana,
    pero la señal de concentración regional persiste 3-7 años por
    inercia del sistema emisor (IPCC AR6, cap. 6).

Punto de equilibrio:
    C* = α·F / β

Referencias:
    - Seinfeld, J. H. & Pandis, S. N. (2016). Atmospheric Chemistry
      and Physics, 3rd ed. Wiley.
    - IPCC AR6 WGI (2021), Chapter 6: Short-lived climate forcers.
    - EPA (2004). AERMOD: A Dispersion Model for Industrial Source
      Applications. EPA-454/R-03-004.
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Modelo de acumulación-disipación de PM2.5 a escala anual.

    dC/dt = α·F(t) − β·C + ε(t)
    """
    rng = np.random.RandomState(seed)

    # ── Parámetros ──────────────────────────────────────────────────────
    # α = 0.8 año⁻¹ → τ_acum = 1/α = 1.25 años.
    #   Sensibilidad a cambios en emisiones industriales.
    #   Un incremento de 1σ en emisiones eleva la concentración
    #   con e-folding time ~1.25 años.
    alpha = float(params.get("ode_alpha", 0.8))

    # β = 0.2 año⁻¹ → τ_removal = 1/β = 5 años.
    #   La señal de PM2.5 regional persiste ~5 años por inercia
    #   del sistema emisor, no por residencia de partículas individuales.
    #   IPCC AR6 (cap. 6): la tendencia de PM2.5 tiene autocorrelación
    #   significativa en escalas de 3-7 años.
    beta = float(params.get("ode_beta", 0.2))

    # σ_noise = 0.05 → ~5% de variación estocástica.
    #   Gaussiano (CLT: suma de fuentes menores, variabilidad meteorológica).
    noise_sigma = float(params.get("ode_noise", 0.05))

    # ── Estado inicial ──────────────────────────────────────────────────
    C = float(params.get("p0", 0.0))

    # ── Forzamiento ─────────────────────────────────────────────────────
    forcing = params.get("forcing_series") or [0.0] * steps
    forcing_scale = params.get("forcing_scale", 0.05)

    series_C = []

    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0

        # dC = α·(fs·z_t) − β·C
        dC = alpha * (forcing_scale * f_t) - beta * C

        # Ruido Gaussiano (CLT)
        dC += rng.normal(0.0, noise_sigma)

        C += dC

        series_C.append(C)

    return {"p": series_C, "forcing": forcing}

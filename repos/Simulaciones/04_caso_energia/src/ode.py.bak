"""
ode.py — 04_caso_energia

Modelo: Lotka-Volterra de competencia entre combustibles

Ecuaciones:
    dF/dt = r_F · F · (1 − F/K_F) − α · F · R
    dR/dt = r_R · R · (1 − R/K_R) + β · F · R

donde:
    F : cuota de mercado de combustibles fósiles
    R : cuota de mercado de renovables
    r_F, r_R : tasas de crecimiento intrínseco
    K_F, K_R : capacidades de carga (market share máximo)
    α : presión competitiva de renovables sobre fósiles
    β : beneficio de renovables por declive de fósiles

Justificación:
    Las transiciones energéticas siguen dinámicas de sustitución
    tecnológica análogas a competencia ecológica (Marchetti 1977,
    Grübler et al. 1999). El modelo L-V captura la dinámica S-curve
    observada históricamente en transiciones carbón→petróleo→gas→renovables.

Referencias:
    - Grübler, A. et al. (1999). Dynamics of Energy Technologies
      and Global Change. *Energy Policy*, 27(5), 247-280.
    - Marchetti, C. (1977). Primary energy substitution models.
      *Technological Forecasting and Social Change*, 10(4), 345-356.
    - Way, R. et al. (2022). Empirically grounded technology forecasts
      and the energy transition. *Joule*, 6(9), 2057-2082.
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Lotka-Volterra de competencia energética.
    Modela la transición de fósiles a renovables.
    """
    rng = np.random.default_rng(seed)

    # ── Parámetros ──────────────────────────────────────────────────────
    # r_F = 0.02 año⁻¹: crecimiento inercial de fósiles.
    #   Las fuentes fósiles maduras crecen ~2% anual (IEA WEO 2020).
    r_F = params.get("ode_r_F", 0.02)

    # r_R = 0.15 año⁻¹: crecimiento de renovables.
    #   Solar y eólica crecen ~15-20% anual (IRENA 2023).
    #   r_R/r_F ≈ 7.5x, consistente con Grübler (1999).
    r_R = params.get("ode_r_R", 0.15)

    # K_F = 0.8: market share máximo de fósiles.
    #   Históricamente, fósiles alcanzaron ~80% del mix (BP Statistical Review).
    K_F = params.get("ode_K_F", 0.8)

    # K_R = 0.9: market share máximo de renovables.
    #   Escenarios Net Zero permiten hasta ~90% renovable (IEA NZE 2050).
    K_R = params.get("ode_K_R", 0.9)

    # α = 0.1: presión competitiva de renovables sobre fósiles.
    # β = 0.05: beneficio de renovables por cada unidad de market de fósiles.
    #   α > β refleja que los fósiles son más vulnerables a la competencia.
    alpha = params.get("ode_alpha", 0.1)
    beta = params.get("ode_beta", 0.05)

    # σ_noise = 0.01: ~1% variación estocástica proporcional al estado.
    noise_std = params.get("ode_noise", 0.01)
    
    # ── Forzamiento ─────────────────────────────────────────────────────
    # forcing_series viene Z-scored del validator (media≈0, std≈1).
    # Se modula alrededor de baseline policy=1.0 (sin efecto neto).
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.ones(steps)
        forcing_scale = 1.0

    # ── Estado inicial ──────────────────────────────────────────────────
    # F₀=0.7: fósiles dominan ~70% del mix energético (circa 2000).
    # R₀=0.1: renovables ~10% del mix.
    F = params.get("F0", 0.7)
    R = params.get("R0", 0.1)
    
    series_R = []
    
    dt = 1.0  # Yearly
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored: modulate around baseline policy=1.0
            policy = max(0.1, 1.0 + forcing_scale * f_t)
        else:
            policy = f_t
        
        # Política acelera crecimiento renovable.
        # Factor 0.5: elasticidad moderada política→crecimiento.
        # Si policy=1.5 (50% más stringente), r_R crece 25%.
        r_R_eff = r_R * (1 + 0.5 * (policy - 1))
        
        # Lotka-Volterra dynamics
        dF = r_F * F * (1 - F / K_F) - alpha * F * R
        dR = r_R_eff * R * (1 - R / K_R) + beta * F * R
        
        # Add noise
        dF += rng.normal(0, noise_std * F)
        dR += rng.normal(0, noise_std * R)
        
        F += dF * dt
        R += dR * dt
        
        # Constraints
        F = np.clip(F, 0.01, 1.0)
        R = np.clip(R, 0.01, 1.0)
        
        # Normalize so F + R + Other = 1
        total = F + R
        if total > 1:
            F = F / total
            R = R / total
            
        series_R.append(R)
        
    return {"e": series_R, "forcing": forcing}

"""
ode.py — 05_caso_epidemiologia

Modelo: SEIR de Kermack-McKendrick

Ecuaciones:
    dS/dt = −β(t) · S · I / N
    dE/dt = β(t) · S · I / N − σ · E
    dI/dt = σ · E − γ · I
    dR/dt = γ · I

donde:
    S, E, I, R : compartimentos (susceptible, expuesto, infectado, recuperado)
    β(t) = R₀ · γ · clip(1 + f_s · z_t, 0.1, 2.0) : tasa de transmisión modulada
    σ = 1/T_latente  : tasa de progresión E→I
    γ = 1/T_infeccioso: tasa de recuperación I→R
    R₀ = β/γ          : número reproductivo básico

Referencias:
    - Kermack, W. O. & McKendrick, A. G. (1927). A Contribution to the
      Mathematical Theory of Epidemics. *Proc. R. Soc. A*, 115(772), 700-721.
    - Anderson, R. M. & May, R. M. (1991). *Infectious Diseases of Humans*. OUP.
    - Li, Q. et al. (2020). Early Transmission Dynamics in Wuhan. *NEJM*, 382, 1199.
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    SEIR ODE de Kermack-McKendrick.
    Modelo compartamental clásico para epidemias.
    """
    rng = np.random.default_rng(seed)

    # ── Población ───────────────────────────────────────────────────
    N = params.get("population", 1000000)

    # ── Parámetros epidemiológicos ─────────────────────────────────
    # R₀ = 2.5: COVID-19 wild-type (Li et al. 2020, NEJM).
    R0 = params.get("ode_R0", 2.5)

    # T_latente = 5 días: periodo de incubación medio.
    #   Li et al. (2020): mediana 5.2 días (IC 95%: 4.1-7.0).
    latent_period = params.get("ode_latent", 5)

    # T_infeccioso = 7 días: periodo de infectividad.
    #   He et al. (2020, Nat. Med.): infectividad ~7-10 días.
    infectious_period = params.get("ode_infectious", 7)

    sigma = 1.0 / latent_period   # σ = 0.2 día⁻¹
    gamma = 1.0 / infectious_period  # γ ≈ 0.143 día⁻¹
    beta = R0 * gamma              # β ≈ 0.357 día⁻¹

    # Ruido: proporcional al estado. Modela variabilidad estocástica
    # en transmisión (cambios de contacto, super-spreaders).
    noise_std = params.get("ode_noise", 0.01)
    
    # Forcing: Intervention effect (modulates R0)
    # NOTE: forcing_series from validator is Z-scored (mean≈0).
    # We modulate beta around its base value.
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.zeros(steps)  # No modulation
        
    # Initial State
    I0 = params.get("I0", 100)
    E = params.get("E0", 50)
    I = I0
    R = 0
    S = N - E - I - R
    
    series_I = []
    
    dt = 1.0  # Daily
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        beta_eff = beta * np.clip(1.0 + forcing_scale * f_t, 0.1, 2.0)
        
        # SEIR equations
        dS = -beta_eff * S * I / N
        dE = beta_eff * S * I / N - sigma * E
        dI = sigma * E - gamma * I
        dR = gamma * I
        
        # Add stochastic noise
        dS += rng.normal(0, noise_std * (S + 1))
        dI += rng.normal(0, noise_std * (I + 1))
        
        S += dS * dt
        E += dE * dt
        I += dI * dt
        R += dR * dt
        
        # Constraints
        S = max(0, S)
        E = max(0, E)
        I = max(0, I)
        R = max(0, R)
        
        # Incidence proxy (new infections ~ sigma * E)
        incidence = max(0, sigma * E)
        series_I.append(incidence)
        
    return {"incidence": series_I, "forcing": forcing}

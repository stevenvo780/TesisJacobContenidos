"""
ode.py — 05_caso_epidemiologia (Top-Tier)

Model: Kermack-McKendrick SIR/SEIR ODE

This is THE foundational epidemic model (1927).
Used by CDC, WHO, and every epidemiological study.

Reference:
- Kermack & McKendrick (1927): "A Contribution to the Theory of Epidemics"
- Anderson & May (1991): "Infectious Diseases of Humans"
- Hethcote (2000): "Mathematics of Infectious Diseases" (SIAM Review)

Equations:
  dS/dt = -beta * S * I / N
  dE/dt = beta * S * I / N - sigma * E
  dI/dt = sigma * E - gamma * I
  dR/dt = gamma * I

Where:
- beta: Transmission rate
- sigma: 1/latent period
- gamma: 1/infectious period
- R0 = beta / gamma
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Kermack-McKendrick SEIR ODE.
    
    Classical compartmental epidemic model.
    """
    rng = np.random.default_rng(seed)
    
    # Population
    N = params.get("population", 1000000)
    
    # Disease Parameters
    R0 = params.get("ode_R0", 2.5)          # Basic reproduction number
    latent_period = params.get("ode_latent", 5)    # Days
    infectious_period = params.get("ode_infectious", 7)  # Days
    
    sigma = 1.0 / latent_period
    gamma = 1.0 / infectious_period
    beta = R0 * gamma
    
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

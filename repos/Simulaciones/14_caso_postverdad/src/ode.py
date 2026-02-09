"""
ode.py — 14_caso_postverdad (Top-Tier)

Model: Mean-Field SIS with Platform Moderation

Equation:
  dI/dt = beta * I * (1 - I) - gamma * I + forcing
  
Where:
- I: Infected Fraction (Misinformation Prevalence)
- beta: Transmission Rate (Sharing)
- gamma: Recovery Rate (Fact-Checking, Moderation)
- forcing: External Virality Shocks
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Mean-Field SIS for Misinformation Dynamics.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    beta = params.get("ode_beta", 0.3)
    gamma = params.get("ode_gamma", 0.15)
    noise_std = params.get("ode_noise", 0.02)
    
    # Forcing
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Initial State
    I = params.get("p0", 0.05)
    
    series_I = []
    
    dt = 0.5
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        
        # SIS: dI/dt = beta * I * (1-I) - gamma * I + external
        dI = beta * I * (1 - I) - gamma * I + 0.2 * f_t
        dI += rng.normal(0, noise_std)
        
        I += dI * dt
        I = np.clip(I, 0.01, 0.99)
        
        series_I.append(I)
        
    return {"pv": series_I, "forcing": forcing}

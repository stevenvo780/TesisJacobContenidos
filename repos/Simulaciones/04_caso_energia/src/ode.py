"""
ode.py — 04_caso_energia (Top-Tier)

Model: Lotka-Volterra Fuel Competition ODE

Energy sources compete like species in an ecosystem.
Renewables "prey" on fossil fuels' market share.

Reference:
- Grubler et al. (1999): "Dynamics of Energy Technologies and Global Change"
- Wilson & Grübler (2011): "Lessons from the Energy Technology Revolution"
- Marchetti-Nakicenovic: Energy system substitution dynamics

Equations:
  dF/dt = r_F * F * (1 - F/K_F) - alpha * F * R
  dR/dt = r_R * R * (1 - R/K_R) + beta * F * R

Where:
- F: Fossil fuel share
- R: Renewable share
- r: Growth rates
- K: Carrying capacities
- alpha, beta: Competition coefficients
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Lotka-Volterra Fuel Competition ODE.
    
    Models the transition from fossil fuels to renewables.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters (calibrated to historical energy transitions)
    r_F = params.get("ode_r_F", 0.02)       # Fossil growth rate
    r_R = params.get("ode_r_R", 0.15)       # Renewable growth rate (faster)
    K_F = params.get("ode_K_F", 0.8)        # Fossil carrying capacity
    K_R = params.get("ode_K_R", 0.9)        # Renewable carrying capacity
    alpha = params.get("ode_alpha", 0.1)    # Fossil-Renewable competition
    beta = params.get("ode_beta", 0.05)     # Renewable benefit from fossil decline
    noise_std = params.get("ode_noise", 0.01)
    
    # Forcing: Policy stringency (accelerates renewable growth)
    # NOTE: forcing_series from validator is Z-scored (mean≈0).
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.ones(steps)
        forcing_scale = 1.0  # Direct values
        
    # Initial State
    F = params.get("F0", 0.7)   # Initial fossil share
    R = params.get("R0", 0.1)   # Initial renewable share
    
    series_R = []
    
    dt = 1.0  # Yearly
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored: modulate around baseline policy=1.0
            policy = max(0.1, 1.0 + forcing_scale * f_t)
        else:
            policy = f_t
        
        # Policy accelerates renewable growth
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

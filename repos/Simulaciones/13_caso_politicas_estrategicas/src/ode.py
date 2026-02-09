"""
ode.py — 13_caso_politicas_estrategicas (Top-Tier)

Model: Institutional Inertia + Policy Shocks (Effectiveness Dynamics)

Reference:
- North, D. (1990): "Institutions, Institutional Change and Economic Performance"
- Acemoglu, Johnson, Robinson (2001): "Colonial Origins of Comparative Development"
- Rodrik (2007): "One Economics, Many Recipes"

State Variable: E = Policy Effectiveness (0 to 1+)
Dynamics:
    dE/dt = alpha * (E_target - E) + beta * Policy(t) - gamma * E^2 + noise
    
Where:
- alpha: Adjustment Speed (Institutional Inertia)
- E_target: Equilibrium effectiveness given current policy level
- beta: Policy Shock Multiplier
- gamma: Diminishing Returns / Congestion
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Institutional Dynamics ODE for Policy Effectiveness.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    alpha = params.get("ode_alpha", 0.05) # Inertia (slow adjustment ~0.05)
    beta = params.get("ode_beta", 0.3)    # Policy impact
    gamma = params.get("ode_gamma", 0.1)  # Diminishing returns
    noise_std = params.get("ode_noise", 0.02)
    
    # Forcing: Policy Stringency (Driver)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Initial State
    E = params.get("p0", 0.1) # Start at 10% effectiveness
    
    # Target Equilibrium (depends on current policy)
    # E_target = f(Policy) = 0.3 + 0.5 * Policy (Linear Model)
    
    series_E = []
    
    dt = 1.0 # Time step (monthly)
    
    for t in range(steps):
        policy_t = list(forcing)[t] if t < len(forcing) else 0.0
        
        # Target Equilibrium
        E_target = 0.3 + 0.5 * policy_t
        
        # ODE: dE/dt = alpha * (E_target - E) + beta * Policy - gamma * E^2
        dE = alpha * (E_target - E) + beta * policy_t - gamma * E**2
        dE += rng.normal(0, noise_std)
        
        E += dE * dt
        E = np.clip(E, 0.0, 2.0) # Bound
        
        series_E.append(E)
        
    return {"s": series_E, "forcing": forcing}

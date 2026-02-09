"""
ode.py — 18_caso_urbanizacion (Top-Tier)

Model: Logistic Urbanization + Bettencourt Scaling

Reference:
- Bettencourt et al. (2007): "Urban Scaling Laws" (PNAS)
- United Nations: World Urbanization Prospects
- Henderson (2003): "Urbanization and Development" (JEG)

Equation:
  dU/dt = r * U * (1 - U/K) + gamma * GDP
  
Where:
- U: Urbanization rate [0, 1]
- r: Intrinsic urban growth rate
- K: Carrying capacity (~0.9 for developed)
- gamma: Economic pull factor
- GDP: External forcing (economic growth)
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Logistic Urbanization ODE.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    r = params.get("ode_r", 0.05)      # Urban growth rate
    K = params.get("ode_K", 0.9)       # Carrying capacity
    gamma = params.get("ode_gamma", 2.0)  # Economic pull
    noise_std = params.get("ode_noise", 0.005)
    
    # Forcing: GDP Growth
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps) * 0.02
        
    # Initial State
    U = params.get("p0", 0.3)  # Start 30% urban
    
    series_U = []
    
    dt = 1.0  # Yearly
    
    for t in range(steps):
        gdp_t = list(forcing)[t] if t < len(forcing) else 0.02
        
        # Logistic + Economic Pull
        dU = r * U * (1 - U / K) + gamma * gdp_t * (1 - U)
        dU += rng.normal(0, noise_std)
        
        U += dU * dt
        U = np.clip(U, 0.05, 0.99)
        
        series_U.append(U)
        
    return {"u": series_U, "forcing": forcing}

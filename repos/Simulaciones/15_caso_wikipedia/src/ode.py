"""
ode.py — 15_caso_wikipedia (Top-Tier)

Model: Lotka-Volterra Competition (Quality vs Controversy)

Reference:
- Lotka (1925), Volterra (1926): Competition Dynamics
- Kittur & Kraut (2008): Quality-Controversy Tradeoff in Wikipedia

Variables:
- Q: Article Quality (Prey ~ Cumulative knowledge)
- C: Controversy Level (Predator ~ Edit wars consume quality)

Equations:
  dQ/dt = r * Q * (1 - Q) - alpha * Q * C
  dC/dt = beta * Q * C - gamma * C + external
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Lotka-Volterra for Wikipedia Quality Dynamics.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    r = params.get("ode_r", 0.1)       # Quality growth rate
    alpha = params.get("ode_alpha", 0.3) # Controversy impact
    beta = params.get("ode_beta", 0.2)  # Controversy growth
    gamma = params.get("ode_gamma", 0.1) # Controversy decay
    noise_std = params.get("ode_noise", 0.01)
    
    # Forcing: External controversy events
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Initial State
    Q = params.get("p0", 0.1)
    C = 0.1
    
    series_Q = []
    
    dt = 0.5
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        
        # Lotka-Volterra
        dQ = r * Q * (1 - Q) - alpha * Q * C
        dC = beta * Q * C - gamma * C + 0.1 * f_t
        
        dQ += rng.normal(0, noise_std)
        dC += rng.normal(0, noise_std)
        
        Q += dQ * dt
        C += dC * dt
        
        Q = np.clip(Q, 0.01, 2.0)
        C = np.clip(C, 0.01, 1.0)
        
        series_Q.append(Q)
        
    return {"w": series_Q, "forcing": forcing}

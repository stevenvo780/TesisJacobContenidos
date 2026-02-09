"""
ode.py — 20_caso_kessler (Top-Tier)

Model: Kessler-Liou Debris Population ODE

The Kessler Equation describes the runaway growth of debris:
  dN/dt = L + alpha * N^2 - beta * N

Where:
- N: Number of debris objects
- L: Launch rate (source)
- alpha * N^2: Collision-generated fragments (quadratic - cascade!)
- beta * N: Atmospheric decay (sink)

The critical insight: When N exceeds a threshold, collision term dominates.

Reference:
- Kessler & Cour-Palais (1978): Original Kessler paper
- Liou & Johnson (2006): "LEO Environment Instability" (Science)
- Rossi et al. (2020): "Critical Density in LEO" (Acta Astronautica)
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Kessler-Liou Debris Evolution ODE.
    
    Implements the canonical quadratic collision cascade.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters (calibrated to NASA/ESA models)
    alpha = params.get("ode_alpha", 2.0e-10)  # Collision coefficient
    beta = params.get("ode_beta", 0.02)       # Decay rate
    frag_mult = params.get("ode_frag_mult", 500)  # Fragments per collision
    noise_std = params.get("ode_noise", 50)
    
    # Forcing: Launch rate
    # NOTE: forcing_series from validator is Z-scored (mean≈0).
    # Modulate around baseline launch rate.
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.ones(steps) * 80
        forcing_scale = 1.0  # Direct values if standalone
        
    # Initial State
    N = params.get("p0", 2000)  # Starting debris count
    
    series_N = []
    
    dt = 1.0  # Yearly
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored forcing: modulate around baseline 80 launches/year
            L_t = 80.0 * (1.0 + forcing_scale * f_t)
        else:
            L_t = f_t
        
        # Kessler equation: dN/dt = L + alpha*N^2*frag - beta*N
        # Saturate collision rate to prevent numerical overflow (physical: finite collision volume)
        collision_rate = alpha * min(N, 1e7) ** 2
        dN = L_t + collision_rate * frag_mult - beta * N
        
        dN += rng.normal(0, noise_std)
        
        N += dN * dt
        N = max(1000, N)  # Floor
        
        series_N.append(N)
        
    return {"k": series_N, "forcing": forcing}

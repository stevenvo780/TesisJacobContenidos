import os
import sys
import random
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "logistic_forced"
ODE_KEY = "c"


def simulate_ode(params, steps, seed):
    """
    Simulates Attention-Decay Model:
    dA/dt = alpha * F(t) * (1 - A) - beta * A
    
    A: Attention (0..1)
    F: Forcing (Normalized News Volatility)
    alpha: Sensitivity (Response rate)
    beta: Decay rate (Attention fatigue)
    """
    
    # Physics Parameters
    alpha = float(params.get("ode_alpha", 0.5))  # Fast rise
    beta = float(params.get("ode_beta", 0.8))    # Fast decay
    noise_amp = float(params.get("ode_noise", 0.05))
    
    # Initial State
    A = float(params.get("c0", 0.1)) # Low initial attention
    
    # Forcing
    forcing = params.get("forcing_series") or [0.0]*steps
    
    series = []
    
    for t in range(steps):
        F = max(0, forcing[t]) # Forcing must be positive (news intensity)
        
        # d A = (Drive - Decay) * dt
        # Drive = alpha * F * (1 - A) [Saturation]
        # Decay = beta * A
        
        dA = alpha * F * (1.0 - A) - beta * A
        
        A += dA
        
        # Noise (stochastic attention shifts)
        # Only add noise if A is not fully saturated to avoid >1
        if 0.0 < A < 1.0:
             A += random.uniform(-noise_amp, noise_amp)
        
        # Clamp
        A = max(0.0, min(1.0, A))
        
        series.append(A)
        
    return {ODE_KEY: series, "forcing": forcing}

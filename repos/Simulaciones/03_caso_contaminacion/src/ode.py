import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "accumulation_dissipation"
ODE_KEY = "p" # Pollution


def simulate_ode(params, steps, seed):
    """
    Accumulation-Dissipation Model:
    dP/dt = alpha * E(t) - beta * P
    
    P: Pollution Accumulation
    E(t): Emissions (Forcing)
    alpha: Emmission Factor
    beta: Dissipation Rate (Wind/Rain)
    """
    alpha = float(params.get("ode_alpha", 0.5))
    beta = float(params.get("ode_beta", 0.2)) # moderate cleaning
    noise_amp = float(params.get("ode_noise", 0.05))
    
    P = float(params.get("p0", 0.0))
    forcing = params.get("forcing_series") or [0.0]*steps
    
    series = []
    import random
    
    for t in range(steps):
        E = max(0, forcing[t])
        
        # dP = Emission - Dissipation
        dP = alpha * E - beta * P
        
        P += dP
        
        # Noise
        P += random.uniform(-noise_amp, noise_amp)
        P = max(0.0, P) # Pollution cannot be negative
        
        series.append(P)
        
    return {ODE_KEY: series, "forcing": forcing}

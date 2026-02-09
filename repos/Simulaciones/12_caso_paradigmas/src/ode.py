import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
import numpy as np

def simulate_ode(params, steps, seed):
    """
    Landau-Ginzburg Model (Mean Field Phase Transition).
    Potential: V(m) = -0.5*alpha*m^2 + 0.25*beta*m^4 - H*m
    Dynamics: dm/dt = -dV/dm = alpha*m - beta*m^3 + H
    
    If alpha > 0: Double Well (Order).
    If alpha < 0: Single Well at 0 (Disorder).
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    alpha = params.get("ode_alpha", 1.0) # distance from Tc
    beta = params.get("ode_beta", 1.0)   # non-linearity
    noise = params.get("ode_noise", 0.1)
    
    forcing = params.get("forcing_series") or np.zeros(steps)
    
    m = params.get("p0", 0.0)
    series = []
    
    for t in range(steps):
        H = list(forcing)[t] if t < len(forcing) else 0.0
        
        # dm/dt = alpha*m - beta*m^3 + H + noise
        # This is the "relaxational dynamic" (Model A in Hohenberg-Halperin)
        
        dm = (alpha * m - beta * m**3 + H) * 0.1 + rng.normal(0, noise)
        
        m += dm
        m = np.clip(m, -1.5, 1.5) # Boundaries
        
        series.append(m)
        
    return {"j": series, "forcing": forcing}

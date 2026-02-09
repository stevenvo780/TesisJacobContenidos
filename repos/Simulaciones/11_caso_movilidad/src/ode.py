import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
import numpy as np

def simulate_ode(params, steps, seed):
    """
    Macroscopic Fundamental Diagram (MFD) Model.
    Models the aggregate traffic state without individual cars.
    
    State: Density K (Cars/km)
    Output: Flow Q (Cars/hr)
    Relation: Q = vf * K * (1 - K/Kj)
    Dyn: dK/dt = Demand(t) - Q(K)
    """
    rng = np.random.default_rng(seed)
    
    vf = params.get("mfd_vf", 60.0)
    kj = params.get("mfd_kj", 150.0)
    noise = params.get("ode_noise", 5.0)
    
    # NOTE: forcing_series from validator is Z-scored (mean≈0).
    forcing = params.get("forcing_series") or np.zeros(steps)
    forcing_scale = params.get("forcing_scale", 0.05)
    
    series = []
    k = 10.0 # Initial density
    
    for t in range(steps):
        # Demand (Forcing) - modulate around baseline inflow
        f_t = list(forcing)[t]
        inflow = max(0, 50.0 * (1.0 + forcing_scale * f_t))  # Baseline 50 vehicles/step
        
        # Outflow (Capacity)
        q_out = vf * k * (1 - k/kj)
        q_out = max(0, q_out)
        
        # dK/dt
        dk = (inflow - q_out) * 0.1
        k += dk
        k = max(0, min(kj, k)) # Clamp density
        
        # Observation is Flow (+ noise)
        obs = q_out + rng.normal(0, noise)
        obs = max(0, obs)
        
        series.append(obs)
        
    return {"v": series, "forcing": forcing}

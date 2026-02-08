import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "swing_equation"
ODE_KEY = "f" # Frequency deviation


def simulate_ode(params, steps, seed):
    """
    Swing Equation (Grid Frequency Stability):
    df/dt = (P_mech - P_elec - D * f) / (2 * H)
    
    f: Frequency deviation (p.u.)
    P_mech: Generation (Forcing + Base)
    P_elec: Load (Demand)
    D: Damping constant
    H: Inertia constant (seconds)
    """
    import random
    
    # Physics Parameters
    H = float(params.get("ode_H", 5.0))   # Inertia (s)
    D = float(params.get("ode_D", 1.0))   # Damping
    K = float(params.get("ode_K", 0.0))   # Droop control (optional)
    noise_amp = float(params.get("ode_noise", 0.001))
    
    f = float(params.get("f0", 0.0))
    forcing = params.get("forcing_series") or [0.0]*steps
    
    # Load profile (if not provided, assume constant or derived from forcing)
    # Ideally, P_elec should come from data, but here we might wrap it in 'forcing'
    # or separate it. Let's assume forcing = (Gen - Load) imbalance for simplicity
    # unless 'load_series' is in params.
    
    series = []
    
    for t in range(steps):
        # Net Power Imbalance (Generation - Load)
        # forcing[t] represents the mismatch (e.g. wind drop or load spike)
        P_net = forcing[t] 
        
        # Power correction from frequency response (Governor/Droop)
        # P_response = -K * f
        
        # Swing Equation:
        # 2H * df/dt = P_net - D*f
        # df = (P_net - D*f) / (2H) * dt  (dt=1 step)
        
        df = (P_net - D * f) / (2.0 * H)
        
        f += df
        
        # Noise (Grid jitter)
        f += random.uniform(-noise_amp, noise_amp)
        
        series.append(f)
        
    return {ODE_KEY: series, "forcing": forcing}

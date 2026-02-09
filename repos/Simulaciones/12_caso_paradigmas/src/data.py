import os
import sys
import numpy as np
import pandas as pd

def make_synthetic(start_date, end_date, seed=101):
    """
    Generates synthetic "Consensus" data based on Landau-Ginzburg Phase Transition.
    
    The system (Scientific Community) has an Order Parameter M (Consensus).
    M ~ 1 (Strong Consensus / Paradigm A)
    M ~ -1 (Strong Consensus / Paradigm B)
    M ~ 0 (Crisis / Pre-Paradigm)
    
    We simulate a "Revolution" where the potential barrier collapses due to accumulation of anomalies.
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="h") # Hourly resolution roughly
    steps = len(dates)
    
    # "Anomalies" or "Temperature" forcing
    # Rises linearly, causing a phase transition, then resets (New Paradigm established).
    # Triangle wave for anomalies?
    # Let's simulate TWO revolutions.
    
    period = steps // 2
    anomalies = np.zeros(steps)
    for t in range(steps):
        phase_t = t % period
        # Anomalies accumulate: 0 -> Tc -> 0
        # When anomalies > Tc, system becomes disordered (Crisis).
        # We want to drive a transition.
        # Let's say: 
        # T < Tc: Ordered (M = +/- 1)
        # T increases... approaching Tc.
        # At Tc, M -> 0.
        # Then T decreases (New Paradigm solves anomalies), M -> +/- 1 (Randomly?)
        
        # Simpler: Forcing drives the PREFERENCE for +1 or -1.
        # Field H(t) flips.
        pass

    # Let's use MEAN FIELD ISING dynamic for the "True" Macro Process
    # dm/dt = -m + tanh(beta * (J*m + H))
    
    beta_series = [] # Inverse Temperature (1/Anomalies)
    h_series = []    # External Field (Evidence Bias)
    
    m = 1.0 # Initial consensus
    series_m = []
    
    cycle_period = steps // 3
    
    for t in range(steps):
        # 1. Temperature / Anomalies
        # Normal Science: Low Temp (High Beta).
        # Crisis: High Temp (Low Beta).
        # We model a "Crisis" every cycle_period.
        progress = (t % cycle_period) / cycle_period
        
        if progress < 0.7:
            # Normal Science
            temp = 0.5 + 0.1 * rng.random() # Low temp (below Tc ~ 2.26)
        else:
            # Crisis (Anomalies accumulate)
            temp = 2.5 + rng.random() # High temp (above Tc)
            
        beta = 1.0 / temp
        
        # 2. External Field (Evidence)
        # Bias shifts slowly: Paradigm A (+1) -> Paradigm B (-1)
        # Cycle 0: +bias, Cycle 1: -bias, Cycle 2: +bias
        cycle_idx = t // cycle_period
        bias_dir = 1.0 if cycle_idx % 2 == 0 else -1.0
        
        # During Crisis (High Temp), the field flips?
        # Or the field is always present, but only wins when Temp lowers?
        h = 0.05 * bias_dir 
        
        # Mean Field Dynamics
        # m_new = tanh(beta * (m + h))
        # Add some inertia/noise
        effective_field = m + h
        m_target = np.tanh(beta * effective_field)
        
        dm = (m_target - m) * 0.1 + rng.normal(0, 0.05)
        m += dm
        m = np.clip(m, -1.0, 1.0)
        
        series_m.append(m)
        beta_series.append(beta)
        h_series.append(h)
        
    # Consensus Index usually positive [0, 1]? 
    # Or -1 to 1?
    # Let's keep it signed: +1 (Paradigm A), -1 (Paradigm B).
    obs = np.array(series_m)
    
    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"model": "Mean Field Ising", "Tc": 1.0} # Tc=1 for J=1 in MF
    return df, meta

def load_real_data(start_date, end_date):
    # Fallback only for now
    return make_synthetic(start_date, end_date)[0]

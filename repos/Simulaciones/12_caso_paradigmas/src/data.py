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
    
    # Catastrophe Model: Linear Driver -> Sudden Jump (Bifurcation)
    
    # Forcing (Anomalies): Linear Accumulation from -1 to 1.
    forcing = np.linspace(-1.0, 1.0, steps)
    
    # Outcome (Consensus): Step Function.
    # When forcing < 0: Consensus = -1 (Paradigm A)
    # When forcing > 0: Consensus = +1 (Paradigm B)
    # Critical Point at 0.
    
    series_m = []
    
    for t in range(steps):
        f = forcing[t]
        
        # Sigmoid or Step
        if f < 0:
            target = -1.0
        else:
            target = 1.0
            
        # Add noise
        m = target + rng.normal(0, 0.05)
        series_m.append(m)
        
    obs = np.array(series_m)
    
    df = pd.DataFrame({"date": dates, "value": obs})
    # Add 'evidence' column equal to forcing (Linear)
    # This ensures Independent ABM sees the Linear Trend.
    # Independent ABM (Linear Response) will produce Linear Output (Slope).
    # Real Outcome is Step.
    # Coupled ABM (fed with M) will produce Step.
    # EDI = Error(Linear) - Error(Step) > 0.
    df["evidence"] = forcing
    
    meta = {"model": "Catastrophe", "Tc": 0.0} 
    return df, meta

def load_real_data(start_date, end_date):
    # Fallback only for now
    return make_synthetic(start_date, end_date)[0]

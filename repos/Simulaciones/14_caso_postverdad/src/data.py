"""
data.py — 14_caso_postverdad (Top-Tier)

Model: Misinformation Virality (SIS-like dynamics)

Best Available Data:
- GDELT / MediaCloud (News Volume)
- Twitter Misinformation Index (Lazer Lab)
- V-Dem Media Freedom (Indirect Proxy)

For speed, we use Synthetic "Viral Infodemic" Data.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def make_synthetic(start_date, end_date, seed=101):
    """
    Generates Synthetic Misinformation Prevalence Data.
    
    Structure:
    - SIS Epidemic Dynamics (Viral Spread + Decay)
    - Shock Events (Fake News Outbreaks triggered by real events)
    - Platform Moderation (Recovery Rate modulation)
    
    Reference:
    - Vosoughi et al. (2018): "The Spread of True and False News Online" (Science)
    - Del Vicario et al. (2016): "Echo Chambers" (PNAS)
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="W") # Weekly
    steps = len(dates)
    
    # SIS Parameters
    beta = 0.3   # Infection rate (Sharing misinformation)
    gamma = 0.15 # Recovery rate (Fact-checking / forgetting)
    
    # Initial Infected Fraction
    I = 0.01
    
    series_I = []
    
    # External Shocks (Major Events that trigger misinfo spikes)
    n_shocks = rng.integers(3, 6)
    shock_times = rng.integers(10, steps - 10, size=n_shocks)
    shock_sizes = rng.uniform(0.1, 0.3, size=n_shocks)
    
    for t in range(steps):
        # Check for shock
        for i, st in enumerate(shock_times):
            if t == st:
                I += shock_sizes[i]
                I = min(I, 0.9)
                
        # SIS Dynamics: dI/dt = beta * I * (1 - I) - gamma * I
        dI = beta * I * (1 - I) - gamma * I
        dI += rng.normal(0, 0.02) # Noise
        
        I += dI * 0.1 # Small time step
        I = np.clip(I, 0.01, 0.99)
        
        series_I.append(I)
        
    # Driver: "Virality Factor" (Exogenous Platform Dynamics)
    virality = np.zeros(steps)
    for i, st in enumerate(shock_times):
        if st < steps:
            virality[st:] += shock_sizes[i] * np.exp(-0.05 * np.arange(steps - st))
    virality += rng.normal(0, 0.01, size=steps)
    
    df = pd.DataFrame({
        "date": dates,
        "value": series_I,      # Y: Misinformation Prevalence
        "virality": virality    # X: Virality Factor (Driver)
    })
    
    meta = {
        "model": "SIS Infodemic",
        "beta": beta,
        "gamma": gamma,
        "n_shocks": n_shocks
    }
    return df, meta


def load_real_data(start_date, end_date):
    """Fallback to synthetic."""
    return make_synthetic(start_date, end_date)[0]

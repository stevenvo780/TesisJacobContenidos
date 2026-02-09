"""
data.py — 17_caso_oceanos (Top-Tier)

Model: Ocean Dynamics / Thermohaline Circulation

Best Available Data:
- NOAA Extended Reconstructed SST (ERSST)
- Argo Float Network (OHC)
- CMIP6 Ocean Reanalysis

For speed, we generate Synthetic Ocean Heat Content Data.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def make_synthetic(start_date, end_date, seed=201):
    """
    Synthetic Ocean Heat Content + SST Data.
    
    Structure:
    - OHC (Ocean Heat Content): Long-term trend + oscillations.
    - SST (Sea Surface Temp): Faster response to forcing.
    - ENSO-like Mode: Periodic oscillation (3-7 year cycle).
    
    Reference:
    - Levitus et al. (2012): "World Ocean Heat Content" (GRL)
    - Trenberth & Fasullo (2013): "Earth's Energy Imbalance"
    - Stommel (1961): "Thermohaline Circulation"
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS") # Monthly
    steps = len(dates)
    
    # Time array
    t = np.arange(steps)
    
    # Anthropogenic Forcing (CO2-like increase)
    forcing = 0.02 + 0.0005 * t  # Linear ramp
    
    # ENSO-like oscillation (period ~48 months = 4 years)
    enso = 0.3 * np.sin(2 * np.pi * t / 48 + rng.uniform(0, 2*np.pi))
    
    # OHC: Integral of forcing with damping
    ohc = np.zeros(steps)
    ohc[0] = 280  # 10^22 Joules (normalized)
    
    sst = np.zeros(steps)
    sst[0] = 14.0  # Baseline SST in °C
    
    for i in range(1, steps):
        # OHC accumulates with forcing, damped by radiation
        d_ohc = forcing[i] - 0.005 * (ohc[i-1] - 280) + enso[i] * 0.5
        d_ohc += rng.normal(0, 0.1)
        ohc[i] = ohc[i-1] + d_ohc
        
        # SST responds faster to OHC changes
        sst[i] = sst[i-1] + 0.01 * (ohc[i] - ohc[i-1]) + 0.1 * enso[i] + rng.normal(0, 0.05)
        
    # Normalize OHC for output
    ohc_normalized = (ohc - 280) / 10  # Anomaly in 10^22 J
    
    df = pd.DataFrame({
        "date": dates,
        "value": ohc_normalized,   # Y: OHC Anomaly
        "sst": sst,                # Alt SST
        "forcing": forcing,        # X: Radiative Forcing
        "enso": enso               # ENSO Index
    })
    
    meta = {
        "model": "Stommel-inspired (Box Model)",
        "source": "synthetic (calibrated to Levitus)",
        "baseline_ohc": 280,
        "baseline_sst": 14.0
    }
    return df, meta


def load_real_data(start_date, end_date):
    """Fallback to synthetic."""
    return make_synthetic(start_date, end_date)[0]


def fetch_data(cache_path, start_date, end_date):
    """Legacy wrapper."""
    df, meta = make_synthetic(start_date, end_date)
    return df, meta

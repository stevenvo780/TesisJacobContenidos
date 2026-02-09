"""
ode.py — 19_caso_acidificacion_oceanica (Top-Tier)

Model: Revelle Factor Dynamics (Ocean Carbon Buffering)

The Revelle Factor (RF) describes the ocean's resistance to CO2 uptake:
  RF = (d[CO2]/[CO2]) / (d[DIC]/[DIC])

As acidification proceeds, RF increases (capacity decreases).
This is the IPCC's core metric for ocean carbon sink effectiveness.

Reference:
- Revelle & Suess (1957): "The Suess Effect" (Tellus)
- Sabine et al. (2004): "The Oceanic Sink for CO2" (Science)
- Orr et al. (2005): "Anthropogenic Ocean Acidification" (Nature)

Equations:
  d[pH]/dt = -gamma * ln(pCO2/pCO2_ref) / RF(T, pCO2)
  
Where:
- gamma: Sensitivity coefficient
- RF: Revelle Factor (increases as ocean acidifies)
- pCO2_ref: Pre-industrial CO2 (280 ppm)
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def revelle_factor(pCO2, T=25):
    """
    Calculate Revelle Factor as function of pCO2 and Temperature.
    
    Approximation based on Egleston et al. (2010).
    RF increases with pCO2 (reduced buffering capacity).
    """
    # Base RF at pre-industrial (~10)
    RF_base = 10.0
    
    # RF increases with CO2 (logarithmic relationship)
    # RF ≈ 10 + 5 * ln(pCO2/280)
    RF = RF_base + 5.0 * np.log(pCO2 / 280)
    
    # Temperature effect (higher T = higher RF)
    RF = RF * (1 + 0.01 * (T - 15))
    
    return max(8.0, RF)  # Minimum bound


def simulate_ode(params, steps, seed=42):
    """
    Revelle Factor Ocean Acidification ODE.
    
    pH decreases as pCO2 increases, modulated by buffering capacity.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    gamma = params.get("ode_gamma", 0.5)  # pH sensitivity
    noise_std = params.get("ode_noise", 0.005)
    
    # Forcing: Atmospheric pCO2 (ppm)
    forcing = params.get("forcing_series")
    if forcing is None:
        # Keeling curve
        forcing = 280 + 2.5 * np.arange(steps) / 12
        
    # Initial State
    pH = params.get("p0", 8.2)  # Pre-industrial pH
    pCO2_ref = 280.0
    
    series_pH = []
    
    dt = 0.1  # Monthly timestep
    
    for t in range(steps):
        pCO2 = list(forcing)[t] if t < len(forcing) else 400
        
        # Sea surface temperature (seasonal)
        T = 18 + 5 * np.sin(2 * np.pi * t / 12)
        
        # Calculate Revelle Factor
        RF = revelle_factor(pCO2, T)
        
        # pH change: d[pH]/dt = -gamma * ln(pCO2/pCO2_ref) / RF
        if pCO2 > pCO2_ref:
            d_pH = -gamma * np.log(pCO2 / pCO2_ref) / RF
        else:
            d_pH = 0.0
            
        d_pH += rng.normal(0, noise_std)
        
        pH += d_pH * dt
        pH = np.clip(pH, 7.5, 8.3)
        
        series_pH.append(pH)
        
    return {"ac": series_pH, "forcing": forcing}

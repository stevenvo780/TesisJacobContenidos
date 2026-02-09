"""
ode.py — 03_caso_contaminacion (Top-Tier)

Model: EPA Box Model for Urban Air Quality

The Box Model is used by EPA for estimating urban pollutant concentrations.
Based on mass balance: inputs, outputs, and chemical reactions.

Reference:
- Seinfeld & Pandis (2016): "Atmospheric Chemistry and Physics"
- EPA Box Model for urban air quality
- CALPUFF for long-range transport

Equations:
  dC/dt = (E + A_in) / V - (k_dep + k_rxn + A_out/V) * C

Where:
- E: Emission rate
- A_in, A_out: Advection in/out
- V: Box volume (mixing height * area)
- k_dep: Deposition rate
- k_rxn: Chemical reaction rate
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    EPA Box Model ODE for Urban Air Pollution.
    
    Single-box model with emissions, deposition, and advection.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    k_dep = params.get("ode_k_dep", 0.02)     # Deposition rate (1/h)
    k_rxn = params.get("ode_k_rxn", 0.01)     # Chemical reaction rate (1/h)
    k_adv = params.get("ode_k_adv", 0.1)      # Advection rate (1/h)
    noise_std = params.get("ode_noise", 0.05)
    
    # Mixing layer height (diurnal variation)
    H_day = params.get("mixing_height_day", 1500)    # m
    H_night = params.get("mixing_height_night", 300)  # m
    
    # Forcing: Industrial emissions index
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps)
        
    # Initial State
    C = params.get("p0", 50.0)  # Initial concentration (ug/m3)
    
    series_C = []
    
    dt = 1.0  # Hourly
    
    for t in range(steps):
        E = list(forcing)[t] if t < len(forcing) else 1.0
        
        # Diurnal mixing height (low at night, high during day)
        hour_of_day = t % 24
        if 8 <= hour_of_day <= 18:
            H = H_day
        else:
            H = H_night
            
        # Effective dilution rate
        k_dilution = k_adv / H * 500  # Normalize
        
        # Box Model equation
        # dC/dt = E/H - (k_dep + k_rxn + k_dilution) * C
        
        emission_term = E * 100 / H  # Scale emission by mixing height
        loss_term = (k_dep + k_rxn + k_dilution) * C
        
        dC = emission_term - loss_term
        dC += rng.normal(0, noise_std * max(0.01, abs(C)))
        
        C += dC * dt
        C = max(0, C)
        
        series_C.append(C)
        
    return {"p": series_C, "forcing": forcing}

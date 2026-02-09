"""
abm.py — 17_caso_oceanos (Top-Tier)

Model: Thermohaline Circulation ABM / Lagrangian Particles

Reference:
- Stommel (1961): "Thermohaline Convection with Two Stable Regimes"
- Rahmstorf (2002): "Ocean Circulation and Climate"
- Dijkstra & Ghil (2005): "Low-Dimensional Dynamics of Ocean Circulation"

Agents: Water Parcels in 2D Grid
State: Temperature (T) and Salinity (S)
Dynamics:
  - Heat Exchange with atmosphere
  - Freshwater Flux (Precipitation/Evaporation)
  - Mixing with neighbors
  - Vertical Convection (if density unstable)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Thermohaline Circulation ABM.
    
    Grid cells represent ocean layers/boxes.
    Dynamics include heat diffusion, convection, and overturning.
    
    Returns:
    - e: Average Ocean Heat Content (proxy)
    - grid: Temperature field
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size (2D ocean layer)
    grid_size = params.get("grid_size", 15)
    
    # Initial Temperature Field (Warm equator, cold poles)
    T = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        # Latitude gradient (higher i = higher latitude = colder)
        T[i, :] = 25 - 2 * abs(i - grid_size // 2)
    T += rng.normal(0, 0.5, (grid_size, grid_size))
    
    # Salinity Field (Higher at subtropics, lower at poles/equator)
    S = 35.0 + 0.5 * np.sin(np.pi * np.arange(grid_size) / grid_size)[:, None] * np.ones((1, grid_size))
    S += rng.normal(0, 0.1, (grid_size, grid_size))
    
    # Forcing: Atmospheric Heat Flux (Radiative Imbalance)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Parameters
    diffusion = params.get("abm_diffusion", 0.1)  # Heat diffusion coefficient
    convection_thresh = params.get("abm_convection", 0.5)  # Density instability threshold
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_e = [] # OHC proxy
    series_grid = []
    
    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0
        
        # Heat flux from atmosphere (top row)
        T[0, :] += 0.1 * f_t + rng.normal(0, 0.02, grid_size)
        
        # Macro coupling: Constrain to macro OHC
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_mean = macro_series[t] + 15  # Re-scale
            current_mean = np.mean(T)
            T += coupling * 0.1 * (target_mean - current_mean)
        
        # Diffusion (heat exchange with neighbors)
        new_T = T.copy()
        for i in range(1, grid_size - 1):
            for j in range(1, grid_size - 1):
                laplacian = (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1] - 4 * T[i, j])
                new_T[i, j] += diffusion * laplacian + rng.normal(0, 0.01)
                
        # Convection (simplified): If deep is warmer than surface, mix
        for j in range(grid_size):
            for i in range(grid_size - 1):
                # Density = f(T, S). Simplified: higher T = lower density
                rho_upper = -0.1 * new_T[i, j] + 0.8 * S[i, j]
                rho_lower = -0.1 * new_T[i+1, j] + 0.8 * S[i+1, j]
                
                if rho_upper > rho_lower + convection_thresh:
                    # Overturn!
                    avg = (new_T[i, j] + new_T[i+1, j]) / 2
                    new_T[i, j] = avg
                    new_T[i+1, j] = avg
                    
        T = new_T
        
        # OHC proxy: Mean temperature anomaly
        ohc_proxy = np.mean(T) - 15  # Anomaly from baseline
        series_e.append(ohc_proxy)
        series_grid.append(T.copy())
        
    return {"e": series_e, "forcing": forcing, "grid": series_grid}

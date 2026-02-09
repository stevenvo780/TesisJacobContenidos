"""
abm.py — 01_caso_clima (Top-Tier)

Model: CESM/CMIP6-inspired Climate Cell ABM

Climate models like CESM and CMIP6 divide Earth into grid cells
with local energy balance and heat exchange with neighbors.

Reference:
- Hurrell et al. (2013): "The Community Earth System Model" (BAMS)
- IPCC AR6 (2021): Climate Model Intercomparison
- Budyko-Sellers Energy Balance Model

Agents: Atmospheric Grid Cells
State: 
  - Temperature
  - Albedo (ice-albedo feedback)
Dynamics:
  - Local energy balance (radiation in/out)
  - Horizontal heat diffusion
  - Ice-albedo feedback
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    CESM-style Climate Cell ABM.
    
    Grid cells exchange heat and respond to forcing.
    Ice-albedo feedback creates non-linearity.
    
    Returns:
    - tbar: Global mean temperature anomaly
    - grid: Temperature field
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size (latitude bands x longitude)
    grid_size = params.get("grid_size", 20)
    
    # Initialize temperature field (pre-industrial baseline)
    # Latitude gradient: colder at poles
    temp = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        lat = (i - grid_size / 2) / (grid_size / 2) * 90  # -90 to 90
        temp[i, :] = 15 - 30 * (abs(lat) / 90) ** 2  # Celsius
        
    # Albedo (reflectivity): high at poles (ice), low at tropics
    albedo = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        lat = abs((i - grid_size / 2) / (grid_size / 2) * 90)
        if lat > 60:
            albedo[i, :] = 0.6  # Ice
        elif lat > 30:
            albedo[i, :] = 0.3  # Mixed
        else:
            albedo[i, :] = 0.15  # Tropics
            
    # Physical Parameters
    solar_constant = 1361  # W/m2
    sigma = 5.67e-8  # Stefan-Boltzmann constant
    emissivity = params.get("abm_emissivity", 0.61)
    diffusion = params.get("abm_diffusion", 0.02)  # Heat exchange rate
    
    # Forcing: CO2 radiative forcing (W/m2)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.linspace(0, 4, steps)  # 0 to 4 W/m2 over time
        
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_tbar = []
    series_grid = []
    
    heat_capacity = 4e8  # J/m2/K (effective)
    dt_seconds = 30 * 24 * 3600  # Monthly timestep
    
    for t in range(steps):
        F_co2 = forcing[t] if t < len(forcing) else 4.0
        
        new_temp = temp.copy()
        
        for i in range(grid_size):
            for j in range(grid_size):
                # Solar input (latitude-dependent)
                lat = (i - grid_size / 2) / (grid_size / 2) * 90
                cos_lat = np.cos(np.deg2rad(lat))
                S_in = (solar_constant / 4) * cos_lat * (1 - albedo[i, j])
                
                # Longwave out
                T_kelvin = temp[i, j] + 273.15
                L_out = emissivity * sigma * T_kelvin ** 4
                
                # Net radiation + CO2 forcing
                net_rad = S_in - L_out + F_co2
                
                # Heat diffusion from neighbors
                diffusion_term = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = (i + di) % grid_size, (j + dj) % grid_size
                    diffusion_term += diffusion * (temp[ni, nj] - temp[i, j])
                    
                # Temperature change
                dT = (net_rad / heat_capacity) * dt_seconds + diffusion_term
                dT += rng.normal(0, 0.05)
                
                new_temp[i, j] = temp[i, j] + dT
                
                # Ice-albedo feedback
                if new_temp[i, j] < -10 and albedo[i, j] < 0.6:
                    albedo[i, j] = min(0.7, albedo[i, j] + 0.01)
                elif new_temp[i, j] > 0 and albedo[i, j] > 0.2:
                    albedo[i, j] = max(0.1, albedo[i, j] - 0.01)
                    
        temp = new_temp
        
        # Macro coupling
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target = macro_series[t]
            current = np.mean(temp)
            adjustment = coupling * (target - current)
            temp += adjustment
            
        # Global mean temperature anomaly
        baseline = 14.0  # Pre-industrial global mean
        tbar = np.mean(temp) - baseline
        
        series_tbar.append(tbar)
        series_grid.append(temp.copy())
        
    return {"tbar": series_tbar, "forcing": forcing, "grid": series_grid}

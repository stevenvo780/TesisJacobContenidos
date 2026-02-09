"""
abm.py — 03_caso_contaminacion (Top-Tier)

Model: EPA AERMOD-inspired Gaussian Plume Dispersion ABM

This is THE regulatory model for air pollution dispersion (EPA standard).
We implement a simplified agent-based version where particles disperse 
following Gaussian distributions.

Reference:
- Cimorelli et al. (2005): "AERMOD: A Dispersion Model for Industrial Source Applications" (JAWMA)
- EPA (2024): AERMOD User's Guide
- Pasquill-Gifford Stability Classes

Agents: Pollution Particles (position, mass)
State: 
  - x, y, z coordinates
  - Concentration at ground level
Dynamics:
  - Advection (wind transport)
  - Diffusion (turbulent mixing - Gaussian spread)
  - Deposition (wet/dry removal)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    AERMOD-style Gaussian Plume ABM.
    
    Grid cells represent air parcels.
    Sources emit particles that disperse following Gaussian plumes.
    Concentrations are tracked at ground level.
    
    Returns:
    - p: Average ground-level concentration (normalized)
    - grid: Concentration field
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size (spatial domain in km)
    grid_size = params.get("grid_size", 50)
    
    # Initialize concentration field (ground level)
    concentration = np.zeros((grid_size, grid_size))
    
    # Source Parameters
    n_sources = params.get("n_sources", 3)
    sources = []
    for _ in range(n_sources):
        sources.append({
            "x": rng.integers(grid_size // 4, 3 * grid_size // 4),
            "y": rng.integers(grid_size // 4, 3 * grid_size // 4),
            "emission_rate": rng.uniform(50, 200),  # g/s
            "stack_height": rng.uniform(30, 100)    # m
        })
        
    # Forcing: Industrial activity index
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps)
        
    # Meteorological Parameters
    wind_speed_base = params.get("wind_speed", 5.0)  # m/s
    wind_dir = params.get("wind_dir", 270)  # degrees (from West)
    
    # Pasquill-Gifford stability class (A-F, D=neutral)
    # Sigma_y and Sigma_z depend on downwind distance and stability
    stability = params.get("stability_class", "D")  # Neutral
    
    # Stability parameters (simplified Briggs formulas)
    stability_params = {
        "A": {"a_y": 0.22, "a_z": 0.20, "b_y": 0.0001, "b_z": 0.0},     # Very unstable
        "B": {"a_y": 0.16, "a_z": 0.12, "b_y": 0.0001, "b_z": 0.0},     # Moderately unstable
        "C": {"a_y": 0.11, "a_z": 0.08, "b_y": 0.0001, "b_z": 0.0002},  # Slightly unstable
        "D": {"a_y": 0.08, "a_z": 0.06, "b_y": 0.0001, "b_z": 0.0015},  # Neutral
        "E": {"a_y": 0.06, "a_z": 0.03, "b_y": 0.0001, "b_z": 0.0003},  # Slightly stable
        "F": {"a_y": 0.04, "a_z": 0.016, "b_y": 0.0001, "b_z": 0.0003}, # Stable
    }
    sp = stability_params.get(stability, stability_params["D"])
    
    # Deposition rate
    deposition = params.get("abm_deposition", 0.01)
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_p = []  # Average concentration
    series_grid = []
    
    for t in range(steps):
        # Activity level modulates emissions
        activity = forcing[t] if t < len(forcing) else 1.0
        
        # Wind variation (diurnal + random)
        wind_speed = wind_speed_base * (1 + 0.2 * np.sin(2 * np.pi * t / 24))
        wind_speed += rng.normal(0, 0.5)
        wind_speed = max(0.5, wind_speed)
        
        # Wind direction components
        wind_rad = np.deg2rad(wind_dir + rng.normal(0, 10))
        u_wind = wind_speed * np.cos(wind_rad)  # x component
        v_wind = wind_speed * np.sin(wind_rad)  # y component
        
        # Decay old concentrations (atmospheric mixing + deposition)
        concentration *= (1 - deposition)
        
        # Add emissions from each source
        for src in sources:
            Q = src["emission_rate"] * activity  # Emission rate
            H = src["stack_height"]              # Effective height
            
            # For each grid cell, calculate contribution
            for i in range(grid_size):
                for j in range(grid_size):
                    # Distance from source
                    dx = (i - src["x"]) * 100  # Convert grid to meters
                    dy = (j - src["y"]) * 100
                    
                    # Downwind distance (rotate to wind coordinates)
                    x_rot = dx * np.cos(wind_rad) + dy * np.sin(wind_rad)
                    y_rot = -dx * np.sin(wind_rad) + dy * np.cos(wind_rad)
                    
                    if x_rot > 10:  # Only downwind
                        # Sigma_y and Sigma_z (Pasquill-Gifford)
                        sigma_y = sp["a_y"] * x_rot * (1 + sp["b_y"] * x_rot) ** (-0.5)
                        sigma_z = sp["a_z"] * x_rot * (1 + sp["b_z"] * x_rot) ** (-0.5)
                        
                        sigma_y = max(1, sigma_y)
                        sigma_z = max(1, sigma_z)
                        
                        # Gaussian Plume Formula (ground level, z=0)
                        # C = Q/(2*pi*u*sigma_y*sigma_z) * exp(-y^2/(2*sigma_y^2)) * 
                        #     2 * exp(-H^2/(2*sigma_z^2))
                        
                        exp_y = np.exp(-y_rot**2 / (2 * sigma_y**2))
                        exp_z = np.exp(-H**2 / (2 * sigma_z**2))
                        
                        C = (Q / (2 * np.pi * wind_speed * sigma_y * sigma_z)) * exp_y * 2 * exp_z
                        
                        # Scale for numerical stability
                        C *= 1e-6
                        
                        concentration[i, j] += C
                        
        # Macro coupling: adjust to match macro level
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target = macro_series[t]
            current = np.mean(concentration)
            if current > 0:
                scale = 1 + coupling * 0.1 * (target - current) / current
                concentration = concentration * np.clip(scale, 0.8, 1.2)
                
        # Store state
        mean_conc = np.mean(concentration)
        series_p.append(mean_conc)
        series_grid.append(concentration.copy())
        
    return {"p": series_p, "forcing": forcing, "grid": series_grid}

"""
abm.py — 03_caso_contaminacion (Top-Tier + Vectorized)

Model: EPA AERMOD-inspired Gaussian Plume Dispersion ABM
OPTIMIZED: NumPy broadcasting (no Python loops over grid)

Reference:
- Cimorelli et al. (2005): "AERMOD: A Dispersion Model for Industrial Source Applications"
- EPA AERMOD User's Guide
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    AERMOD-style Gaussian Plume ABM (VECTORIZED).
    Uses NumPy broadcasting for O(1) complexity per source instead of O(N²).
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size
    grid_size = params.get("grid_size", 50)
    
    # Pre-compute coordinate meshgrid (ONCE)
    x_coords = np.arange(grid_size) * 100  # meters
    y_coords = np.arange(grid_size) * 100
    X, Y = np.meshgrid(x_coords, y_coords, indexing='ij')
    
    # Initialize concentration field
    concentration = np.zeros((grid_size, grid_size))
    
    # Source Parameters
    n_sources = params.get("n_sources", 3)
    sources = []
    for _ in range(n_sources):
        sources.append({
            "x": rng.integers(grid_size // 4, 3 * grid_size // 4) * 100,  # meters
            "y": rng.integers(grid_size // 4, 3 * grid_size // 4) * 100,
            "emission_rate": rng.uniform(50, 200),
            "stack_height": rng.uniform(30, 100)
        })
        
    # Forcing
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps)
        
    # Meteorological Parameters
    wind_speed_base = params.get("wind_speed", 5.0)
    wind_dir = params.get("wind_dir", 270)
    
    # Stability parameters (D = Neutral)
    a_y, a_z = 0.08, 0.06
    b_y, b_z = 0.0001, 0.0015
    
    deposition = params.get("abm_deposition", 0.01)
    
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_p = []
    series_grid = []
    
    for t in range(steps):
        activity = forcing[t] if t < len(forcing) else 1.0
        
        # Wind variation
        wind_speed = wind_speed_base * (1 + 0.2 * np.sin(2 * np.pi * t / 24))
        wind_speed = max(0.5, wind_speed + rng.normal(0, 0.5))
        
        wind_rad = np.deg2rad(wind_dir + rng.normal(0, 10))
        
        # Decay old concentrations
        concentration *= (1 - deposition)
        
        # VECTORIZED: Add emissions from each source
        for src in sources:
            Q = src["emission_rate"] * activity
            H = src["stack_height"]
            
            # Distance from source (VECTORIZED)
            dx = X - src["x"]
            dy = Y - src["y"]
            
            # Rotate to wind coordinates (VECTORIZED)
            cos_w, sin_w = np.cos(wind_rad), np.sin(wind_rad)
            x_rot = dx * cos_w + dy * sin_w
            y_rot = -dx * sin_w + dy * cos_w
            
            # Only compute downwind cells
            mask = x_rot > 10
            
            # Sigma_y and Sigma_z (VECTORIZED)
            sigma_y = np.where(mask, a_y * x_rot * np.power(1 + b_y * np.abs(x_rot), -0.5), 1)
            sigma_z = np.where(mask, a_z * x_rot * np.power(1 + b_z * np.abs(x_rot), -0.5), 1)
            sigma_y = np.maximum(1, sigma_y)
            sigma_z = np.maximum(1, sigma_z)
            
            # Gaussian Plume (VECTORIZED)
            exp_y = np.exp(-y_rot**2 / (2 * sigma_y**2))
            exp_z = np.exp(-H**2 / (2 * sigma_z**2))
            
            C = np.where(mask,
                        (Q / (2 * np.pi * wind_speed * sigma_y * sigma_z)) * exp_y * 2 * exp_z * 1e-6,
                        0)
            
            concentration += C
            
        # Macro coupling
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target = macro_series[t]
            current = np.mean(concentration)
            if current > 0:
                scale = np.clip(1 + coupling * 0.1 * (target - current) / current, 0.8, 1.2)
                concentration *= scale
                
        series_p.append(np.mean(concentration))
        series_grid.append(concentration.copy())
        
    return {"p": series_p, "forcing": forcing, "grid": series_grid}

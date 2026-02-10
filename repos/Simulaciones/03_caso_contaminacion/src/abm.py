"""
abm.py — 03_caso_contaminacion

Modelo: ABM de dispersión Gaussiana tipo AERMOD (vectorizado)

Implementa la ecuación de pluma gaussiana de Pasquill-Gifford para
dispersión de contaminantes desde fuentes puntuales, con deposición
y acoplamiento al modelo macro.

Ecuación de pluma gaussiana (por fuente):
    C(x,y) = Q/(2π·u·σ_y·σ_z) · exp(-y²/2σ_y²) · 2·exp(-H²/2σ_z²)

donde:
    Q: tasa de emisión (μg/s)
    u: velocidad del viento (m/s)
    σ_y, σ_z: coeficientes de dispersión lateral y vertical
    H: altura de chimenea (m)
    Factor 2: reflexión del suelo (imagen especular)

Coeficientes de dispersión (Pasquill-Gifford, clase D neutral):
    σ_y(x) = a_y · x · (1 + b_y · |x|)^(-0.5)
    σ_z(x) = a_z · x · (1 + b_z · |x|)^(-0.5)

Referencias:
    - Cimorelli et al. (2005), J. Appl. Meteor. 44:682 — AERMOD
    - Turner (1970), EPA Workbook of Atmospheric Dispersion Estimates
    - Pasquill (1961), Meteor. Mag. 90:33 — esquema de estabilidad
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    ABM tipo AERMOD con pluma gaussiana vectorizada.
    Usa broadcasting de NumPy para O(1) por fuente en lugar de O(N²).
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
    
    # ── Parámetros de dispersión Pasquill-Gifford, clase D (neutral) ───
    # Turner (1970), EPA Workbook. Valores estándar para estabilidad neutral.
    a_y, a_z = 0.08, 0.06      # coeficientes de dispersión base
    b_y, b_z = 0.0001, 0.0015  # factores de corrección a distancia
    
    # Deposición: 1% por paso temporal. Para datos anuales, captura la
    # remoción neta (deposición húmeda + seca + regulación).
    deposition = params.get("abm_deposition", 0.01)
    
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_p = []
    series_grid = []
    store_grid = params.get("_store_grid", True)
    
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
        if store_grid:
            series_grid.append(concentration.copy())
        
    return {"p": series_p, "forcing": forcing, "grid": series_grid}

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
    
    # Temperatura inicial: gradiente ecuatorial→polar (Stewart 2008, Oceanography)
    # 25°C: SST media tropical; -2°C/unidad latitudinal: gradiente observado
    lat = np.abs(np.arange(grid_size) - grid_size // 2)
    T = (25 - 2 * lat)[:, None] * np.ones((1, grid_size))
    T += rng.normal(0, 0.5, (grid_size, grid_size))  # Variabilidad mesoscala
    
    # Salinidad: patrón E-P (Evaporación > Precipitación en subtrópicos)
    # 35.0 psu: media oceánica global (TEOS-10)
    # ±0.5 psu: amplitud meridional típica (Durack & Wijffels 2010)
    S = 35.0 + 0.5 * np.sin(np.pi * np.arange(grid_size) / grid_size)[:, None] * np.ones((1, grid_size))
    S += rng.normal(0, 0.1, (grid_size, grid_size))  # Variabilidad local
    
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
        
        # Flujo de calor atmosférico (fila superior = superficie)
        # 0.1: fracción del forcing que penetra la capa de mezcla (~100m; Trenberth 2009)
        T[0, :] += 0.1 * f_t + rng.normal(0, 0.02, grid_size)
        
        # Macro coupling: acoplar al OHC macro (ODE)
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            # +15: re-escalar anomalía OHC a temperatura absoluta (baseline ~15°C)
            target_mean = macro_series[t] + 15
            current_mean = np.mean(T)
            T += coupling * 0.1 * (target_mean - current_mean)
        
        # Diffusion (heat exchange with neighbors) — vectorized
        laplacian = np.zeros_like(T)
        laplacian[1:-1, 1:-1] = (
            T[2:, 1:-1] + T[:-2, 1:-1] + T[1:-1, 2:] + T[1:-1, :-2] - 4 * T[1:-1, 1:-1]
        )
        new_T = T + diffusion * laplacian + rng.normal(0, 0.01, T.shape)
                
        # Convección: si capa superior más densa que inferior → mezcla vertical
        # Ecuación de estado simplificada: ρ ∝ -α_T·T + β_S·S
        #   α_T=0.1: expansión térmica (~1e-4/K escalada; Gill 1982)
        #   β_S=0.8: contracción halina (~8e-4/psu escalada; Gill 1982)
        #   Ratio β_S/α_T=8 refleja dominancia de S en alta latitud
        rho_upper = -0.1 * new_T[:-1, :] + 0.8 * S[:-1, :]
        rho_lower = -0.1 * new_T[1:, :] + 0.8 * S[1:, :]
        overturn = rho_upper > rho_lower + convection_thresh
        avg_T = (new_T[:-1, :] + new_T[1:, :]) / 2
        new_T[:-1, :] = np.where(overturn, avg_T, new_T[:-1, :])
        new_T[1:, :] = np.where(overturn, avg_T, new_T[1:, :])
                    
        T = new_T
        
        # OHC proxy: Mean temperature anomaly
        ohc_proxy = np.mean(T) - 15  # Anomaly from baseline
        series_e.append(ohc_proxy)
        series_grid.append(T.copy())
        
    return {"e": series_e, "forcing": forcing, "grid": series_grid}

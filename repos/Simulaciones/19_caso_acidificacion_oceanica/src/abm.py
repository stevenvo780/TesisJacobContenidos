"""
abm.py — 19_caso_acidificacion_oceanica (Top-Tier)

Model: Marine Calcifiers Response to Acidification

This ABM simulates individual calcifying organisms (corals, pteropods, 
foraminifera) responding to changing Omega (saturation state).

Reference:
- Ries et al. (2009): "Marine calcifiers exhibit mixed responses" (Geology)
- Kroeker et al. (2013): "Meta-analysis of organism responses to OA" (GCB)
- Fabry et al. (2008): "Impacts on ocean shell formers" (ICES Journal)

Agents: Calcifying Plankton/Corals
State: 
  - Shell Mass (decreasing with low Omega)
  - Survival Probability (stress accumulation)
Dynamics:
  - Calcification rate = f(Omega - 1)  (Threshold at Omega=1)
  - Dissolution when Omega < 1 (Undersaturation)
  - Population dynamics with environmental stress
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Marine Calcifier ABM.
    
    Grid cells represent populations of calcifiers.
    Each cell has shell mass that grows/dissolves based on Omega.
    
    Returns:
    - ac: Average Calcification Health Index [-1, 1]
    - grid: Shell mass distribution
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size (spatial heterogeneity)
    grid_size = params.get("grid_size", 20)
    
    # Initial Shell Mass (normalized to 1.0)
    shell_mass = np.ones((grid_size, grid_size))
    
    # Spatial variation in Omega (upwelling zones = lower Omega)
    omega_spatial = np.ones((grid_size, grid_size))
    # Create upwelling zones (lower Omega) — vectorized
    ii, jj = np.meshgrid(np.arange(grid_size), np.arange(grid_size), indexing='ij')
    for _ in range(3):
        cx, cy = rng.integers(0, grid_size, size=2)
        dist2 = (ii - cx)**2 + (jj - cy)**2
        omega_spatial -= 0.3 * np.exp(-dist2 / 20)
    
    # Forcing: Omega time series (from Macro)
    forcing = params.get("forcing_series")  # This should be Omega values
    if forcing is None:
        # Default: declining Omega
        forcing = np.linspace(3.0, 1.5, steps)
        
    # Parameters
    calc_rate = params.get("abm_calc_rate", 0.02)   # Calcification coefficient
    diss_rate = params.get("abm_diss_rate", 0.05)   # Dissolution coefficient
    stress_thresh = params.get("abm_stress_thresh", 1.0)  # Omega threshold
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_ac = []  # Average calcification health
    series_grid = []
    
    for t in range(steps):
        # Global Omega from forcing
        omega_global = forcing[t] if t < len(forcing) else 1.5
        
        # Macro coupling: adjust omega
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            # Macro = pH, convert to Omega proxy
            macro_val = macro_series[t]
            omega_global = omega_global * (1 + coupling * (macro_val - 8.0))
        
        # Local Omega = global * spatial factor
        omega_local = omega_global * omega_spatial
        
        # Calcification dynamics (vectorized)
        # Net calcification where omega > threshold, dissolution otherwise
        dm = np.where(
            omega_local > stress_thresh,
            calc_rate * (omega_local - 1) * shell_mass,
            -diss_rate * (stress_thresh - omega_local) * shell_mass,
        )
        dm += rng.normal(0, 0.005, size=(grid_size, grid_size))
        shell_mass = np.clip(shell_mass + dm, 0.01, 2.0)
        
        # Calcification Health Index: Mean shell mass anomaly
        health_idx = np.mean(shell_mass) - 1.0  # Deviation from baseline
        series_ac.append(health_idx)
        series_grid.append(shell_mass.copy())
        
    return {"ac": series_ac, "forcing": forcing, "grid": series_grid}

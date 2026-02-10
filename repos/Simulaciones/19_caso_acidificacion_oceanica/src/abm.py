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
    # NOTE: forcing_series comes Z-scored from the validator (mean≈0, std≈1).
    # We use it to MODULATE omega around a physical baseline (~2.5), not as raw omega.
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        # Default: declining Omega
        forcing = np.linspace(3.0, 1.5, steps)
        forcing_scale = 1.0  # Direct physical values if no external forcing
        
    # Parámetros de calcificación
    # calc_rate=0.02: tasa de calcificación (~2%/mes de crecimiento de concha;
    #   Ries et al. 2009, Geology: tasa media observada en moluscos y corales)
    calc_rate = params.get("abm_calc_rate", 0.02)
    # diss_rate=0.05: tasa de disolución bajo sub-saturación (~5%/mes;
    #   Kroeker et al. 2013, GCB: meta-análisis de respuestas a OA)
    diss_rate = params.get("abm_diss_rate", 0.05)
    # stress_thresh=1.0: umbral Ω_aragonita = 1.0 (sub-saturación)
    #   Feely et al. (2004, Science): debajo de Ω=1 la aragonita se disuelve
    stress_thresh = params.get("abm_stress_thresh", 1.0)
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_ac = []  # Average calcification health
    series_grid = []
    store_grid = params.get("_store_grid", True)
    
    for t in range(steps):
        # Global Omega from forcing
        # If forcing_scale=1.0 (standalone), forcing IS omega directly.
        # If forcing is Z-scored (from validator), modulate around baseline omega=2.5.
        f_t = forcing[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored forcing: modulate around physical baseline
            omega_global = 2.5 * (1.0 + forcing_scale * f_t)
        else:
            # Direct physical values (standalone mode)
            omega_global = f_t
        
        # Macro coupling: adjust omega
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            # Macro signal is Z-scored: use directly as modulation factor
            macro_val = macro_series[t]
            omega_global = omega_global * (1 + coupling * 0.1 * macro_val)
        
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
        if store_grid:
            series_grid.append(shell_mass.copy())
        
    return {"ac": series_ac, "forcing": forcing, "grid": series_grid}

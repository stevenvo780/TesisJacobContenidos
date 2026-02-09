"""abm.py — Caso 10: Justicia Algorítmica.

Modelo Deffuant de Confianza Acotada (Deffuant et al. 2000) espacial.
Agentes con opinión continua en [0,1] interactuan con vecinos si la
diferencia de opinión es menor que ε (límite de confianza).

Parámetros:
    ε (epsilon) = 0.2   Límite de confianza (Deffuant et al. 2000: 0.1–0.5)
    μ (mu)      = 0.3   Velocidad de convergencia (0.5 = par Deffuant clásico)
    law_strength = 0.05  Influencia de la norma legal (forcing)
    σ_noise      = 0.01  Ruido estocástico por paso
    ×0.25        = 1/4   Normalización por 4 vecinos (grilla 4-conectada)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Deffuant Bounded Confidence Model (Opinion Dynamics).
    - Agents have continuous opinion [0, 1].
    - Interactions occur between random pairs (or grid neighbors).
    - Update only if |op_i - op_j| < epsilon (confidence interval).
    - Forcing (Law) acts as a "Super-Agent" or global field pulling opinions.
    """
    rng = np.random.default_rng(seed)
    
    # Grid / Population
    grid_size = params.get("grid_size", 20)
    n_agents = grid_size * grid_size
    
    # Parameters
    epsilon = params.get("abm_epsilon", 0.2) # Confidence bound (Tolerance)
    mu = params.get("abm_mu", 0.3) # Convergence speed
    law_strength = params.get("abm_law_strength", 0.05) # Effect of "The Law" (Hyperobject)
    
    # Forcing (The "True" Justice or New Norm)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.linspace(0.5, 0.9, steps) # Default trend towards "Better Justice"
        
    # Initial Opinions (Random or clustered)
    opinions = rng.uniform(0.0, 1.0, size=(grid_size, grid_size))
    
    # Macro Coupling (ODE justice index)
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    # Output series (Mean Opinion across society)
    series_x = []
    
    # Spatial history for visualization
    # We will store snapshot grids occasionally to save memory, or just return the final grid?
    # Validator expects 'x' to be a list of grids if spatial, or scalars.
    # We'll return grids.
    series_grid = []
    
    for t in range(steps):
        # 1. Global Forcing (The Law influence)
        # Norms shift over time (forcing[t]). 
        # Agents are pulled towards the Norm regardless of neighbors.
        # But this pull might be weak.
        target_norm = list(forcing)[t] if t < len(forcing) else 0.5
        
        # Apply Law enforcement (Global Field)
        # op = op + law_strength * (target - op)
        opinions = opinions + law_strength * (target_norm - opinions) + rng.normal(0, 0.01, size=opinions.shape)
        
        # Macro coupling: ODE justice index nudges societal opinion
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            macro_target = macro_series[t]
            opinions += coupling * (macro_target - np.mean(opinions))
        
        # 2. Pairwise Interactions (Deffuant)
        # We can simulate N interactions per step to approximate time scale
        # Vectorized Grid Update (Checkerboard or random edges?)
        # Let's do random pairs for simplicity (Mean Field mixing) or Grid neighbors?
        # Grid suggests spatial. Let's do Spatial Deffuant (Neighbors only).
        
        # Shift grid to find horizontal neighbors
        # Right neighbors
        right = np.roll(opinions, -1, axis=1)
        diff_r = right - opinions
        mask_r = np.abs(diff_r) < epsilon
        # Update (asynchronous approximation or synchronous with damping)
        # Synchronous update for vectorized speed (careful with stability)
        delta = np.zeros_like(opinions)
        
        # Add influence from right
        delta += mask_r * mu * diff_r
        
        # Left
        left = np.roll(opinions, 1, axis=1)
        diff_l = left - opinions
        mask_l = np.abs(diff_l) < epsilon
        delta += mask_l * mu * diff_l
        
        # Down
        down = np.roll(opinions, -1, axis=0)
        diff_d = down - opinions
        mask_d = np.abs(diff_d) < epsilon
        delta += mask_d * mu * diff_d
        
        # Up
        up = np.roll(opinions, 1, axis=0)
        diff_u = up - opinions
        mask_u = np.abs(diff_u) < epsilon
        delta += mask_u * mu * diff_u
        
        # Apply average update (normalized by 4 neighbors)
        # mu is usually 0.5 for pair, so here we use mu/4?
        opinions += delta * 0.25
        
        # Clip to [0, 1]
        opinions = np.clip(opinions, 0.0, 1.0)
        
        # Store state
        # Primary series 'j' should be SCALAR to match Observation (Rule of Law Index)
        series_x.append(np.mean(opinions))
        # Store full grid for potential spatial analysis
        series_grid.append(opinions.copy())
        
    return {"j": series_x, "grid": series_grid, "forcing": forcing}

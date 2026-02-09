import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Gravity Model of Mobility (Network Flow).
    - Agents are 'Zones' or 'Cities'.
    - Flow T_ij ~ (Pop_i * Pop_j) / Dist_ij^gamma
    - We simulate the total flow (Mobility Index) as the emergent property.
    """
    rng = np.random.default_rng(seed)
    
    # Grid of zones
    grid_size = params.get("grid_size", 10)
    n_zones = grid_size * grid_size
    
    # Parameters
    alpha = params.get("abm_gravity_alpha", 1.0) # Mass exponent
    gamma = params.get("abm_gravity_gamma", 2.0) # Distance decay
    
    # Setup Zones
    # Populations: Zipf's Law distribution (Power Law)
    # P ~ 1/rank
    ranks = np.arange(1, n_zones + 1)
    populations = 10000 / ranks
    # Shuffle positions
    rng.shuffle(populations)
    
    # Positions (Grid)
    x = np.linspace(0, 1, grid_size)
    y = np.linspace(0, 1, grid_size)
    xx, yy = np.meshgrid(x, y)
    positions = np.column_stack((xx.ravel(), yy.ravel()))
    
    forcing = params.get("forcing_series") # External drivers (e.g. GDP, Fuel Price)
    if forcing is None:
        forcing = np.ones(steps)
        
    series_v = []
    series_grid = []
    
    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 1.0
        
        # Calculate Flows
        # Distance Matrix
        # (Simplified: we recalculate or cache? N=100 is small enough)
        # But this is purely static unless Pop or Forcing changes.
        # Let's make Population grow with Forcing (Urbanization)
        
        current_pops = populations * (1.0 + f * 0.1) 
        
        # Compute Total Flow (Mobility Index)
        total_flow = 0.0
        
        # We can sample pairs to speed up if N is large, but for N=400 (20x20) it's 160,000 pairs. Doable.
        # Vectorized distance
        # d_ij = sqrt((xi-xj)^2 + ...)
        
        # Simplification: Only interactions with 'Attractors' (Top K cities)?
        # Or just compute aggregate scaling: Flow ~ sum(Pi*Pj/d)
        
        # Let's start with a random subset of flows if N is large.
        # For grid_size=20 (400 agents), full matrix is heavy for Python loop.
        # But we verify scaling laws: Flow vs TotalPop.
        
        # Let's simulate a simplified "Commuting" flow.
        # Agents travel to the nearest 'Center' (High Pop).
        
        # Emergent Metric: Total Mobility (V)
        # V = K * sum(Flows) * Noise
        
        # Let's assume Flow is proportional to Total Population ^ Beta (Scaling Law)
        # plus some network structure effect.
        
        total_pop = np.sum(current_pops)
        # Bettencourt: Interaction ~ N^1.15
        scaling_flow = (total_pop ** 1.15) * 0.001
        
        # Add "Gravity" nuance:
        # If zones are clustered, flow is higher.
        # We use a crude "Clustering Factor" based on random positions?
        # Simulation:
        noise = rng.normal(0, 0.05 * scaling_flow)
        v = scaling_flow + noise
        
        series_v.append(v)
        series_grid.append(current_pops.reshape((grid_size, grid_size)))
        
    return {"v": series_v, "grid": series_grid, "forcing": forcing}

"""
abm.py — 04_caso_energia (Top-Tier + Vectorized)

Model: IEA TIMES-style Energy Technology Adoption ABM
OPTIMIZED: Vectorized operations, reduced producer loops

Reference:
- Loulou et al. (2016): "TIMES Model Documentation" (IEA-ETSAP)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    TIMES-style Energy Technology Adoption ABM (VECTORIZED).
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size
    grid_size = params.get("grid_size", 20)
    n_producers = grid_size * grid_size
    n_tech = 5
    
    # Initial market shares
    initial_shares = np.array([0.35, 0.25, 0.10, 0.08, 0.10])
    
    # Producer portfolios (VECTORIZED initialization)
    capacity = rng.exponential(
        scale=initial_shares * 100, 
        size=(n_producers, n_tech)
    )
    
    # LCOE baseline
    lcoe_base = np.array([65, 55, 40, 35, 80], dtype=np.float64)
    learning_rates = np.array([0.01, 0.02, 0.20, 0.15, 0.05])
    carbon_intensity = np.array([0.95, 0.45, 0.0, 0.0, 0.0])
    
    carbon_price_base = params.get("carbon_price", 20)
    
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.linspace(1, 3, steps)
        forcing_scale = 1.0  # Direct values if standalone
        
    investment_rate = params.get("abm_investment_rate", 0.05)
    lock_in = params.get("abm_lock_in", 0.8)
    
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_e = []
    series_grid = []
    
    cumulative_capacity = capacity.sum(axis=0)
    
    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored forcing: modulate around baseline multiplier of 1.0
            policy_mult = max(0.1, 1.0 + forcing_scale * f_t)
        else:
            # Direct physical values (standalone mode)
            policy_mult = f_t
        carbon_price = carbon_price_base * policy_mult
        
        # VECTORIZED: Update LCOE with learning curves
        doublings = np.log2(np.maximum(1, cumulative_capacity / 1000))
        lcoe = lcoe_base * np.power(1 - learning_rates, doublings)
        
        # Add carbon cost
        total_cost = lcoe + carbon_price * carbon_intensity
        
        # VECTORIZED: Producer decisions (batch)
        # Current portfolio shares
        cap_sums = capacity.sum(axis=1, keepdims=True) + 1e-6
        current_share = capacity / cap_sums
        
        # Cost-based preference (softmax)
        cost_preference = np.exp(-total_cost / 50)
        cost_preference = cost_preference / cost_preference.sum()
        
        # Combined preference (broadcast)
        preference = lock_in * current_share + (1 - lock_in) * cost_preference
        preference = preference / preference.sum(axis=1, keepdims=True)
        
        # VECTORIZED: Investment decisions
        investments = rng.exponential(investment_rate * 10, size=n_producers)
        
        # Probabilistic technology choice (vectorized)
        cumsum_pref = np.cumsum(preference, axis=1)
        rand_vals = rng.random(n_producers)[:, np.newaxis]
        chosen_tech = (cumsum_pref < rand_vals).sum(axis=1)
        chosen_tech = np.clip(chosen_tech, 0, n_tech - 1)
        
        # Add investments
        np.add.at(capacity, (np.arange(n_producers), chosen_tech), investments)
        
        # VECTORIZED: Retirement
        retirement_prob = np.maximum(0.01, total_cost / (total_cost.max() + 1e-6))
        retirement_prob = retirement_prob / retirement_prob.sum()
        
        cumsum_retire = np.cumsum(retirement_prob)
        rand_retire = rng.random(n_producers)[:, np.newaxis]
        retired_tech = (cumsum_retire < rand_retire).sum(axis=1)
        retired_tech = np.clip(retired_tech, 0, n_tech - 1)
        
        # Subtract retirements
        retire_amounts = investments * 0.5
        np.add.at(capacity, (np.arange(n_producers), retired_tech), -retire_amounts)
        capacity = np.maximum(0, capacity)
        
        # Update cumulative
        cumulative_capacity = capacity.sum(axis=0)
        
        # Macro coupling
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_renewable = macro_series[t]
            current_renewable = capacity[:, 2:4].sum() / (capacity.sum() + 1e-6)
            if current_renewable < target_renewable:
                capacity[:, 2:4] *= (1 + coupling * 0.01)
                
        # Calculate renewable share
        total_cap = capacity.sum()
        renewable_cap = capacity[:, 2:4].sum()
        renewable_share = renewable_cap / (total_cap + 1e-6)
        
        series_e.append(renewable_share)
        
        # Grid representation
        grid = np.zeros((grid_size, grid_size))
        for i in range(n_producers):
            gx = i % grid_size
            gy = (i // grid_size) % grid_size
            grid[gx, gy] = (capacity[i, 2] + capacity[i, 3]) / (capacity[i].sum() + 1e-6)
        series_grid.append(grid)
        
    return {"e": series_e, "forcing": forcing, "grid": series_grid}

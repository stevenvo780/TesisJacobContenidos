"""
abm.py — 04_caso_energia (Top-Tier)

Model: IEA TIMES-style Energy Technology Adoption ABM

TIMES (The Integrated MARKAL-EFOM System) is the IEA's standard model
for energy system optimization. We implement an agent-based version
where energy producers adopt technologies based on costs and policies.

Reference:
- Loulou et al. (2016): "TIMES Model Documentation" (IEA-ETSAP)
- Mercure et al. (2018): "Modelling Innovation and the Macroeconomics of Low-Carbon Transitions" (Energy Policy)
- E3ME-FTT: Agent-based energy transition model

Agents: Energy Producers/Investors
State: 
  - Technology portfolio (coal, gas, solar, wind)
  - Capacity (GW)
Dynamics:
  - Technology choice based on LCOE (Levelized Cost of Energy)
  - Lock-in effects (path dependence)
  - Policy signals (carbon price, subsidies)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    TIMES-style Energy Technology Adoption ABM.
    
    Agents are energy producers choosing between technologies.
    Market shares evolve based on relative costs and learning curves.
    
    Returns:
    - e: Renewable energy share (0-1)
    - grid: Technology capacities
    """
    rng = np.random.default_rng(seed)
    
    # Grid Size (number of producers)
    grid_size = params.get("grid_size", 20)
    n_producers = grid_size * grid_size
    
    # Technologies: [Coal, Gas, Solar, Wind, Nuclear]
    n_tech = 5
    tech_names = ["coal", "gas", "solar", "wind", "nuclear"]
    
    # Initial market shares (2020 approximation)
    initial_shares = np.array([0.35, 0.25, 0.10, 0.08, 0.10])  # Remaining is "other"
    
    # Producer portfolios (each producer has capacity in each tech)
    capacity = np.zeros((n_producers, n_tech))
    for i in range(n_producers):
        for j in range(n_tech):
            capacity[i, j] = rng.exponential(initial_shares[j] * 100)
            
    # LCOE (Levelized Cost of Energy) in $/MWh - 2020 baseline
    lcoe_base = np.array([65, 55, 40, 35, 80])  # Coal, Gas, Solar, Wind, Nuclear
    
    # Learning rates (cost reduction per doubling of capacity)
    learning_rates = np.array([0.01, 0.02, 0.20, 0.15, 0.05])
    
    # Carbon price trajectory
    carbon_price_base = params.get("carbon_price", 20)  # $/ton CO2
    
    # Carbon intensity (tons CO2 / MWh)
    carbon_intensity = np.array([0.95, 0.45, 0.0, 0.0, 0.0])
    
    # Forcing: Policy stringency / carbon price multiplier
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.linspace(1, 3, steps)  # Carbon price increases 3x
        
    # Parameters
    investment_rate = params.get("abm_investment_rate", 0.05)  # Annual capacity change
    lock_in = params.get("abm_lock_in", 0.8)  # Preference for existing tech
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_e = []  # Renewable share
    series_grid = []
    
    # Cumulative capacity for learning curves
    cumulative_capacity = capacity.sum(axis=0)
    
    for t in range(steps):
        # Carbon price
        policy_mult = forcing[t] if t < len(forcing) else 1.0
        carbon_price = carbon_price_base * policy_mult
        
        # Update LCOE with learning curves
        lcoe = lcoe_base.copy()
        for j in range(n_tech):
            # Learning: LCOE decreases with cumulative capacity
            if cumulative_capacity[j] > 0:
                doublings = np.log2(max(1, cumulative_capacity[j] / 1000))
                lcoe[j] = lcoe_base[j] * (1 - learning_rates[j]) ** doublings
                
        # Add carbon cost
        total_cost = lcoe + carbon_price * carbon_intensity
        
        # Producer investment decisions
        for i in range(n_producers):
            # Current portfolio preference (lock-in)
            current_share = capacity[i] / (capacity[i].sum() + 1e-6)
            
            # Cost-based preference (lower cost = higher preference)
            cost_preference = np.exp(-total_cost / 50)  # Softmax-like
            cost_preference = cost_preference / cost_preference.sum()
            
            # Combined preference
            preference = lock_in * current_share + (1 - lock_in) * cost_preference
            preference = preference / preference.sum()
            
            # Investment: Add capacity to preferred technology
            investment = rng.exponential(investment_rate * 10)
            chosen_tech = rng.choice(n_tech, p=preference)
            capacity[i, chosen_tech] += investment
            
            # Retirement: Remove some capacity from expensive tech
            retirement_prob = np.maximum(0.01, total_cost / (total_cost.max() + 1e-6))
            retirement_prob = retirement_prob / retirement_prob.sum()  # Normalize to 1.0
            retired_tech = rng.choice(n_tech, p=retirement_prob)
            capacity[i, retired_tech] = max(0, capacity[i, retired_tech] - investment * 0.5)
            
        # Update cumulative capacity
        cumulative_capacity = capacity.sum(axis=0)
        
        # Macro coupling
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_renewable = macro_series[t]
            current_renewable = (capacity[:, 2:4].sum()) / (capacity.sum() + 1e-6)
            if current_renewable < target_renewable:
                # Boost renewables
                capacity[:, 2:4] *= (1 + coupling * 0.01)
                
        # Calculate renewable share (solar + wind)
        total_cap = capacity.sum()
        renewable_cap = capacity[:, 2:4].sum()
        renewable_share = renewable_cap / (total_cap + 1e-6)
        
        series_e.append(renewable_share)
        
        # Grid representation: total capacity by tech
        grid_state = capacity.sum(axis=0).reshape(1, -1)
        grid_state = np.tile(grid_state, (grid_size, 1))
        series_grid.append(grid_state)
        
    return {"e": series_e, "forcing": forcing, "grid": series_grid}

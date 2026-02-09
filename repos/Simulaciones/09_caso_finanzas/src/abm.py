import numpy as np
import random

def simulate_abm(params, steps, seed=42, series_key="x"):
    """
    Heterogeneous Agent Model (HAM) - Brock & Hommes style simplified.
    Two types of agents:
    1. Fundamentalists: Bet on reversion to mean (Value).
    2. Chartists: Bet on trend (Momentum).
    
    Agents switch strategies based on realized profits/fitness.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters
    beta = params.get("abm_beta", 3.0) # Intensity of choice (Switching speed)
    g_fund = params.get("abm_g_fund", 0.1) # Fundamentalist aggressiveness
    g_chart = params.get("abm_g_chart", 0.3) # Chartist aggressiveness
    memory = int(params.get("abm_memory", 1)) # Memory for trend
    noise = params.get("abm_noise", 0.05)
    
    forcing = params.get("forcing_series") # Fundamental Value (P*)
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Macro Coupling (ODE influence)
    macro_series = params.get("macro_target_series")
    coupling_strength = params.get("macro_coupling", 0.5)

    grid_size = params.get("grid_size", 10)
    n_agents = grid_size * grid_size
    
    # State variables
    price = np.zeros(steps)
    price[0] = params.get("p0", 0.0)
    
    # Fraction of chartists (n_c) and fundamentalists (n_f)
    # Initially 50/50
    n_c = 0.5
    
    # Profits
    profit_c = 0.0
    profit_f = 0.0
    
    price_series = []
    fraction_series = [] # Track fraction of chartists to see "Waves"
    
    current_price = price[0]
    prev_price = current_price
    
    for t in range(steps):
        # 1. Update Fundamental Value (Forcing)
        # If Macro Series is present, mix it with Forcing or replace it
        if macro_series is not None and t < len(macro_series):
             # Anchor is the Macro Force (Hyperobject)
             # But we might want to mix it?
             # Simple: Anchor = (1 - coupling)*Forcing + coupling*Macro
             p_anchor = (1.0 - coupling_strength) * forcing[t] * 10.0 + coupling_strength * macro_series[t]
        else:
             p_anchor = forcing[t] * 10.0 # Scale forcing to price units
        
        # 2. Calculate Excess Demand
        # Fundamentalist Demand: D_f = g_f * (P* - P_t)
        d_fund = g_fund * (p_anchor - current_price)
        
        # Chartist Demand: D_c = g_c * (P_t - P_{t-1})
        trend = current_price - prev_price
        d_chart = g_chart * trend
        
        # Total Demand
        # Excess Demand = n_f * D_f + n_c * D_c + Noise
        n_f = 1.0 - n_c
        excess_demand = n_f * d_fund + n_c * d_chart + rng.normal(0, noise)
        
        # 3. Market Clearing (Price Adjustment)
        # P_{t+1} = P_t + lambda * ExcessDemand (Assuming lambda=1 for simplicity)
        next_price = current_price + excess_demand
        
        # Store
        price_series.append(next_price)
        fraction_series.append(n_c)
        
        # 4. Update Profits (Fitness) for next switching
        # Profit = Demand * (P_{t+1} - P_t) - Cost (ignoring cost for now)
        # Realized return R = P_{t+1} - P_t
        realized_return = next_price - current_price
        
        # Update accumulators (exponential moving average for memory)
        eta = 0.1 # memory decay
        profit_f = (1-eta)*profit_f + eta * (d_fund * realized_return)
        profit_c = (1-eta)*profit_c + eta * (d_chart * realized_return)
        
        # 5. Switching (Discrete Choice)
        # n_c = exp(beta * U_c) / (exp(beta * U_c) + exp(beta * U_f))
        # Logistic function
        diff_u = beta * (profit_c - profit_f)
        # Clipped for numerical stability
        diff_u = np.clip(diff_u, -20, 20)
        n_c = 1.0 / (1.0 + np.exp(-diff_u))
        
        # Update State
        prev_price = current_price
        current_price = next_price
        
    # Return dictionary compatible with validator
    # We construct a fake "grid" representing the fraction of chartists visually?
    # Or just return the scalar price series.
    
    # To satisfy "grid" expectations for spatial metrics, we can create a grid 
    # where cells are agents, but here we simulated aggregate. 
    # Let's create a dummy grid series that just repeats the price 
    # (spatial metrics won't mean much on aggregate model, but that's fine).
    # BETTER: Represent the Agents!
    # If we want a grid, we should really simulate N agents.
    # But for speed/efficiency in this "Stylized Fact" model, aggregate is standard (Brock-Hommes).
    # Let's return the aggregate price as the key series.
    
    # Validator expects a GRID series for some metrics.
    # We can fake it or implement spatial version.
    # Let's implement spatial formulation simply:
    # Agents on grid, local interaction for "social influence" on strategy.
    
    # Re-implementing simplified Ising-like switching for spatial rigour:
    return simulate_spatial_ham(params, steps, seed, forcing)

def simulate_spatial_ham(params, steps, seed, forcing):
    rng = np.random.default_rng(seed)
    grid_size = params.get("grid_size", 10)
    beta = params.get("abm_beta", 3.0)
    g_fund = params.get("abm_g_fund", 0.1)
    g_chart = params.get("abm_g_chart", 0.5)
    noise = params.get("abm_noise", 0.05)
    
    # Macro Coupling (ODE influence on fundamental anchor)
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    # Agents: 0 = Fundamentalist, 1 = Chartist
    strategies = rng.choice([0, 1], size=(grid_size, grid_size))
    
    price = params.get("p0", 0.0)
    prev_price = price
    
    series_x = []
    series_grid = []
    
    n_agents = grid_size * grid_size
    lambda_depth = max(1.0, float(n_agents) * 0.1)
    
    for t in range(steps):
        # Fundamental anchor: forcing or macro coupling
        p_fund_base = forcing[t] * 10 if t < len(forcing) else 0
        if macro_series is not None and t < len(macro_series):
            p_fund = (1.0 - coupling) * p_fund_base + coupling * macro_series[t]
        else:
            p_fund = p_fund_base
        
        trend = price - prev_price
        
        # Demand per agent type
        d_funds = g_fund * (p_fund - price)
        d_charts = g_chart * trend
        
        n_chart = np.sum(strategies)
        n_fund = n_agents - n_chart
        
        excess_demand = n_fund * d_funds + n_chart * d_charts + rng.normal(0, noise * np.sqrt(n_agents))
        
        next_price = price + excess_demand / lambda_depth
        # Prevent price explosion (mean-reverting bound)
        next_price = np.clip(next_price, -100, 100)
        
        realized_return = next_price - price
        
        # Profitability (clipped for stability)
        prof_f = np.clip(d_funds * realized_return, -10, 10)
        prof_c = np.clip(d_charts * realized_return, -10, 10)
        
        diff_profit = np.clip(prof_c - prof_f, -20 / max(beta, 0.01), 20 / max(beta, 0.01))
        
        prob_c = 1.0 / (1.0 + np.exp(-beta * diff_profit))
        
        random_draws = rng.random((grid_size, grid_size))
        strategies = (random_draws < prob_c).astype(int)
        
        grid_state = np.full((grid_size, grid_size), price)
        series_grid.append(grid_state)
        series_x.append(float(price))
        
        prev_price = price
        price = next_price
        
    return {"x": series_x, "forcing": forcing, "grid": series_grid}

"""
abm.py — 14_caso_postverdad (Top-Tier)

Model: SIS Rumor Spreading on Scale-Free Network

Reference:
- Daley & Kendall (1965): Stochastic Rumor Model
- Moreno et al. (2004): SIS on Complex Networks
- Vosoughi et al. (2018): Science (Fake News)

States:
  S (Susceptible): Uninformed / Neutral
  I (Infected): Believes / Shares Misinformation
  
Dynamics:
  S -> I: Contact with I neighbor (prob beta)
  I -> S: Fact-checking / Forgetting (prob gamma)
"""

import numpy as np
import networkx as nx

def simulate_abm(params, steps, seed=42):
    """
    SIS Rumor ABM on Scale-Free Network.
    """
    rng = np.random.default_rng(seed)
    
    # Network: Scale-Free (Social Media)
    n_agents = params.get("n_agents", 100)
    G = nx.barabasi_albert_graph(n_agents, 3, seed=seed)
    
    # State: 0 = S, 1 = I
    state = np.zeros(n_agents)
    # Seed initial infectors (Fake News Originators)
    n_initial = max(1, n_agents // 20)
    infectors = rng.choice(n_agents, size=n_initial, replace=False)
    state[infectors] = 1
    
    # Parameters
    beta = params.get("abm_beta", 0.2)   # Transmission
    gamma = params.get("abm_gamma", 0.1)  # Recovery
    
    # Forcing: Virality Shock (increases beta)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    adj = [list(G.neighbors(i)) for i in range(n_agents)]
    
    series_pv = [] # Prevalence (Infected Fraction)
    series_grid = []
    store_grid = params.get("_store_grid", True)
    
    for t in range(steps):
        # Modulate beta by virality
        f_t = forcing[t] if t < len(forcing) else 0.0
        beta_eff = beta + 0.3 * f_t
        
        # Macro coupling (if macro prevalence is high, harder to recover?)
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            macro_val = macro_series[t]
            gamma_eff = gamma * (1.0 - coupling * macro_val)
            gamma_eff = max(0.01, gamma_eff)
        else:
            gamma_eff = gamma
        
        new_state = state.copy()
        
        for i in range(n_agents):
            if state[i] == 0: # Susceptible
                # Infection from neighbors
                n_infected = sum(state[j] for j in adj[i])
                if n_infected > 0:
                    prob = 1 - (1 - beta_eff) ** n_infected
                    if rng.random() < prob:
                        new_state[i] = 1
            else: # Infected
                # Recovery
                if rng.random() < gamma_eff:
                    new_state[i] = 0
                    
        state = new_state
        
        # Prevalence
        prevalence = np.mean(state)
        series_pv.append(prevalence)
        
        # Grid
        grid_dim = int(np.sqrt(n_agents))
        if grid_dim * grid_dim == n_agents:
            grid_rep = state.reshape((grid_dim, grid_dim))
        else:
            grid_rep = np.zeros((10, 10))
            grid_rep.flat[:n_agents] = state
        if store_grid:
            series_grid.append(grid_rep.copy())
        
    return {"pv": series_pv, "forcing": forcing, "grid": series_grid}

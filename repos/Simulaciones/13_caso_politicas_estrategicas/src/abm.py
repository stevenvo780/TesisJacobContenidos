"""
abm.py — 13_caso_politicas_estrategicas (Top-Tier)

Model: Bass Diffusion on Scale-Free Network (Policy Adoption)

Reference:
- Bass, F.M. (1969): "A New Product Growth Model for Consumer Durables"
- Janssen & Jager (2003): Agent-Based Policy Diffusion
- Maoz & Russett: Democratic Peace Network Effects

Agents: Countries / Institutions
State: Adopted (1) or Not Adopted (0)
Dynamics:
    - Innovation Probability (p): External pressure (treaties, norms)
    - Imitation Probability (q * neighbors_adopted): Peer influence
"""

import numpy as np
import networkx as nx

def simulate_abm(params, steps, seed=42):
    """
    Bass Diffusion ABM on Scale-Free Network.
    
    Returns:
    - s: Adoption Rate (Fraction of Adopters)
    - grid: Visual representation of adoption state
    """
    rng = np.random.default_rng(seed)
    
    # Network Topology: Scale-Free (Power-Law in International Relations)
    n_agents = params.get("n_agents", 50) # 50 Countries
    G = nx.barabasi_albert_graph(n_agents, 2, seed=seed)
    
    # Initial State: All Non-Adopted (0)
    state = np.zeros(n_agents)
    
    # Forcing: External Pressure (Treaties, UN Resolutions, etc.)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Bass Parameters
    p = params.get("abm_p", 0.01) # Innovation (Base adoption rate)
    q = params.get("abm_q", 0.3)  # Imitation (Peer influence strength)
    
    # Macro Coupling (Hyperobject Constraint)
    # Global Effectiveness (ODE State) influences individual adoption?
    # If global policy is "effective", countries are MORE likely to adopt (feedback).
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    # Pre-compute adjacency
    adj = [list(G.neighbors(i)) for i in range(n_agents)]
    
    series_s = [] # Adoption rate
    series_grid = []
    
    for t in range(steps):
        # External Forcing modulates p
        f_t = forcing[t] if t < len(forcing) else 0.0
        p_eff = p + 0.1 * f_t # Stronger treaties -> higher p
        
        # Macro Coupling modulates...
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            # If Global Effectiveness (ODE) is high, peer pressure increases
            macro_val = macro_series[t]
            q_eff = q + coupling * macro_val
        else:
            q_eff = q
        
        # Current Adoption Rate
        A = np.mean(state)
        
        # Update each agent
        new_state = state.copy()
        for i in range(n_agents):
            if state[i] == 0: # Not yet adopted
                # Neighbors' adoption fraction
                neighbors = adj[i]
                if len(neighbors) > 0:
                    neighbors_adopted = np.mean([state[j] for j in neighbors])
                else:
                    neighbors_adopted = 0.0
                
                # Bass Probability
                prob = (p_eff + q_eff * neighbors_adopted) * (1.0 - A)
                prob = np.clip(prob, 0.0, 1.0)
                
                if rng.random() < prob:
                    new_state[i] = 1
        
        state = new_state
        
        # Record
        adoption_rate = np.mean(state)
        series_s.append(adoption_rate)
        
        # Grid visualization
        grid_dim = int(np.sqrt(n_agents))
        if grid_dim * grid_dim == n_agents:
            grid_rep = state.reshape((grid_dim, grid_dim))
        else:
            grid_rep = np.zeros((7, 7)) # Fallback for 50 agents
            grid_rep.flat[:n_agents] = state
        series_grid.append(grid_rep.copy())
        
    return {"s": series_s, "forcing": forcing, "grid": series_grid}

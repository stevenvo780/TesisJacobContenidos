"""
abm.py — 05_caso_epidemiologia (Top-Tier)

Model: SEIR Network Epidemic ABM

This is THE standard model for epidemic simulation (CDC, WHO).
We implement individual-based SEIR on a scale-free contact network.

Reference:
- Kermack & McKendrick (1927): "A Contribution to the Theory of Epidemics" (Proc. Royal Soc.)
- Keeling & Eames (2005): "Networks and Epidemic Models" (J. R. Soc. Interface)
- Ferguson et al. (2020): Imperial College COVID Model

Agents: Individuals
State: S (Susceptible), E (Exposed), I (Infected), R (Recovered)
Dynamics:
  - Transmission on network edges
  - Latent period (E -> I)
  - Recovery period (I -> R)
  - Reinfection possible (R -> S, if no permanent immunity)
"""

import numpy as np
import networkx as nx

def simulate_abm(params, steps, seed=42):
    """
    SEIR Network Epidemic ABM.
    
    Individual-level epidemic simulation on a scale-free network.
    
    Returns:
    - incidence: New infections per timestep
    - grid: Population by SEIR state
    """
    rng = np.random.default_rng(seed)
    
    # Network: Scale-free (Barabasi-Albert)
    n_agents = params.get("n_agents", 1000)
    m = params.get("network_m", 3)  # Edges per new node
    
    G = nx.barabasi_albert_graph(n_agents, m, seed=seed)
    
    # State: 0=S, 1=E, 2=I, 3=R
    states = np.zeros(n_agents, dtype=int)
    
    # Initial infected (patient zero)
    initial_infected = max(1, int(n_agents * 0.001))
    infected_idx = rng.choice(n_agents, size=initial_infected, replace=False)
    states[infected_idx] = 2  # I
    
    # Timers for E and I states
    exposure_timer = np.zeros(n_agents)  # Days until E -> I
    infection_timer = np.zeros(n_agents)  # Days until I -> R
    
    # Disease Parameters
    beta = params.get("abm_beta", 0.3)        # Transmission prob per contact
    latent_period = params.get("abm_latent", 3)    # Days E -> I
    infectious_period = params.get("abm_infectious", 7)  # Days I -> R
    immunity_waning = params.get("abm_waning", 0.0)  # Prob R -> S per day
    
    # Forcing: Behavioral changes / interventions
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps)
        
    # Macro Coupling (ODE reproduction number)
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    # Initialize timers for initial infected
    infection_timer[infected_idx] = rng.integers(1, infectious_period + 1, size=initial_infected)
    
    # Pre-compute adjacency list
    adj = {node: list(G.neighbors(node)) for node in G.nodes()}
    
    series_incidence = []
    series_grid = []
    
    for t in range(steps):
        # Intervention effect (reduces transmission)
        intervention = forcing[t] if t < len(forcing) else 1.0
        beta_eff = beta * intervention
        
        # Macro coupling: adjust beta to match macro R0
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_R = macro_series[t]
            # R0 ~ beta * infectious_period * average_contacts
            avg_contacts = np.mean([len(adj[i]) for i in range(n_agents)])
            current_R0 = beta_eff * infectious_period * avg_contacts
            if current_R0 > 0:
                beta_eff = beta_eff * (1 + coupling * 0.1 * (target_R - current_R0) / current_R0)
                beta_eff = np.clip(beta_eff, 0, 1)
                
        new_infections = 0
        new_states = states.copy()
        
        # Process each agent
        for i in range(n_agents):
            if states[i] == 0:  # Susceptible
                # Check contacts with infectious
                neighbors = adj[i]
                for j in neighbors:
                    if states[j] == 2:  # Neighbor is Infectious
                        if rng.random() < beta_eff:
                            new_states[i] = 1  # Exposed
                            exposure_timer[i] = latent_period
                            new_infections += 1
                            break
                            
            elif states[i] == 1:  # Exposed
                exposure_timer[i] -= 1
                if exposure_timer[i] <= 0:
                    new_states[i] = 2  # Infectious
                    infection_timer[i] = infectious_period
                    
            elif states[i] == 2:  # Infectious
                infection_timer[i] -= 1
                if infection_timer[i] <= 0:
                    new_states[i] = 3  # Recovered
                    
            elif states[i] == 3:  # Recovered
                # Waning immunity
                if immunity_waning > 0 and rng.random() < immunity_waning:
                    new_states[i] = 0  # Susceptible again
                    
        states = new_states
        
        # Record incidence (new infections)
        series_incidence.append(new_infections)
        
        # Grid representation: SEIR compartment counts
        grid_size = params.get("grid_size", 20)
        S_count = np.sum(states == 0)
        E_count = np.sum(states == 1)
        I_count = np.sum(states == 2)
        R_count = np.sum(states == 3)
        
        # Create a visual grid (approximate spatial distribution)
        grid = np.zeros((grid_size, grid_size))
        for i in range(n_agents):
            gx = i % grid_size
            gy = i // grid_size % grid_size
            if states[i] == 2:  # Infectious
                grid[gx, gy] += 1
                
        series_grid.append(grid)
        
    return {"incidence": series_incidence, "forcing": forcing, "grid": series_grid}

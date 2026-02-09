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
from scipy.sparse import csr_matrix

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
    immunity_waning = params.get("abm_waning", 0.02)  # Prob R -> S per step (~50 step immunity)
    
    # Forcing: Behavioral changes / interventions
    # NOTE: forcing_series comes Z-scored from the validator (mean≈0, std≈1).
    # We use it as a MODULATOR around base beta, not a raw multiplier.
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.zeros(steps)  # No external forcing = no modulation
        
    # Macro Coupling (ODE reproduction number)
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    # Initialize timers for initial infected
    infection_timer[infected_idx] = rng.integers(1, infectious_period + 1, size=initial_infected)
    
    # Pre-compute sparse adjacency matrix for vectorized transmission
    adj_matrix = nx.adjacency_matrix(G).astype(np.float64)
    
    series_incidence = []
    series_grid = []
    
    for t in range(steps):
        # Intervention effect (modulates transmission around base beta)
        # forcing[t] is Z-scored: 0 = mean, +1 = 1 std above, etc.
        intervention = forcing[t] if t < len(forcing) else 0.0
        beta_eff = beta * np.clip(1.0 + forcing_scale * intervention, 0.1, 2.0)
        
        # Macro coupling: adjust beta to match macro R0
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_R = macro_series[t]
            avg_contacts = 2 * G.number_of_edges() / n_agents
            current_R0 = beta_eff * infectious_period * avg_contacts
            if current_R0 > 0:
                beta_eff = beta_eff * (1 + coupling * 0.1 * (target_R - current_R0) / current_R0)
                beta_eff = np.clip(beta_eff, 0, 1)
                
        # Vectorized SEIR transitions
        is_S = (states == 0)
        is_E = (states == 1)
        is_I = (states == 2)
        is_R = (states == 3)
        
        # Transmission: for each susceptible, count infectious neighbors
        infectious_vec = is_I.astype(np.float64)
        n_inf_neighbors = np.asarray(adj_matrix.dot(infectious_vec)).ravel()
        
        # Probability of NOT being infected by any neighbor: (1-beta)^n_inf_neighbors
        prob_escape = np.power(1 - beta_eff, n_inf_neighbors)
        prob_infected = 1 - prob_escape
        
        # Draw random for each susceptible
        new_exposed = is_S & (rng.random(n_agents) < prob_infected)
        new_infections = int(np.sum(new_exposed))
        
        # E -> I transitions (timer expired)
        exposure_timer[is_E] -= 1
        new_infectious = is_E & (exposure_timer <= 0)
        
        # I -> R transitions (timer expired)
        infection_timer[is_I] -= 1
        new_recovered = is_I & (infection_timer <= 0)
        
        # R -> S waning immunity
        new_susceptible = np.zeros(n_agents, dtype=bool)
        if immunity_waning > 0:
            new_susceptible = is_R & (rng.random(n_agents) < immunity_waning)
        
        # Apply transitions
        states[new_exposed] = 1
        exposure_timer[new_exposed] = latent_period
        states[new_infectious] = 2
        infection_timer[new_infectious] = infectious_period
        states[new_recovered] = 3
        states[new_susceptible] = 0
        
        # Record incidence (new infections)
        series_incidence.append(new_infections)
        
        # Grid representation: SEIR compartment counts
        grid_size = params.get("grid_size", 20)
        S_count = np.sum(states == 0)
        E_count = np.sum(states == 1)
        I_count = np.sum(states == 2)
        R_count = np.sum(states == 3)
        
        # Grid representation: approximate spatial distribution (vectorized)
        grid = np.zeros((grid_size, grid_size))
        inf_idx = np.where(states == 2)[0]
        gx = inf_idx % grid_size
        gy = (inf_idx // grid_size) % grid_size
        np.add.at(grid, (gx, gy), 1)
                
        series_grid.append(grid)
        
    return {"incidence": series_incidence, "forcing": forcing, "grid": series_grid}

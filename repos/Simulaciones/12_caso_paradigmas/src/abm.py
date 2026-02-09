import numpy as np
import networkx as nx

def simulate_abm(params, steps, seed=42):
    """
    Ising Model on Scale-Free Network (Scientific Paradigms).
    
    - Agents: Scientists (Nodes).
    - State: Spin S_i in {-1, +1} (Paradigm A vs B).
    - Dynamics: Glauber / Metropolis Algorithm.
      Delta E = 2 * S_i * (sum(S_j) + H)
      P(flip) = exp(-Delta E / T)
    - Emergence: Spontaneous Magnetization (Consensus) below Tc.
    """
    rng = np.random.default_rng(seed)
    
    # 1. Network Topology (Scientific Community)
    n_agents = params.get("n_agents", 100)
    # Scale-Free (Barabasi-Albert) - Hubs are influence leaders
    G = nx.barabasi_albert_graph(n_agents, 3, seed=seed)
    
    # Initial State: Random spins
    spins = rng.choice([-1, 1], size=n_agents)
    
    # Forcing: External Evidence (H field)
    forcing = params.get("forcing_series") # interpret as Field H
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Temperature Series (Anomalies)
    # Passed as 'macro_series' or inferred?
    # For simplicity, let's look for a 'temperature_series' param or use forcing magnitude?
    # Or just constant T? 
    # To match synthetic data, we need dynamic T.
    # Let's assume params['temperature'] is a base, modulated by...
    # Actually, in the synthetic generator, we varied T.
    # Here, let's fix T near critical and drive with H, OR vary T.
    # We'll use a param default T close to Tc.
    
    T_base = params.get("abm_temperature", 2.5) # critical for BA graph is high
    
    series_m = [] # Magnetization (Average Spin)
    series_grid = [] # Pattern (spins)
    
    # Pre-compute adjacency lists for speed
    adj = [list(G.neighbors(i)) for i in range(n_agents)]
    
    for t in range(steps):
        # External Field (Evidence)
        H_ext = forcing[t] if t < len(forcing) else 0.0
        
        # Macro Coupling (Social Pressure from Paradigm)
        # If coupling > 0, the Global Consensus (ODE State) biases local nodes.
        # This represents "Scientific Zeitgeist" or "Funding Bias".
        macro_series = params.get("macro_target_series")
        coupling = params.get("macro_coupling", 0.0)
        
        H_macro = 0.0
        if macro_series is not None and t < len(macro_series):
            H_macro = macro_series[t] # Order Parameter M from ODE
            
        # Total Effective External Field
        H = H_ext + coupling * H_macro
        
        # Metropolis Updates
        # Random sequential updates per step (N times)
        for _ in range(n_agents):
            i = rng.integers(0, n_agents)
            s_i = spins[i]
            
            # Local Field: Sum of neighbors spins
            # h_local = sum(spins[j] for j in neighbors)
            # Optimization: raw access
            h_local = sum(spins[j] for j in adj[i])
            
            # Total energy change if flipped
            # E = - J * S_i * h_local - H * S_i
            # Delta E = E_new - E_old
            # S_new = -S_i
            # Delta E = (- (-S_i) * (h_local + H)) - (- (S_i) * (h_local + H))
            #         = (S_i * (h_local + H)) + (S_i * (h_local + H))
            #         = 2 * S_i * (h_local + H)
            
            delta_E = 2 * s_i * (h_local + H)
            
            if delta_E <= 0:
                # Energy lowers, accept flip
                spins[i] = -s_i
            else:
                # Energy increases, accept with prob exp(-dE/T)
                # T relates to "Anomalies" or "Tolerance"
                # If T is high (Crisis), we flip easily (Randomness/search).
                # If T is low (Normal Science), we stick to consensus.
                
                # To capture the Synthetic dynamic, T must vary?
                # We don't have a direct T-series input usually.
                # Let's assume constant T for the "Validator" default,
                # unless macro_coupling modulates it?
                # Or maybe H represents the evidence.
                
                prob = np.exp(-delta_E / T_base)
                if rng.random() < prob:
                    spins[i] = -s_i
                    
        # Calculate Magnetization
        m = np.mean(spins)
        series_m.append(m)
        
        # Store state (visual)
        # Map to grid? Network isn't grid.
        # Just store raw 1D array, wrapper can reshape if needed or store as is.
        # Validator expects grid-like for spatial analysis?
        # Let's map to a Dummy 10x10 grid if N=100
        grid_dim = int(np.sqrt(n_agents))
        if grid_dim * grid_dim == n_agents:
            grid_rep = spins.reshape((grid_dim, grid_dim))
        else:
            grid_rep = np.zeros((10,10)) # fallback
            
        series_grid.append(grid_rep.copy())
        
    return {"j": series_m, "forcing": forcing, "grid": series_grid}

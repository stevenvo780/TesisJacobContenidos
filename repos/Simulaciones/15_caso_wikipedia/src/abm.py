"""
abm.py — 15_caso_wikipedia (Top-Tier)

Model: Axelrod Culture Dynamics / Edit War on Network

Reference:
- Axelrod (1997): "The Dissemination of Culture"
- Castellano et al. (2009): "Social Dynamics" (Rev Mod Phys)
- Yasseri et al. (2012): "Edit Wars"

Agents: Wikipedia Editors
State: Opinion Vector (e.g., [Political, Factual, Style] stances)
Dynamics:
  - Homophily: Interact more with similar editors
  - Convergence: After interaction, become more similar
  - Conflict: If very different, may revert each other's edits
"""

import numpy as np
import networkx as nx

def simulate_abm(params, steps, seed=42):
    """
    Axelrod Culture Model for Wikipedia Edit Dynamics.
    
    Returns:
    - w: Article Quality (Cumulative constructive edits)
    - grid: Editor opinion states
    """
    rng = np.random.default_rng(seed)
    
    # Network: Small-World (Wikipedia editor community)
    n_agents = params.get("n_agents", 50)
    G = nx.watts_strogatz_graph(n_agents, 4, 0.3, seed=seed)
    
    # Opinion: Vector of length F (Features)
    n_features = params.get("n_features", 5)
    n_traits = params.get("n_traits", 3) # Values per feature
    opinions = rng.integers(0, n_traits, size=(n_agents, n_features))
    
    # Article State: Quality Score
    quality = params.get("p0", 0.1)
    
    # Forcing: External Controversy (Events)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    adj = [list(G.neighbors(i)) for i in range(n_agents)]
    
    series_w = [] # Quality
    series_grid = []
    
    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0
        
        # Axelrod Dynamics
        for _ in range(n_agents):
            i = rng.integers(0, n_agents)
            if len(adj[i]) == 0:
                continue
            j = rng.choice(adj[i])
            
            # Similarity: Fraction of shared features
            sim = np.mean(opinions[i] == opinions[j])
            
            # Interact with probability proportional to similarity
            if rng.random() < sim:
                # Find a feature where they differ
                diff_features = np.where(opinions[i] != opinions[j])[0]
                if len(diff_features) > 0:
                    # i adopts j's trait on one feature
                    f_idx = rng.choice(diff_features)
                    opinions[i, f_idx] = opinions[j, f_idx]
                    # Constructive edit! Quality increases
                    quality += 0.01
            else:
                # Low similarity -> Conflict
                # Chance of revert (quality decreases)
                if sim < 0.3 and rng.random() < 0.5:
                    quality -= 0.02 * (1 + f_t) # More reverting during controversy
                    
        # Macro Coupling: If global quality is high, stabilize
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            macro_val = macro_series[t]
            quality = (1 - coupling * 0.1) * quality + coupling * 0.1 * macro_val
            
        quality = np.clip(quality, 0.0, 2.0)
        series_w.append(quality)
        
        # Grid: Show opinion state (flatten to 2D for viz)
        grid_rep = np.zeros((7, 7))
        # Use first feature for visualization
        for i in range(min(49, n_agents)):
            grid_rep.flat[i] = opinions[i, 0]
        series_grid.append(grid_rep.copy())
        
    return {"w": series_w, "forcing": forcing, "grid": series_grid}

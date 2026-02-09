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

def simulate_abm(params, steps, seed=42):
    """
    Axelrod Culture Model for Wikipedia Edit Dynamics.
    
    Vectorized synchronous update: all agent interactions computed
    simultaneously from start-of-step opinions.
    
    Returns:
    - w: Article Quality (Cumulative constructive edits)
    - grid: Editor opinion states
    """
    rng = np.random.default_rng(seed)
    
    # Network: Small-World (Wikipedia editor community)
    # Build adjacency directly with numpy (avoid networkx overhead)
    n_agents = params.get("n_agents", 50)
    k_neighbors = 4
    p_rewire = 0.3
    
    # Build Watts-Strogatz adjacency list with numpy
    adj = [set() for _ in range(n_agents)]
    for i in range(n_agents):
        for j_off in range(1, k_neighbors // 2 + 1):
            j = (i + j_off) % n_agents
            adj[i].add(j)
            adj[j].add(i)
    # Rewire
    for i in range(n_agents):
        for j_off in range(1, k_neighbors // 2 + 1):
            if rng.random() < p_rewire:
                j_old = (i + j_off) % n_agents
                candidates = [c for c in range(n_agents) if c != i and c not in adj[i]]
                if candidates:
                    j_new = rng.choice(candidates)
                    adj[i].discard(j_old)
                    adj[j_old].discard(i)
                    adj[i].add(j_new)
                    adj[j_new].add(i)
    
    # Convert to list-of-arrays for fast indexing
    adj_list = [np.array(sorted(s), dtype=np.int32) for s in adj]
    nonempty = np.array([i for i in range(n_agents) if len(adj_list[i]) > 0], dtype=np.int32)
    
    # Opinion: Vector of length F (Features)
    n_features = params.get("n_features", 5)
    n_traits = params.get("n_traits", 3)
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
    
    series_w = []
    series_grid = []
    
    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0
        
        # Axelrod Dynamics — fully vectorized synchronous update
        if len(nonempty) > 0:
            agents_i = rng.choice(nonempty, size=n_agents)
            # Pick random neighbor for each agent (vectorized with pre-indexed adjacency)
            agents_j = np.array([rng.choice(adj_list[i]) for i in agents_i])
            
            # Similarities: fraction of matching features
            match_mask = (opinions[agents_i] == opinions[agents_j])  # (n_agents, n_features)
            sims = match_mask.mean(axis=1)  # (n_agents,)
            
            # Interaction rolls
            rolls = rng.random(n_agents)
            
            # --- Convergent interactions: roll < sim AND not fully similar ---
            diff_mask = ~match_mask  # (n_agents, n_features)
            n_diffs = diff_mask.sum(axis=1)  # (n_agents,)
            converge = (rolls < sims) & (n_diffs > 0)
            n_converge = converge.sum()
            
            if n_converge > 0:
                # For each converging pair, pick one random differing feature
                conv_idx = np.where(converge)[0]
                conv_diffs = diff_mask[conv_idx]  # (n_converge, n_features)
                # Weighted random selection: for each row, pick a random True column
                # Assign random priorities to True positions, pick the max
                priorities = rng.random((n_converge, n_features)) * conv_diffs
                chosen_features = priorities.argmax(axis=1)
                # Apply: opinions[agents_i[conv_idx], chosen_features] = opinions[agents_j[conv_idx], chosen_features]
                opinions[agents_i[conv_idx], chosen_features] = opinions[agents_j[conv_idx], chosen_features]
                quality += 0.01 * n_converge
            
            # --- Conflict interactions: roll >= sim AND sim < 0.3 ---
            conflict_rolls = rng.random(n_agents)
            conflict = (rolls >= sims) & (sims < 0.3) & (conflict_rolls < 0.5)
            n_conflict = conflict.sum()
            quality -= 0.02 * (1 + f_t) * n_conflict
                    
        # Macro Coupling
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            macro_val = macro_series[t]
            quality = (1 - coupling * 0.1) * quality + coupling * 0.1 * macro_val
            
        quality = np.clip(quality, 0.0, 2.0)
        series_w.append(quality)
        
        # Grid: Show opinion state (flatten to 2D for viz)
        grid_rep = np.zeros((7, 7))
        grid_rep.flat[:min(49, n_agents)] = opinions[:min(49, n_agents), 0]
        series_grid.append(grid_rep.copy())
        
    return {"w": series_w, "forcing": forcing, "grid": series_grid}

import numpy as np
import networkx as nx
from data import generate_city_graph

def simulate_abm(params, steps, seed=42):
    """
    Traffic ABM (High Fidelity).
    - Network: Scale-Free City.
    - Agents: Vehicles with Origin-Destination.
    - Dynamics: Routing + Congestion.
    """
    rng = np.random.default_rng(seed)
    
    # 1. Setup Network
    n_nodes = params.get("n_nodes", 100)
    G = generate_city_graph(n_nodes, seed=seed)
    
    # 2. Setup Agents
    n_agents = params.get("n_agents", 500)
    agents = []
    
    # Assign Homes and Works
    # Hubs (low IDs) are Work centers. High IDs are Homes.
    work_nodes = list(range(10))
    home_nodes = list(range(10, n_nodes))
    
    for i in range(n_agents):
        origin = rng.choice(home_nodes)
        dest = rng.choice(work_nodes)
        agents.append({
            "id": i,
            "origin": origin,
            "dest": dest,
            "path": [], # List of nodes
            "pos": 0,   # Index in path
            "active": False,
            "arrival_time": None
        })
        
    # Forcing (Demand Profile)
    # NOTE: forcing_series comes Z-scored from the validator (mean≈0, std≈1).
    # We use it to MODULATE demand around a baseline, not as absolute demand.
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.zeros(steps)  # No modulation = baseline demand
        
    series_flow = []
    series_grid = [] # Store aggregate density map?
    
    # Traffic State tracking
    # edges: (u, v) -> current_occupancy
    edge_occupancy = {e: 0 for e in G.edges()}
    total_completed = 0
    
    for t in range(steps):
        # 1. Demand Injection (Rush Hour based on Forcing)
        # Baseline demand + Z-scored modulation
        f_t = forcing[t] if t < len(forcing) else 0.0
        demand_level = max(0.1, 0.5 + forcing_scale * f_t)  # Baseline 0.5, modulated
        n_to_activate = int(demand_level * 50) # 50 agents/hr max
        
        # Activate random dormant agents
        dormant = [a for a in agents if not a["active"] and a["arrival_time"] is None]
        if not dormant:
            # Also re-queue agents with empty paths from recirculation
            dormant = [a for a in agents if not a["active"] and len(a["path"]) == 0]
        if dormant:
            batch = rng.choice(dormant, size=min(len(dormant), n_to_activate), replace=False)
            for a in batch:
                a["active"] = True
                # Compute Initial Path (Dijkstra)
                try:
                    path = nx.shortest_path(G, source=a["origin"], target=a["dest"], weight="travel_time")
                    a["path"] = path
                    a["pos"] = 0
                except nx.NetworkXNoPath:
                    a["active"] = False # Nowhere to go
                    
        # 2. Update Edge Speeds (Greenshields)
        # v = vf * (1 - k/kj)
        # Update graph weights based on occupancy
        for u, v in G.edges():
            capacity = G[u][v]['capacity']
            occ = edge_occupancy.get((u, v), 0) + edge_occupancy.get((v, u), 0) # Undirected flow logic? Or directed?
            # NetworkX graph is undirected by default unless DiGraph. generate_city_graph uses barabasi_albert (undir).
            # So (u,v) flows interact with (v,u)? Let's assume non-separated lanes for simplicity (Jam is bidirectional).
            
            density_ratio = occ / (capacity * 0.1) # Scale capacity to simulation step
            density_ratio = min(1.0, density_ratio)
            
            speed_factor = max(0.1, 1.0 - density_ratio) # Min 10% speed
            
            # 2b. Macro-Coupling (Hyperobject Constraint)
            # If Global State (MFD) says "Jam", we slow down everyone.
            # macro_series[t] is Global Flow or Density?
            # ODE returns 'v' (Flow). High Flow = Good? Or Jam?
            # MFD: High Flow means Optimal Density. Low Flow means Empty OR Jammed.
            # Let's assume 'macro_series' passed here is a "Stress" or "Congestion" index?
            # hybrid_validator passes the ODE output ('v' = Flow).
            # Using Flow to constrain speed is tricky (Parabolic).
            # Let's assume the ODE output for coupling is DENSITY or inverse speed?
            # Config 'ode_key'='v'.
            # We can use 'forcing' as the macro signal? No, forcing is Demand.
            
            # Let's use a simple Global Constraint:
            # global_factor = params.get("macro_series")[t] if available
            macro_series = params.get("macro_target_series")
            coupling = params.get("macro_coupling", 0.0)
            
            if macro_series is not None and t < len(macro_series) and coupling > 0.0:
                # Interpret macro_val as "Global Speed Factor" or similar?
                # If ODE outputs Flow, it's hard to interpret as Speed Constraint directly.
                # But let's assume High Flow = High Speed (in uncongested regime).
                # Normalize macro_val?
                macro_val = macro_series[t]
                # Assume macro_val is approx proportional to system efficiency.
                # We blend local speed with global efficiency.
                # speed = (1-c)*local + c*global
                # Need to normalize macro_val to [0,1].
                # Synthetic max flow ~ 2000? 
                # Let's just use it as a raw factor if scaled? 
                # Or simplistic: macro_val is just a signal.
                
                # BETTER: Recalibrate ODE to output "Efficiency" (0-1) in 'v' or separate key 'e'?
                # For now, let's assume macro_val is scaled flow.
                # If flow is high, traffic moves.
                
                global_speed = min(1.0, macro_val / 500.0) # Crude normalization
                speed_factor = (1.0 - coupling) * speed_factor + coupling * global_speed
            
            current_travel_time = G[u][v]['length'] / (G[u][v]['free_flow_speed'] * max(0.01, speed_factor))
            G[u][v]['weight'] = current_travel_time # Update for routing
            
        # 3. Move Agents
        # Compute global speed factor from macro coupling
        global_macro_factor = 1.0
        macro_series = params.get("macro_target_series")
        coupling = params.get("macro_coupling", 0.0)
        if macro_series is not None and t < len(macro_series) and coupling > 0.0:
            macro_val = macro_series[t]
            # Interpret ODE output as normalized efficiency signal
            global_macro_factor = 1.0 + coupling * macro_val
            global_macro_factor = max(0.1, min(3.0, global_macro_factor))
        
        # Reset occupancy for next step tally or keep persistent?
        # Agents occupy edge for duration.
        # Simplified: Agents jump nodes based on speed?
        # Or Agents occupy ONE edge at a time.
        
        # Let's clear occupancy and rebuild it based on agent positions
        edge_occupancy = {e: 0 for e in G.edges()}
        
        active_agents = [a for a in agents if a["active"] and len(a["path"]) > 0]
        
        for a in active_agents:
            # Check if arrived
            if a["pos"] >= len(a["path"]) - 1:
                a["active"] = False
                a["arrival_time"] = t
                total_completed += 1
                # Reset for next trip (recirculate)
                a["origin"], a["dest"] = a["dest"], a["origin"]
                a["path"] = []
                a["pos"] = 0
                a["arrival_time"] = None
                continue
                
            # Current Edge
            u = a["path"][a["pos"]]
            v = a["path"][a["pos"]+1]
            
            # Register occupancy
            if u < v: edge = (u,v)
            else: edge = (v,u)
            edge_occupancy[edge] = edge_occupancy.get(edge, 0) + 1
            
            # Advance logic: Probabilistic jump based on edge congestion
            # capacity check
            capacity = G[u][v]['capacity'] * 0.1
            current_jam = edge_occupancy[edge]
            
            # Probability to move to next node
            # P_move ~ SpeedFactor
            # If jammed, P_move -> low
            density = current_jam / capacity
            prob_move = max(0.05, (1.0 - density) * global_macro_factor)
            
            if rng.random() < prob_move:
                a["pos"] += 1
                # Re-routing chance if jammed?
                if density > 0.8 and rng.random() < 0.2:
                    # Re-calc path from current v to dest
                    try:
                        new_path = nx.shortest_path(G, source=v, target=a["dest"], weight="weight")
                        a["path"] = a["path"][:a["pos"]+1] + new_path[1:]
                    except:
                        pass
                        
        # Emergent Metric: Total Flow (Active Agents moving)
        # Or Network Flux.
        # Let's track Total Active Agents (Density) vs Total Completed (Flow)?
        # Or just number of active agents (Density proxy).
        series_flow.append(len(active_agents))
        
        # Grid visual (Density Heatmap)
        grid_size = params.get("grid_size", 20)
        grid = np.zeros((grid_size, grid_size))
        
        # Aggregate active agent positions
        for a in active_agents:
            if not a["active"] or len(a["path"]) == 0 or a["pos"] >= len(a["path"]):
                continue
            u = a["path"][a["pos"]]
            v = a["path"][min(len(a["path"])-1, a["pos"]+1)]
            
            # Interpolate position? Assume at node u for simplicity
            try:
                # Use node u position
                px, py = G.nodes[u]['pos']
                # Map to grid
                gx = int(px * (grid_size - 1))
                gy = int(py * (grid_size - 1))
                grid[gx, gy] += 1
            except KeyError:
                pass
                
        series_grid.append(grid)
        
    return {"v": series_flow, "forcing": forcing}

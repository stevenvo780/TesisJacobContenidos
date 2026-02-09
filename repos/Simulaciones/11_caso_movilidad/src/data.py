import os
import sys
import numpy as np
import pandas as pd
import networkx as nx

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from data_universal import fetch_case_data

def generate_city_graph(n_nodes=100, seed=42):
    """
    Generates a Scale-Free City Network (Barabasi-Albert).
    """
    rng = np.random.default_rng(seed)
    # Preferential Attachment (Hubs = Highways/Centers)
    G = nx.barabasi_albert_graph(n_nodes, 2, seed=seed)
    
    # Assign Spatial Positions (Bettencourt's Fractal City)
    # Use spring layout or random? Random is fine for abstract city.
    # Hubs should be central?
    pos = nx.spring_layout(G, seed=seed)
    # Visualize as mapping to [0,1]x[0,1]
    # layout returns {node: [x,y]}
    # Normalize to [0,1]
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    for n in G.nodes():
        norm_x = (pos[n][0] - min_x) / (max_x - min_x + 1e-6)
        norm_y = (pos[n][1] - min_y) / (max_y - min_y + 1e-6)
        G.nodes[n]['pos'] = (norm_x, norm_y)
    
    # Assign Edge Capacities and Lengths
    for u, v in G.edges():
        # Hub edges (connected to low index nodes) have higher capacity
        is_hub = (u < 10 or v < 10)
        G[u][v]['capacity'] = 2000 if is_hub else 500 # Vehicles per hour
        G[u][v]['length'] = rng.uniform(0.5, 5.0) # km
        G[u][v]['free_flow_speed'] = 60 if is_hub else 30 # km/h
        G[u][v]['travel_time'] = G[u][v]['length'] / G[u][v]['free_flow_speed']
        
    return G

def make_synthetic(start_date, end_date, seed=101):
    """
    Generates synthetic traffic flow data based on Macroscopic Fundamental Diagram (MFD).
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="h") # Hourly data!
    steps = len(dates)
    
    # Daily Cycle Forcing (Rush Hour)
    # Double hump: Morning (8am) and Evening (6pm)
    t_hour = dates.hour.values
    
    morning_rush = np.exp(-((t_hour - 8)**2) / 8.0)
    evening_rush = np.exp(-((t_hour - 18)**2) / 8.0)
    demand_pattern = 0.5 + 1.0 * (morning_rush + evening_rush)
    
    # MFD Simulation (Backward Bending)
    # Flow Q = k * v(k)
    # v(k) = vf * (1 - k/kj)
    # Q(k) = vf * k * (1 - k/kj)  [Parabolic]
    
    kj = 150.0 # Jam density per km
    vf = 60.0  # Free flow speed
    
    density = np.zeros(steps)
    flow = np.zeros(steps)
    
    k_t = 10.0 # Initial density
    
    for t in range(steps):
        # Demand inflow
        inflow = demand_pattern[t] * 10.0 + rng.normal(0, 2.0)
        
        # Outflow (Capacity constrained by MFD)
        q_out = vf * k_t * (1 - k_t/kj)
        q_out = max(0, q_out)
        
        # Density Dynamics: dK/dt = Inflow - Outflow
        dk = (inflow - q_out) * 0.1 # Time step scaling
        k_t += dk
        k_t = max(0, min(kj, k_t))
        
        density[t] = k_t
        flow[t] = q_out
        
    # Observed Metric: Average Speed or Flow?
    # Let's observe Flow (Traffic Volume)
    obs = flow + rng.normal(0, 5.0, size=steps)
    obs = np.clip(obs, 0, None)
    
    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"mfd_true": {"vf": vf, "kj": kj}}
    return df, meta

def load_real_data(start_date, end_date):
    # Construct absolute path to the data directory (root/data)
    # Assuming this script is in repos/Simulaciones/11_caso_movilidad/src/
    cache_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    )
    # For now, return synthetic if no real data
    # fetch_case_data handles the fallback logic internally usually, 
    # but here we hardcode fallback to make_synthetic if file missing logic 
    # isn't fully in fetch_case_data for this specific path style.
    # Actually, let's use the fetch_case_data generic.
    
    df, meta = fetch_case_data("11_caso_movilidad", start_date, end_date, cache_path=cache_path)
    if df is not None and not df.empty:
         df["date"] = pd.to_datetime(df["date"])
         return df.dropna()
         
    return make_synthetic(start_date, end_date)[0]

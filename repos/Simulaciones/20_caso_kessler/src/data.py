"""
data.py — 20_caso_kessler (Top-Tier)

Model: NASA ORDEM / ESA MASTER-inspired Space Debris Environment

This models the Kessler Syndrome - the cascade of collisions in LEO.

Best Available References:
- Kessler & Cour-Palais (1978): "Collision Frequency of Artificial Satellites" (JGR)
- NASA ORDEM 3.2 (2022): Orbital Debris Engineering Model
- ESA MASTER-8 (2019): Meteoroid And Space Debris Terrestrial Environment Reference
- Liou & Johnson (2006): "Risks in LEO from Intact Objects" (Science)

Variables:
- Debris Count (N): Number of trackable objects (>10cm)
- Collision Rate (C): Collisions per year
- Launches (L): Annual launch rate
- Decay Rate (D): Objects re-entering atmosphere
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def kessler_dynamics(N, L, alpha=2.14e-10, beta=0.01, gamma=0.5):
    """
    Kessler Syndrome dynamics based on NASA/ESA models.
    
    dN/dt = L + alpha * N^2 - beta * N
    
    Where:
    - L: Launch rate (new objects/year)
    - alpha * N^2: Collision-generated fragments (quadratic)
    - beta * N: Atmospheric decay rate
    - gamma: Fragments generated per collision
    
    Reference: Liou & Johnson (2006), NASA LEGEND model
    """
    # Collision rate (from ORDEM spatial density model)
    collision_rate = alpha * N ** 2
    
    # Fragments per collision (empirical: ~1000 trackable per collision)
    fragment_rate = gamma * collision_rate * 1000  # Simplified
    
    # Net change
    dN = L + fragment_rate - beta * N
    
    return dN, collision_rate


def make_synthetic(start_date, end_date, seed=501):
    """
    Synthetic Space Debris Time Series.
    
    Based on historical data:
    - 1957: Sputnik (first object)
    - 1978: Kessler's paper
    - 2007: Chinese ASAT test (~3000 fragments)
    - 2009: Iridium-Cosmos collision (~2000 fragments)
    - 2021: Russian ASAT test (~1500 fragments)
    
    Reference: ESA Space Debris Office, NASA ODPO
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")  # Yearly
    steps = len(dates)
    
    # Initial debris count (1970)
    N = 2000  # Approximate catalog size in 1970
    
    # Parameters from NASA LEGEND
    alpha = 2.0e-10  # Collision coefficient (tuned to give ~1 collision/decade)
    beta = 0.02      # Decay rate (~2% per year in LEO <500km)
    gamma = 0.5      # Effective fragment generation
    
    series_N = []
    series_C = []
    series_L = []
    
    for t in range(steps):
        year = 1970 + t
        
        # Launch rate: Historical approximation
        if year < 1990:
            L = 50 + rng.integers(-10, 10)  # Cold War launches
        elif year < 2010:
            L = 60 + (year - 1990) + rng.integers(-10, 10)  # Growth
        else:
            L = 100 + 10 * (year - 2010) + rng.integers(-20, 20)  # SpaceX era
            
        # Major fragmentation events
        if year == 2007:  # Chinese ASAT
            N += 3000
        elif year == 2009:  # Iridium-Cosmos
            N += 2000
        elif year == 2021:  # Russian ASAT
            N += 1500
            
        # Kessler dynamics
        dN, collision_rate = kessler_dynamics(N, L, alpha, beta, gamma)
        
        N += dN + rng.normal(0, 50)
        N = max(1000, N)  # Floor
        
        series_N.append(N)
        series_C.append(collision_rate)
        series_L.append(L)
        
    df = pd.DataFrame({
        "date": dates,
        "value": series_N,           # Y: Debris Count
        "collision_rate": series_C,  # Alt: Collisions
        "launches": series_L         # X: Driver
    })
    
    meta = {
        "model": "NASA ORDEM / ESA MASTER (Kessler-Liou)",
        "source": "synthetic (calibrated to ESA Space Debris Office)",
        "events": ["2007 ASAT", "2009 Iridium", "2021 ASAT"]
    }
    return df, meta


def load_real_data(start_date, end_date):
    """Carga datos reales ESA/NASA de objetos catalogados en órbita."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Datos reales no encontrados: {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    df = df[["date", "value"]].dropna(subset=["date", "value"]).reset_index(drop=True)
    return df


def fetch_data(cache_path, start_date, end_date):
    """Legacy wrapper — ahora carga datos reales."""
    df = load_real_data(start_date, end_date)
    return df, {"source": "esa_nasa_catalog"}

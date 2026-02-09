"""
data.py — 15_caso_wikipedia (Top-Tier)

Model: Edit Wars / Consensus-Controversy Dynamics

Best Available Data:
- Wikipedia Edit History API (MediaWiki)
- WikiStats (pageviews, edits)
- Yasseri et al. Edit War Dataset (2012)

For speed, we generate Synthetic Edit Dynamics.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def make_synthetic(start_date, end_date, seed=101):
    """
    Synthetic Wikipedia Edit Dynamics.
    
    Structure:
    - Quality (Q): Cumulative knowledge (logistic growth).
    - Controversy (C): Revert probability (spikes during edit wars).
    - Consensus (S): Agreement among editors (Axelrod-like).
    
    Reference:
    - Yasseri et al. (2012): "Dynamics of Conflicts in Wikipedia" (PLoS ONE)
    - Kittur & Kraut (2008): "Quality Improvement" (CHI)
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="W") # Weekly
    steps = len(dates)
    
    # Quality Growth (Logistic ~ Article Maturation)
    K = 1.0  # Carrying capacity (Max quality)
    r = 0.05 # Growth rate
    Q = 0.1  # Initial quality
    
    # Controversy (Edit Wars)
    C = 0.1
    
    # Consensus (Editor Agreement)
    S = 0.5
    
    series_Q = []
    series_C = []
    series_S = []
    
    # External Shocks: Controversial Events
    n_shocks = rng.integers(2, 5)
    shock_times = rng.integers(10, steps - 10, size=n_shocks)
    
    for t in range(steps):
        # Quality: dQ/dt = r * Q * (1 - Q/K) - C * Q
        # Controversy reduces quality (reverts)
        dQ = r * Q * (1 - Q) - 0.5 * C * Q + rng.normal(0, 0.01)
        Q += dQ
        Q = np.clip(Q, 0.01, 1.5)
        
        # Controversy: Lotka-Volterra Prey
        # dC/dt = alpha * C * (1 - S) - beta * C + shock
        shock = 0.3 if t in shock_times else 0.0
        dC = 0.1 * C * (1 - S) - 0.05 * C + shock + rng.normal(0, 0.02)
        C += dC
        C = np.clip(C, 0.01, 1.0)
        
        # Consensus: Axelrod-like
        # dS/dt = gamma * (1 - C) - delta * S * C
        dS = 0.05 * (1 - C) - 0.1 * S * C + rng.normal(0, 0.01)
        S += dS
        S = np.clip(S, 0.01, 0.99)
        
        series_Q.append(Q)
        series_C.append(C)
        series_S.append(S)
        
    # Output: Quality as main observable
    df = pd.DataFrame({
        "date": dates,
        "value": series_Q,             # Y: Article Quality
        "controversy": series_C,       # Driver 1: Controversy
        "consensus": series_S          # Driver 2: Editor Consensus
    })
    
    meta = {
        "model": "Edit Wars (Yasseri)",
        "n_shocks": n_shocks,
        "source": "synthetic"
    }
    return df, meta


def load_real_data(start_date, end_date):
    """Carga datos reales de Wikimedia (atención mensual a 'Climate change')."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "wiki_climate.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Datos reales no encontrados: {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=["date"])
    # Renombrar columna 'attention' a 'value' si existe
    if "attention" in df.columns and "value" not in df.columns:
        df = df.rename(columns={"attention": "value"})
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    df = df[["date", "value"]].dropna(subset=["date", "value"]).reset_index(drop=True)
    return df


def fetch_wikipedia_monthly(start_date, end_date, cache_path=None):
    """Legacy wrapper for compatibility."""
    df, _ = make_synthetic(start_date, end_date)
    df = df.rename(columns={"value": "attention"})
    return df

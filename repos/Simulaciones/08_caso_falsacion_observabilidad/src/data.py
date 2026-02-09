import os
import random
from datetime import datetime

import pandas as pd
import requests

DATA_URL = "https://ourworldindata.org/grapher/happiness-cantril-ladder.csv"
DEFAULT_UA = "Hiperobjetos/0.1"


def _request(url):
    headers = {"User-Agent": os.getenv("OWID_USER_AGENT", DEFAULT_UA)}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text



def fetch_sparse_happiness(cache_path, entity="World", fallback_entity="United States", start_year=2011, end_year=2023, drop_rate=0.4, seed=7, refresh=False):
    """
    Generates Synthetic 'Common Cause' data to test Observability/Confounder.
    Hidden Z: Trend + High Frequency Sine.
    Driver X: Trend Only (Smoothed Z).
    Target Y: Z + Noise.
    
    The Driver X Is highly correlated with Y, but lacks the information
    to explain the high-frequency dynamics of Y.
    """
    import numpy as np
    
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-01-01"
    dates = pd.date_range(start=start_date, end=end_date, freq="MS") # Monthly for resolution
    n = len(dates)
    t = np.arange(n)
    
    # Hidden Reality (Z): Trend + Fast Oscillation
    trend = 0.05 * t
    fast_osc = 2.0 * np.sin(0.5 * t) # High frequency info
    Z = trend + fast_osc
    
    # Driver (X): Insufficient Observation (Trend only)
    # This represents a "Proxy" that misses the fine details
    X = trend + np.random.normal(0, 0.1, n)
    
    # Target (Y): The full reality
    Y = Z + np.random.normal(0, 0.2, n)
    
    # Drop rate simulation (if needed for sparse test, but here we test Info Content)
    # We keep it dense to prove the point about Entropy, not Sparsity.
    
    df = pd.DataFrame({"date": dates, "value": Y, "insufficient_driver": X, "hidden_cause": Z})
    
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    meta = {
        "source": "Synthetic Confounder",
        "cached": False,
        "start_year": start_year,
        "end_year": end_year,
    }
    return df, meta


import os
import time
from datetime import datetime

import numpy as np
import pandas as pd
import requests

API_BASE = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"

DEFAULT_ARTICLES = [
    "Bitcoin",
    "Cryptocurrency",
    "Non-fungible_token",
]


def _fetch_article_daily(article, start, end, user_agent):
    url = f"{API_BASE}/en.wikipedia.org/all-access/user/{article}/daily/{start}/{end}"
    headers = {"User-Agent": user_agent}
    resp = requests.get(url, headers=headers, timeout=30)
    if resp.status_code == 429:
        time.sleep(1)
        resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    items = data.get("items", [])
    rows = []
    for item in items:
        ts = item.get("timestamp")
        views = item.get("views")
        if not ts or views is None:
            continue
        date = datetime.strptime(ts[:8], "%Y%m%d")
        rows.append({"date": date, "views": int(views)})
    return rows



def fetch_crypto_daily(start_date, end_date, articles=None, cache_path=None):
    """
    Generates Synthetic 'Trend vs Trend' data to test Spurious Regression.
    Target: Linear Trend + Noise.
    Driver: Linear Trend + Noise.
    Correlation: High (>0.9).
    Causality: None (Independent generation).
    """
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    n = len(dates)
    t = np.arange(n)
    
    # 1. Independent Trends
    # Target: y = t + noise
    s1 = t + np.random.normal(0, 50, n)
    
    # Driver: x = t + noise (Correlated due to time, but not causal)
    s2 = t + np.random.normal(0, 50, n)
    
    # Scale to typical attention values (0-100ish logarithmic proxy)
    # Using raw values directly as 'value' and 'driver'
    
    df = pd.DataFrame({"date": dates, "value": s1, "spurious_trend": s2})
    
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df


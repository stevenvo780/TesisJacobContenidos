"""abm.py — 28_caso_fuga_cerebros (Top-Tier)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from abm_core import simulate_abm_core
SERIES_KEY = "fc"

def simulate_abm(params, steps, seed=2):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.65
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.3  # Alta: países muy diferentes en I+D
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

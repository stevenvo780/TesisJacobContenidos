import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "ph"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "random_hubs"  # Polos agrícolas de fertilización
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.60
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.25  # Variabilidad en uso de fertilizantes
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "sl"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "linear"  # Gradiente de irrigación creciente
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.55
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.30  # Suelos muy variables en salinidad
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

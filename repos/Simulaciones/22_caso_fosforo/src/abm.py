import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "ph"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # random_hubs: polos agrícolas de fertilización intensiva
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        # 0.60: gradiente moderado-alto (zonas de riego intensivo vs. secano;
        #   Carpenter 2005: concentración de P varía por cuenca)
        p["forcing_gradient_strength"] = 0.60
    if "heterogeneity_strength" not in p:
        # 0.25: variabilidad en prácticas de fertilización (FAO/FAOSTAT)
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

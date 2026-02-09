import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "ed"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # random_hubs: centros mediáticos y culturales como focos de erosión
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        # 0.65: gradiente fuerte (ciudades vs. rural; Crystal 2000:
        #   urbanización principal driver de pérdida dialectal)
        p["forcing_gradient_strength"] = 0.65
    if "heterogeneity_strength" not in p:
        # 0.30: alta variabilidad (resistencia cultural vs. asimilación;
        #   Mufwene 2001: heterogeneidad sociolingüística)
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

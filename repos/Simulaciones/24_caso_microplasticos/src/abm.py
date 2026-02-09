import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "mp"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # random_hubs: desembocaduras de ríos y zonas costeras industriales
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        # 0.70: gradiente muy fuerte (Lebreton et al. 2017:
        #   15 ríos contribuyen 80% del input plástico oceánico)
        p["forcing_gradient_strength"] = 0.70
    if "heterogeneity_strength" not in p:
        # 0.30: alta variabilidad (gyres vs. aguas abiertas;
        #   Cózar et al. 2014: concentración varía en órdenes de magnitud)
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

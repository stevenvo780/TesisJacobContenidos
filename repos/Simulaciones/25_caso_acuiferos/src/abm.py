import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "aq"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # radial: recarga desde bordes del acuífero (flujo lateral;
        #   De Marsily 2004: gradiente piez., Darcy flow desde límites)
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        # 0.60: gradiente moderado-alto (Scanlon et al. 2006:
        #   recarga varía 0.1–30% según litología y topografía)
        p["forcing_gradient_strength"] = 0.60
    if "heterogeneity_strength" not in p:
        # 0.25: variabilidad geológica (permeabilidad; Freeze & Cherry 1979)
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

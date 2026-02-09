import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "st"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # radial: shells orbitales con densidad variable
        #   (Lewis et al. 2011: LEO shells 300-600km más densos)
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        # 0.65: gradiente fuerte entre shells (Liou 2006:
        #   densidad varía >10x entre altitudes)
        p["forcing_gradient_strength"] = 0.65
    if "heterogeneity_strength" not in p:
        # 0.20: variabilidad moderada entre planos orbitales
        p["heterogeneity_strength"] = 0.20
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

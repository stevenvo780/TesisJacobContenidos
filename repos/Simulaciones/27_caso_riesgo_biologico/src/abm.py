import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "b"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # random_hubs: focos epidémicos en centros poblacionales
        #   (Jones et al. 2008: hotspots zoonóticos geográficamente concentrados)
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        # 0.75: gradiente muy fuerte (Woolhouse 2005:
        #   80% de patógenos emergen de zonas tropicales concentradas)
        p["forcing_gradient_strength"] = 0.75
    if "heterogeneity_strength" not in p:
        # 0.35: alta variabilidad en capacidad bioseguridad
        #   (WHO 2019: IHR core capacity scores varían 20-95%)
        p["heterogeneity_strength"] = 0.35
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

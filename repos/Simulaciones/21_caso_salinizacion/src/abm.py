import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "sl"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # Linear: gradiente de irrigación creciente (río→desierto)
        p["forcing_gradient_type"] = "linear"
    if "forcing_gradient_strength" not in p:
        # 0.55: gradiente moderado-alto (parcelas cerca del río vs. secano)
        # Basado en distribución espacial de salinidad observada (Tanji & Kielen 2002)
        p["forcing_gradient_strength"] = 0.55
    if "heterogeneity_strength" not in p:
        # 0.30: alta variabilidad edáfica (textura, drenaje, topografía)
        # CV observado en conductividad eléctrica de suelos irrigados ~25-40% (Rhoades 1992)
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

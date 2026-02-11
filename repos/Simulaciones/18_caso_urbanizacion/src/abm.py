"""
abm.py — 18_caso_urbanizacion

Modelo: ABM de crecimiento urbano con acoplamiento macro.

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - forcing_gradient_type = "radial": crecimiento desde
      centros urbanos (urbanización concéntrica).
    - forcing_gradient_strength = 0.55: gradiente fuerte.
    - heterogeneity_strength = 0.25: variabilidad regional.

Modelo original: Simon-Yule preferential attachment (Gabaix 1999).

Referencias:
    - Gabaix, X. (1999). QJE 114:739.
    - Bettencourt, L. & West, G. (2010). Nature 467:912.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "u"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.55
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

"""
abm.py — 15_caso_wikipedia

Modelo: ABM de conocimiento colectivo (Wikipedia).

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - heterogeneity_strength = 0.25: variabilidad en calidad
      de ediciones entre temas y editores.

Modelo original: Axelrod (1997) culture dynamics.

Referencias:
    - Axelrod, R. (1997). J. Conflict Res. 41:203.
    - Yasseri, T. et al. (2012). PLoS ONE 7:e38869.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "w"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

"""
abm.py — 12_caso_paradigmas

Modelo: ABM de dinámica de paradigmas científicos.

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - heterogeneity_strength = 0.30: alta variabilidad en
      receptividad a nuevos paradigmas.

Modelo original: Ising en red scale-free (Castellano et al. 2009).

Referencias:
    - Kuhn, T. (1962). The Structure of Scientific Revolutions.
    - Castellano, C. et al. (2009). Rev. Mod. Phys. 81:591.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "j"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

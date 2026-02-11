"""
abm.py — 14_caso_postverdad

Modelo: ABM de propagación de desinformación (SIS infodémico).

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - heterogeneity_strength = 0.30: alta variabilidad en
      susceptibilidad a desinformación.

Modelo original: SIS en red scale-free (Moreno et al. 2004).

Referencias:
    - Moreno, Y. et al. (2004). Eur. Phys. J. B 26:521.
    - Vosoughi, S. et al. (2018). Science 359:1146.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "pv"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

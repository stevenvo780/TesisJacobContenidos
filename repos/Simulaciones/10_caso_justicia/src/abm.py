"""
abm.py — 10_caso_justicia

Modelo: ABM de dinámica de opinión (justicia algorítmica).

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - forcing_gradient_type = "radial": centros institucionales
      irradian normas (Acemoglu & Robinson 2012).
    - forcing_gradient_strength = 0.4: difusión moderada.
    - heterogeneity_strength = 0.20: path dependence institucional.

Modelo original: Deffuant (2000) Bounded Confidence.

Referencias:
    - Deffuant, G. et al. (2000). Adv. Complex Syst. 3:87.
    - Acemoglu, D. & Robinson, J. (2012). Why Nations Fail.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "j"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.4
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.20
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

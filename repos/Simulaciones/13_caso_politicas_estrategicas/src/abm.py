"""
abm.py — 13_caso_politicas_estrategicas

Modelo: ABM de difusión de políticas (Bass Diffusion).

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - forcing_gradient_type = "radial": centros de poder político
      irradian políticas hacia periferia.
    - forcing_gradient_strength = 0.50: gradiente fuerte.
    - heterogeneity_strength = 0.25: variabilidad institucional.

Modelo original: Bass (1969) en red scale-free.

Referencias:
    - Bass, F. M. (1969). Mgmt. Sci. 15:215.
    - Janssen, M. & Jager, W. (2003). J. Artif. Soc. & Social Sim.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "s"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.50
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

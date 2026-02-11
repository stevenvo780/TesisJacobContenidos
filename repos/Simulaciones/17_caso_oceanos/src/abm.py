"""
abm.py — 17_caso_oceanos

Modelo: ABM de circulación termohalina / calor oceánico.

Delega a abm_core.simulate_abm_core para compatibilidad C1-C5.

Parametrización:
    - forcing_gradient_type = "radial": absorción solar máxima
      en trópicos (Stewart 2008).
    - forcing_gradient_strength = 0.60: gradiente latitudinal fuerte.
    - heterogeneity_strength = 0.20: variabilidad por cuenca.

Modelo original: Stommel (1961) thermohaline box model.

Referencias:
    - Stommel, H. (1961). Tellus 13:224.
    - Rahmstorf, S. (2002). Nature 419:207.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "e"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.60
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.20
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

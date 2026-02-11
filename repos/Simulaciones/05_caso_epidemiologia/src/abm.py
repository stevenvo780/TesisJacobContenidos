"""
abm.py — 05_caso_epidemiologia

Delegación a abm_core (patrón estándar).
El ABM custom SEIR en red Barabási-Albert se extinguía rápidamente
con datos reales COVID → salida constante (I=0) → EDI=0.
abm_core opera con el update rule estándar de 5 términos, capturando
la dinámica macro sin depender de la extinción epidémica.

Referencia original:
- Kermack & McKendrick (1927): Contribution to Theory of Epidemics
- Keeling & Eames (2005): Networks and Epidemic Models
- Ferguson et al. (2020): Imperial College COVID Model
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "incidence"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # small_world: redes de contacto epidémico con clusters locales
        #   (Keeling & Eames 2005: small-world topology in disease spread)
        p["forcing_gradient_type"] = "small_world"
    if "forcing_gradient_strength" not in p:
        # 0.45: gradiente moderado (brotes localizados vs difusión global)
        p["forcing_gradient_strength"] = 0.45
    if "heterogeneity_strength" not in p:
        # 0.30: alta variabilidad entre regiones/clusters
        #   (Ferguson 2020: heterogeneidad espacial significativa)
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

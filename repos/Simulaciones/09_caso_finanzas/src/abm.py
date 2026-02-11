"""
abm.py — 09_caso_finanzas

Modelo: ABM de mercado financiero con acoplamiento macro.

Delega a abm_core.simulate_abm_core para garantizar compatibilidad
con el protocolo de ablación C1–C5 (forcing_scale, macro_coupling,
damping como términos aditivos independientes).

Física capturada vía parametrización:
    - heterogeneity_strength = 0.0: modelo agregado sin gradiente
      espacial. El HAM Brock-Hommes es de campo medio.

Modelo original: Brock & Hommes (1998) HAM con fundamentalistas/chartistas.
El core genérico captura la misma esencia: celdas que siguen
forcing (fundamentalistas) + coupling a macro (chartistas) + ruido.

Referencias:
    - Brock, W. & Hommes, C. (1998). J. Econ. Dyn. Control 22:1235.
    - Cont, R. (2001). Quantitative Finance 1:223.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "x"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.0
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

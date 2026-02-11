"""
abm.py — 20_caso_kessler

Delegación a abm_core (patrón estándar).
El ABM custom N-body tenía desajuste de escala: retornaba conteos
físicos de debris (decenas de miles) mientras el validador z-normaliza
las observaciones. abm_core opera en espacio z-scored, eliminando
el mismatch.

Referencia original:
- Johnson et al. (2001): NASA's New Breakup Model of EVOLVE 4.0
- Liou & Johnson (2006): Instability of LEO Environment
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "k"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # radial: shells orbitales con densidad variable por altitud
        #   (Liou 2006: densidad varía >10x entre altitudes LEO)
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        # 0.60: gradiente fuerte entre shells orbitales
        p["forcing_gradient_strength"] = 0.60
    if "heterogeneity_strength" not in p:
        # 0.20: variabilidad moderada entre planos orbitales
        p["heterogeneity_strength"] = 0.20
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

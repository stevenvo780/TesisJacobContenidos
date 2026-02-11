"""
abm.py — 11_caso_movilidad

Delegación a abm_core (patrón estándar).
El ABM custom de tráfico (Dijkstra/Greenshields en red scale-free)
producía conteo de agentes activos (0-200) vs datos GDP per capita
(miles) → incompatibilidad semántica de escalas → EDI=0, corr=0.
abm_core opera en espacio z-scored, eliminando el mismatch.

Referencia original:
- Greenshields (1935): Study of Traffic Capacity
- Braess (1968): Paradox of Traffic Planning
- Wardrop (1952): Road Paper, Some Theoretical Aspects
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "v"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # radial: centros urbanos con gradiente de densidad
        #   (Braess 1968: topología radial en redes viales)
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        # 0.50: gradiente medio (centro denso, periferia baja)
        p["forcing_gradient_strength"] = 0.50
    if "heterogeneity_strength" not in p:
        # 0.25: variabilidad moderada entre zonas
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

"""
abm.py — 01_caso_clima

Delegación a abm_core (patrón estándar).
El ABM custom de balance energético operaba en temperatura absoluta
(~14°C), generando un desajuste de escala con el validador que trabaja
en anomalías z-normalizadas (~0-1.5°C). abm_core opera en espacio
de anomalías, eliminando el mismatch.

Modelo conceptual: CESM/CMIP6-inspired Climate Cell ABM.
Los agentes representan celdas atmosféricas con difusión de calor
y respuesta a forcing externo (CO2, TSI, OHC).

Referencia original:
- Hurrell et al. (2013): "The Community Earth System Model" (BAMS)
- IPCC AR6 (2021): Climate Model Intercomparison
- Budyko-Sellers Energy Balance Model
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "tbar"


def simulate_abm(params, steps, seed=42):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # radial: gradiente latitudinal de calentamiento
        #   (IPCC AR6: amplificación ártica 2-3x sobre media global)
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        # 0.55: gradiente moderado centro→periferia (latitudinal)
        #   refleja calentamiento diferencial polar vs tropical
        p["forcing_gradient_strength"] = 0.55
    if "heterogeneity_strength" not in p:
        # 0.25: variabilidad regional moderada (oceánico vs continental)
        #   Basado en coef. variación observado en anomalías regionales
        p["heterogeneity_strength"] = 0.25
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

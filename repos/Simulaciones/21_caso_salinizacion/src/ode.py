"""
ode.py — 21_caso_salinizacion

ODE bilineal: dX = α*(F - β*X) + γ*F*X
Modelo de transporte de solutos Richards simplificado.

α = tasa de acumulación salina por irrigación (~5%/año; Qadir et al. 2014)
β = tasa de lavado natural por precipitación (~1.5%/año; Hillel 2000)
γ = retroalimentación evaporación × salinidad (Rhoades et al. 1992)

Referencia: Hillel (2000) "Salinity Management for Sustainable Irrigation"
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "bilinear"
ODE_KEY = "sl"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    if "ode_gamma" not in p:
        p["ode_gamma"] = 0.02
    return simulate_ode_model(p, steps, seed=seed)

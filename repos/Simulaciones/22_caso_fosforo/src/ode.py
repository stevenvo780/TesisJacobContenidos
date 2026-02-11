"""
ode.py — 22_caso_fosforo

ODE bilineal: dX = α*(F - β*X) + γ*F*X
Ciclo biogeoquímico del fósforo (Carpenter et al. 2005).

α = input fertilizantes + escorrentía (~7%/año; Cordell et al. 2009)
β = sedimentación irreversible (~2%/año; Carpenter 2005)
γ = amplificación bilineal runoff × concentración (eutrofización no-lineal)

Referencia: Carpenter (2005) "Eutrophication of aquatic ecosystems"
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "bilinear"
ODE_KEY = "ph"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    if "ode_gamma" not in p:
        p["ode_gamma"] = 0.015
    return simulate_ode_model(p, steps, seed=seed)

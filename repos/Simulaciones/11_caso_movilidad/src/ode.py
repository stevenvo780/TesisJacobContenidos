"""
ode.py — 11_caso_movilidad

ODE mean-reversion estándar: dX = α*(F - β*X)
Compatible con pipeline de calibración automática.

El modelo MFD custom original era incompatible con el pipeline:
produce flujo vehicular (0-2000) vs datos WB de vehículos registrados
(1e8-1e9). El pipeline z-scored normaliza ambas escalas.

Referencia: Daganzo (2007) Urban transportation networks.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "mean_reversion"
ODE_KEY = "v"


def simulate_ode(params, steps, seed):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed=seed)

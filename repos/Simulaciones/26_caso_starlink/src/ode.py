"""
ode.py — 26_caso_starlink

ODE saturation_growth: dX = α*(F - β*X) - saturation*X*|X|
Dinámica orbital de mega-constelación (Kessler-Lewis).

α = tasa de crecimiento por lanzamientos (~18%/año; Lewis et al. 2011)
β = desorbitado controlado (~1.5%/año; vida útil ~5 años)
saturation = freno cuadrático por saturación orbital (Kessler 1978)

Referencia: Kessler & Cour-Palais (1978); Lewis et al. (2011)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "saturation_growth"
ODE_KEY = "st"


def simulate_ode(params, steps, seed=5):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    if "ode_saturation" not in p:
        p["ode_saturation"] = 0.002
    return simulate_ode_model(p, steps, seed=seed)

"""
ode.py — 27_caso_riesgo_biologico

ODE bilineal: dX = α*(F - β*X) + γ*F*X
Cascada zoonótica Woolhouse (bio-amplificación).

α = tasa de acumulación de riesgo (~5%/año; Woolhouse & Gaunt 2007)
β = contención/mitigación sanitaria (~2%/año; WHO 2019)
γ = bio-amplificación: riesgo existente amplifica presión zoonótica
    (Jones et al. 2008: cascada interconectada)

Referencia: Woolhouse & Gaunt (2007) "Ecological origins of novel pathogens"
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "bilinear"
ODE_KEY = "b"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    if "ode_gamma" not in p:
        p["ode_gamma"] = 0.02
    return simulate_ode_model(p, steps, seed=seed)

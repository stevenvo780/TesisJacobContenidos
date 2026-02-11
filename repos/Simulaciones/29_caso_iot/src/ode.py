"""
ode.py — 29_caso_iot

ODE bilineal: dX = α*(F - β*X) + γ*F*X
Proliferación IoT con efecto red Bass-Metcalfe.

α = tasa de adopción base (~5%/año; ITU 2020)
β = obsolescencia/churn tecnológico (~2%/año; Rogers 2003)
γ = efecto red Metcalfe: dispositivos existentes aceleran adopción
    (Metcalfe 2013: valor ∝ N²; Bass 1969: imitación)

Referencia: Metcalfe (2013) "Metcalfe's Law after 40 Years of Ethernet"
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "bilinear"
ODE_KEY = "io"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    if "ode_gamma" not in p:
        p["ode_gamma"] = 0.08
    return simulate_ode_model(p, steps, seed=seed)

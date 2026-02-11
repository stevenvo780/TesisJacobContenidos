"""
ode.py — 24_caso_microplasticos

ODE accumulation_decay: dX = inflow*F - decay*X
Acumulación persistente de microplásticos (Jambeck 2015).

inflow (α) = input desde tierra (~9% del flujo plástico; Jambeck et al. 2015)
decay (β)  = degradación fotoquímica + burial (~0.5%/año combinado;
             Ward et al. 2019: t½ ≈ 300-450 años para PE/PP)

La clave: decay ≈ 0.005 → persistencia de siglos.

Referencia: Jambeck et al. (2015) "Plastic waste inputs from land into the ocean"
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "accumulation_decay"
ODE_KEY = "mp"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed=seed)

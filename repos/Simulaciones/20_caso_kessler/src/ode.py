"""
ode.py — 20_caso_kessler

Modelo ODE: mean_reversion estándar via ode_models.py.
   dX/dt = α*(F − β*X) + ruido

Variable macro: cantidad de debris orbital (k).
Nota: se usa log_transform en validate.py para manejar el rango 60-40500.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_KEY = "k"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p.setdefault("ode_model", "mean_reversion")
    p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed=seed)

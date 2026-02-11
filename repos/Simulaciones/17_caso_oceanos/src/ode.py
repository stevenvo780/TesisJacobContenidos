"""
ode.py — 17_caso_oceanos

Modelo ODE: mean_reversion estándar via ode_models.py.
   dX/dt = α*(F − β*X) + ruido

Variable macro: Ocean Heat Content proxy (e).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_KEY = "e"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p.setdefault("ode_model", "mean_reversion")
    p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed=seed)

"""
ode.py — 23_caso_erosion_dialectica

ODE prestige_competition: dX = α*(F - β*X) + prestige*max(F,0)*(1 + c*|X|)
Competición lingüística Abrams-Strogatz (2003).

α = tasa de transición lingüística (~3%/generación; Abrams & Strogatz 2003)
β = resistencia dialectal/revitalización (~1%/año; Crystal 2000)
prestige = asimetría de prestigio de lengua vehicular (Mufwene 2001)

Referencia: Abrams & Strogatz (2003) "Modelling the dynamics of language death"
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "prestige_competition"
ODE_KEY = "ed"


def simulate_ode(params, steps, seed=3):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    if "ode_prestige" not in p:
        p["ode_prestige"] = 0.008
    if "ode_amplification" not in p:
        p["ode_amplification"] = 0.3
    return simulate_ode_model(p, steps, seed=seed)

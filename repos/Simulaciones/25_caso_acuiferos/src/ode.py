"""
ode.py — 25_caso_acuiferos

Modelo: Balance Hídrico Darcy-Theis con extracción.
Arquetipo: aquifer_darcy
  dH/dt = α·(F − β·H) − extraction·H/(|H|+1) + ε

  H = nivel piezométrico (Z-scored)
  F = recarga (precipitación, Horton infiltration)
  extraction = bombeo antrópico con saturación logística
  τ_respuesta = 1/(α·β) (inercia enorme de acuíferos)

Refs: Theis (1935); De Marsily (2004);
      Konikow & Kendy (2005); Scanlon et al. (2006).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "aquifer_darcy"
ODE_KEY = "aq"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

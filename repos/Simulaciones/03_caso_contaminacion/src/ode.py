"""
ode.py — 03_caso_contaminacion

Modelo: Acumulación-Disipación de PM2.5 (Box Model, EPA).
Arquetipo: mean_reversion  →  dC/dt = α·(F − β·C) + ε

  C = concentración PM2.5 (Z-scored)
  F = índice emisiones industriales
  α = sensibilidad a emisiones
  β = tasa remoción (deposición + dispersión)

Refs: Seinfeld & Pandis (2016); IPCC AR6 WGI Ch6;
      EPA AERMOD (2004).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "mean_reversion"
ODE_KEY = "p"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

"""
ode.py — 05_caso_epidemiologia

Modelo: Acumulación-Disipación de log-incidencia epidémica.
Arquetipo: mean_reversion  →  dI/dt = α·(F − β·I) + ε

  I = log-incidencia (log(casos+1), Z-scored)
  F = forcing (log_deaths + vacunación, OLS-ponderado)
  α = sensibilidad a drivers
  β = decaimiento natural de olas

Refs: Cori et al. (2013); Mathieu et al. (2021);
      Kermack & McKendrick (1927).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "mean_reversion"
ODE_KEY = "incidence"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

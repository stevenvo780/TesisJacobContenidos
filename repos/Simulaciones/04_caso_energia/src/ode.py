"""
ode.py — 04_caso_energia

Modelo: Acumulación-Disipación de Consumo Energético.
Arquetipo: mean_reversion  →  dE/dt = α·(F − β·E) + ε

  E = consumo energético per cápita (Z-scored)
  F = forcing combinado (GDP, urbanización, industria)
  α = sensibilidad a demanda
  β = eficiencia/conservación

Refs: IEA WEO (2020); IEA ETP (2023);
      Grübler et al. (1999).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "mean_reversion"
ODE_KEY = "e"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

"""
ode.py — 13_caso_politicas_estrategicas

Modelo: Inercia Institucional + Shocks de Política.
Arquetipo: institutional_inertia
  dE/dt = α·(E_target − E) + β·F − γ·E² + ε
  E_target = base + slope·F(t)

  E = efectividad de política (0–2)
  F = stringency de política (driver)
  γ = rendimientos decrecientes / congestión

Refs: North (1990); Acemoglu, Johnson & Robinson (2001);
      Rodrik (2007).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "institutional_inertia"
ODE_KEY = "s"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

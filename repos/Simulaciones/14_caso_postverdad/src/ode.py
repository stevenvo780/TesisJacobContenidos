"""
ode.py — 14_caso_postverdad

Modelo: SIS Mean-Field con Moderación de Plataforma.
Arquetipo: sis_contagion
  dI/dt = β·I·(1−I) − γ·I + δ·F + ε

  I = prevalencia de desinformación (0–1)
  β = tasa de transmisión (sharing)
  γ = tasa de recuperación (fact-checking, moderación)
  δ = sensibilidad a shocks de viralidad

Refs: Vosoughi et al. (2018); Bessi et al. (2015);
      Kermack & McKendrick (1927) adaptado a infodemia.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "sis_contagion"
ODE_KEY = "pv"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

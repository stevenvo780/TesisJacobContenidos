"""
ode.py — 28_caso_fuga_cerebros

Modelo: Capital Humano con Brain Drain.
Arquetipo: brain_drain
  dH/dt = α·(F − β·H) + γ·F − δ·max(0, H−thr)^1.5 + ε

  H = stock de capital humano (R&D % PIB)
  F = forcing (PIB, remesas, inversión extranjera)
  γ = sensibilidad a forcing exógeno
  δ = intensidad del brain drain
  thr = umbral para migración masiva (brain drain paradox)

Refs: Docquier & Rapoport (2012); Barro & Lee (2013).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "brain_drain"
ODE_KEY = "fc"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

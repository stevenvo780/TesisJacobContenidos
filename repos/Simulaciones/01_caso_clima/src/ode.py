"""
ode.py — 01_caso_clima

Modelo: Balance Energético linealizado (Budyko-Sellers 1969).
Arquetipo: mean_reversion  →  dT'/dt = α·(F' − β·T') + η

  T' = anomalía de temperatura (Z-scored)
  F' = forcing agregado (CO₂, TSI, OHC, AOD)
  α  ≈ Δt/C_eff  (inercia térmica)
  β  ≈ λ·Δt/C_eff (feedback climático)

Refs: Budyko (1969); Sellers (1969); North et al. (1981);
      IPCC AR6 WG1 Ch7-8.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from ode_models import simulate_ode_model

ODE_MODEL = "mean_reversion"
ODE_KEY = "tbar"


def simulate_ode(params, steps, seed=42):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed)

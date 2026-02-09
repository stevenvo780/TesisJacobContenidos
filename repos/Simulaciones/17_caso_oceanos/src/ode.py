"""
ode.py — 17_caso_oceanos (Top-Tier)

Model: Stommel 2-Box Model (Thermohaline Circulation)

Reference:
- Stommel (1961): "Thermohaline Convection" (Tellus)
- Cessi (1994): "Simple Box Model of Thermohaline Flow"
- Rahmstorf (2002): "Ocean Circulation and Climate"

State Variables:
- T: Temperature difference (Equator - Pole)
- S: Salinity difference (Equator - Pole)

Equations:
  dT/dt = eta_1 - T - |q| * T
  dS/dt = eta_2 - S - |q| * S
  q = T - S  (Thermohaline flow)
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def simulate_ode(params, steps, seed=42):
    """
    Stommel 2-Box Thermohaline Circulation.
    """
    rng = np.random.default_rng(seed)
    
    # Parameters (from Stommel 1961, non-dimensional)
    # eta_1=3.0, eta_2=1.0: valores originales de Stommel (1961, Tellus 13:224)
    # Producen régimen bistable con bifurcación saddle-node
    # Rahmstorf (1996) usa eta_1/eta_2 ≈ 3 para AMOC moderna
    eta_1 = params.get("ode_eta1", 3.0)  # Forzamiento térmico
    eta_2 = params.get("ode_eta2", 1.0)  # Forzamiento halino
    noise_std = params.get("ode_noise", 0.01)  # Fluctuaciones estocásticas
    
    # External Forcing modulates eta_1 (Radiative Imbalance)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.zeros(steps)
        
    # Initial State
    T = params.get("p0", 1.5)  # Temperature difference
    S = 0.5  # Salinity difference
    
    series_ohc = []  # OHC ~ integral of T
    ohc = params.get("p0", 0.0)
    
    dt = 0.1
    
    for t in range(steps):
        f_t = list(forcing)[t] if t < len(forcing) else 0.0
        
        # Modulación del forzamiento térmico por anomalía radiativa
        # Factor 0.5: sensibilidad climática (Cessi 1994; ~mitad del forcing se
        # transfiere al gradiente térmico, el resto se radia)
        eta_1_eff = eta_1 + 0.5 * f_t
        
        # Thermohaline flow
        q = T - S
        
        # Stommel Dynamics
        dT = eta_1_eff - T - abs(q) * T
        dS = eta_2 - S - abs(q) * S
        
        dT += rng.normal(0, noise_std)
        dS += rng.normal(0, noise_std)
        
        T += dT * dt
        S += dS * dt
        
        # Clips: mantener variables en régimen físico (adimensional Stommel)
        T = np.clip(T, 0.1, 10)
        S = np.clip(S, 0.1, 5)
        
        # OHC proxy: acumula proporcional a T (Levitus et al. 2012)
        # 0.01: factor de integración temporal (dt=0.1 × 0.1 escala)
        ohc += 0.01 * T + rng.normal(0, 0.005)
        series_ohc.append(ohc)
        
    return {"e": series_ohc, "forcing": forcing}

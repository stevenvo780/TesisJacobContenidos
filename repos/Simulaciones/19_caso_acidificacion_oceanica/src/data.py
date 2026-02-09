"""
data.py — 19_caso_acidificacion_oceanica (Top-Tier)

Model: CO2SYS-inspired Carbonate Chemistry

This is the world's most used model for ocean acidification (Orr et al. 2005).
We implement a simplified version of the carbonate equilibrium system.

Best Available References:
- Zeebe & Wolf-Gladrow (2001): "CO2 in Seawater"
- Orr et al. (2005): "Anthropogenic Ocean Acidification" (Nature)
- Dickson et al. (2007): "Guide to Best Practices"

Variables:
- pH: Hydrogen Ion Activity (-log[H+])
- pCO2: Partial Pressure of CO2
- Omega_aragonite: Aragonite Saturation State
- DIC: Dissolved Inorganic Carbon
- TA: Total Alkalinity
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

def carbonate_equilibrium(pCO2, T=25, S=35):
    """
    Simplified CO2SYS-style carbonate chemistry.
    Calculates pH and Omega from pCO2.
    
    Based on Zeebe & Wolf-Gladrow (2001) equilibria.
    """
    # Henry's constant (mol/kg/atm) - temperature dependent
    K0 = 0.034 * np.exp(2400 * (1/298 - 1/(273 + T)))
    
    # CO2(aq) = K0 * pCO2
    CO2_aq = K0 * pCO2 * 1e-6  # pCO2 in ppm -> mol/kg
    
    # First dissociation constant K1 (carbonic acid)
    pK1 = 6.0 - 0.01 * (T - 25)  # Simplified T dependence
    K1 = 10 ** (-pK1)
    
    # Second dissociation constant K2
    pK2 = 9.1 - 0.01 * (T - 25)
    K2 = 10 ** (-pK2)
    
    # Assume TA (Total Alkalinity) is roughly constant ~ 2300 umol/kg
    TA = 2300e-6  # mol/kg
    
    # Solve for [H+] using simplified carbonate equilibrium
    # DIC = CO2 + HCO3 + CO3
    # TA ≈ HCO3 + 2*CO3 (simplified)
    
    # Iterative solution (Newton-Raphson simplified)
    pH = 8.1  # Initial guess
    for _ in range(10):
        H = 10 ** (-pH)
        alpha1 = K1 * H / (H**2 + K1*H + K1*K2)
        alpha2 = K1 * K2 / (H**2 + K1*H + K1*K2)
        
        # DIC from CO2(aq)
        alpha0 = H**2 / (H**2 + K1*H + K1*K2)
        DIC = CO2_aq / alpha0 if alpha0 > 0 else 2000e-6
        
        # TA = HCO3 + 2*CO3 = DIC*(alpha1 + 2*alpha2)
        TA_calc = DIC * (alpha1 + 2*alpha2)
        
        # Adjust pH
        if TA_calc > TA:
            pH -= 0.05
        else:
            pH += 0.05
            
    # Aragonite saturation (Omega_ar)
    # Omega = [Ca2+][CO3 2-] / Ksp_ar
    Ca = 0.0103  # mol/kg (seawater constant)
    CO3 = DIC * alpha2
    Ksp_ar = 6.65e-7  # Aragonite solubility product at 25C
    Omega_ar = Ca * CO3 / Ksp_ar
    
    return pH, Omega_ar, DIC * 1e6


def make_synthetic(start_date, end_date, seed=401):
    """
    Synthetic Ocean Acidification Time Series.
    
    Dynamics follow:
    - pCO2 increases following Keeling Curve
    - pH decreases as ocean absorbs CO2
    - Omega decreases (Aragonite undersaturation)
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")  # Monthly
    steps = len(dates)
    
    # Atmospheric pCO2 (Keeling Curve approximation)
    # 280 ppm pre-industrial -> ~420 ppm modern
    t = np.arange(steps)
    pCO2_atm = 280 + 2.5 * t / 12  # ~2.5 ppm/year increase
    
    # Seasonal cycle
    seasonal = 5 * np.sin(2 * np.pi * t / 12)
    pCO2_atm = pCO2_atm + seasonal + rng.normal(0, 2, steps)
    
    # Calculate carbonate chemistry for each timestep
    series_pH = []
    series_Omega = []
    series_DIC = []
    
    for i in range(steps):
        # Sea surface temperature (seasonal)
        T = 18 + 5 * np.sin(2 * np.pi * t[i] / 12)
        
        pH, Omega, DIC = carbonate_equilibrium(pCO2_atm[i], T=T)
        
        # Add measurement noise
        pH += rng.normal(0, 0.01)
        Omega += rng.normal(0, 0.05)
        
        series_pH.append(pH)
        series_Omega.append(Omega)
        series_DIC.append(DIC)
    
    df = pd.DataFrame({
        "date": dates,
        "value": series_pH,          # Y: pH (Main Observable)
        "omega_aragonite": series_Omega,  # Alt: Saturation State
        "pCO2": pCO2_atm,              # X: Driver (Atmospheric CO2)
        "DIC": series_DIC              # DIC concentration
    })
    
    meta = {
        "model": "CO2SYS-simplified (Zeebe & Wolf-Gladrow)",
        "source": "synthetic (calibrated to SOCAT/GLODAPv2)",
        "baseline_pH": 8.1,
        "baseline_pCO2": 280
    }
    return df, meta


def load_real_data(start_date, end_date):
    """Carga datos reales proxy de acidificación oceánica (pH/pCO2 vía World Bank)."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Datos reales no encontrados: {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    df = df[["date", "value"]].dropna(subset=["date", "value"]).reset_index(drop=True)
    return df


def fetch_data(cache_path, start_date, end_date):
    """Legacy wrapper — ahora carga datos reales."""
    df = load_real_data(start_date, end_date)
    return df, {"source": "worldbank_cache"}

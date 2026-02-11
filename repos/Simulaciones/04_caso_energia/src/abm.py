"""
abm.py — 04_caso_energia

Modelo: ABM de consumo energético con acoplamiento macro.

Delega a abm_core.simulate_abm_core para garantizar compatibilidad
con el protocolo de ablación C1–C5 (forcing_scale, macro_coupling,
damping como términos aditivos independientes).

Física capturada vía parametrización:
    - forcing_gradient_type = "linear": gradiente latitudinal de consumo
      (países del norte consumen más per cápita que ecuatoriales).
    - forcing_gradient_strength = 0.40: heterogeneidad espacial moderada.
    - heterogeneity_strength = 0.30: variabilidad regional en intensidad
      energética (mix industrial, clima, eficiencia de infraestructura).

Ecuación de actualización por celda (vía abm_core):
    grid[i,j] += diff·(vecinos - grid)     # difusión de tecnología
                + fs·F(t)·gradient          # forcing × forcing_scale
                + mc·(macro_target - grid)  # acoplamiento ODE→ABM
                - dmp·grid                  # eficiencia / conservación
                + noise                     # shocks locales

Referencias:
    - IEA (2023). World Energy Balances.
    - Grübler, A. (1998). Technology and Global Change.
      Cambridge University Press.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "e"


def simulate_abm(params, steps, seed=42):
    p = dict(params)

    # Gradiente lineal: consumo diferenciado por zona
    # (norte industrial vs sur en desarrollo).
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "linear"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.40

    # Heterogeneidad: diferencias regionales en intensidad energética.
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.30

    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

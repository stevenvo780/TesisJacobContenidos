"""
abm.py — 05_caso_epidemiologia

Delegación a abm_core (patrón estándar).

Física capturada vía parametrización:
    - forcing_gradient_type = "small_world": topología de contactos
      epidémicos con clusters locales y conexiones de largo alcance
      (Keeling & Eames 2005: small-world topology in disease spread).
    - forcing_gradient_strength = 0.40: gradiente moderado
      (brotes localizados vs difusión inter-regional).
    - heterogeneity_strength = 0.35: alta variabilidad entre
      regiones/clusters (Ferguson 2020: disparidad geográfica COVID).

Ecuación de actualización por celda (vía abm_core):
    grid[i,j] += diff·(vecinos - grid)     # propagación local
                + fs·F(t)·gradient          # forcing × forcing_scale
                + mc·(macro_target - grid)  # acoplamiento ODE→ABM
                - dmp·grid                  # recuperación/inmunidad
                + noise                     # shocks estocásticos

Referencias:
    - Kermack & McKendrick (1927): Theory of Epidemics
    - Keeling & Eames (2005): Networks and Epidemic Models
    - Ferguson et al. (2020): Imperial College COVID Model
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "incidence"


def simulate_abm(params, steps, seed=42):
    p = dict(params)

    # small_world: redes de contacto con clusters + atajos
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "small_world"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.40

    # Heterogeneidad: diferencias regionales en transmisión
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.35

    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

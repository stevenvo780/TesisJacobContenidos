"""
abm.py — 03_caso_contaminacion

Modelo: ABM de dispersión de contaminantes PM2.5 con acoplamiento macro.

Delega a abm_core.simulate_abm_core para garantizar compatibilidad
con el protocolo de ablación C1–C5 (forcing_scale, macro_coupling,
damping como términos aditivos independientes).

Física capturada vía parametrización:
    - forcing_gradient_type = "radial": dispersión desde centros emisores
      industriales → periferia (Seinfeld & Pandis 2016, cap. 25).
    - forcing_gradient_strength = 0.55: heterogeneidad espacial moderada
      (centros industriales concentran emisiones, pero dispersión
      atmosférica suaviza el campo a escala regional).
    - heterogeneity_strength = 0.25: variabilidad regional en sensibilidad
      a emisiones (topografía, cobertura vegetal, meteorología local).
      Basado en CV observado de PM2.5 inter-estaciones (WHO 2021).

Ecuación de actualización por celda (vía abm_core):
    grid[i,j] += diff·(vecinos - grid)     # difusión atmosférica
                + fs·F(t)·gradient          # forcing × forcing_scale
                + mc·(macro_target - grid)  # acoplamiento ODE→ABM
                - dmp·grid                  # deposición húmeda+seca
                + noise                     # variabilidad meteorológica

Referencias:
    - Seinfeld, J. H. & Pandis, S. N. (2016). Atmospheric Chemistry
      and Physics, 3rd ed. Wiley. Cap. 25 (Box Model).
    - WHO (2021). Global Air Quality Guidelines.
    - IPCC AR6 WGI (2021), Chapter 6: Short-lived climate forcers.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "p"


def simulate_abm(params, steps, seed=42):
    p = dict(params)

    # Dispersión radial: emisiones se concentran en centros industriales
    # y se dispersan hacia periferia (patrón hub-and-spoke de contaminación).
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "radial"
    if "forcing_gradient_strength" not in p:
        # 0.55: gradiente moderado centro→periferia.
        # Menor que deforestación (0.65) porque la dispersión atmosférica
        # suaviza más el campo que la expansión agrícola.
        p["forcing_gradient_strength"] = 0.55

    # Heterogeneidad: variabilidad regional en sensibilidad a emisiones.
    # Topografía (valles acumulan), vegetación (filtro), clima local.
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.25

    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

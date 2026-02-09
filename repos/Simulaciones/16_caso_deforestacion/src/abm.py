import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "d"


def simulate_abm(params, steps, seed):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "radial"  # Deforestación avanza desde periferia (von Thünen 1826)
    if "forcing_gradient_strength" not in p:
        # 0.65: gradiente fuerte centro→periferia, refleja que la deforestación
        # es heterogénea espacialmente (Laurance et al. 2002: fish-bone pattern)
        p["forcing_gradient_strength"] = 0.65
    if "heterogeneity_strength" not in p:
        # 0.30: alta variabilidad regional (suelo, topografía, accesibilidad)
        # Basado en coef. variación observado en tasas de deforestación (Hansen 2013)
        p["heterogeneity_strength"] = 0.30
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

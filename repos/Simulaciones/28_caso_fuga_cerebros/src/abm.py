"""abm.py — 28_caso_fuga_cerebros (Top-Tier)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from abm_core import simulate_abm_core
SERIES_KEY = "fc"

def simulate_abm(params, steps, seed=2):
    p = dict(params)
    if "forcing_gradient_type" not in p:
        # random_hubs: polos académicos/tecnológicos como atractores
        #   (Docquier & Rapoport 2012: brain drain concentrado)
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        # 0.65: gradiente fuerte (Beine et al. 2001:
        #   países destino concentran >60% de migrantes cualificados)
        p["forcing_gradient_strength"] = 0.65
    if "heterogeneity_strength" not in p:
        # 0.30: alta variabilidad en I+D entre países
        #   (UNESCO 2021: GERD varía 0.1–4.5% del PIB)
        p["heterogeneity_strength"] = 0.3
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

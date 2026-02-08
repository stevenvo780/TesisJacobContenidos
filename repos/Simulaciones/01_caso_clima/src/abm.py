import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "tbar"


def simulate_abm(params, steps, seed):
    # Ensure macro coupling params are passed through
    p = dict(params)
    if "macro_target_series" in p and p["macro_target_series"] is not None:
        # Debug: confirm coupling is active
        # print(f"DEBUG: Coupling check - macro_target_series length: {len(p['macro_target_series'])}")
        pass
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

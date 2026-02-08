import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "tbar"


def simulate_abm(params, steps, seed):
    # Ensure macro coupling params are passed through
    p = dict(params)
    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_core import simulate_abm_core

SERIES_KEY = "d"


def simulate_abm(params, steps, seed):
    return simulate_abm_core(params, steps, seed=seed, series_key=SERIES_KEY)

"""
validate.py — 15_caso_wikipedia (Top-Tier)

Hyperobject: "Wikipedia" / "Collective Knowledge"
- Non-local: Articles are edited by global community.
- Viscous: Knowledge accumulates slowly, hard to erase.
- Phased: Different topics at different maturity stages.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import load_real_data, make_synthetic
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def main():
    config = CaseConfig(
        case_name="Wikipedia (Axelrod + Lotka-Volterra)",
        value_col="value",
        series_key="w",
        grid_size=7,
        persistence_window=12,
        synthetic_start="2005-01-01",
        synthetic_end="2023-01-01", # ~18 years weekly
        synthetic_split="2015-01-01",
        real_start="2015-07-01",
        real_end="2024-12-01",
        real_split="2021-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "n_agents": 50,
            "n_features": 5,
            "n_traits": 3,
            "ode_r": 0.1,
            "ode_alpha": 0.3,
            "ode_beta": 0.2,
            "ode_gamma": 0.1
        },
        driver_cols=[],  # Datos Wikimedia sin driver externo
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    print(f"DEBUG: writing results to {os.path.abspath(out_dir)}")
    write_outputs(results, os.path.abspath(out_dir))

    # Print Metrics
    print("\n--- Validation Results ---")
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        val = edi.get('value', 'N/A') if isinstance(edi, dict) else edi
        print(f"  {phase_name}: EDI={val:.4f} Pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

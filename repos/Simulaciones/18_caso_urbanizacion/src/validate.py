"""
validate.py — 18_caso_urbanizacion (Top-Tier)

Hyperobject: "The City" / "Global Urban System"
- Non-local: Cities are connected via trade, migration, ideas.
- Viscous: Infrastructure persists for centuries.
- Phased: Different cities at different development stages.
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
        case_name="Urbanización (Bettencourt + Preferential Attachment)",
        value_col="value",
        series_key="u",
        grid_size=20,
        persistence_window=10, # Decadal
        synthetic_start="1960-01-01",
        synthetic_end="2023-01-01", # 63 years yearly
        synthetic_split="2000-01-01",
        real_start="1960-01-01",
        real_end="2023-01-01",
        real_split="2000-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "n_initial_cities": 10,
            "abm_new_city_prob": 0.02,
            "abm_migration_rate": 0.05,
            "abm_beta": 1.15,
            "ode_r": 0.05,
            "ode_K": 0.9,
            "ode_gamma": 2.0
        },
        driver_cols=["gdp_growth"],
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

"""
validate.py — 20_caso_kessler (Top-Tier)

Hyperobject: "Kessler Syndrome" / "The Debris Cloud"
- Non-local: Debris orbits entire Earth.
- Viscous: Remains for decades-centuries at high altitudes.
- Phased: Different orbital regimes at different saturation.

Models Used:
- NASA ORDEM / ESA MASTER Data Generation
- NASA LEGEND-style Shell ABM with Breakup Model
- Kessler-Liou Quadratic ODE (Runaway Cascade)
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
        case_name="Síndrome de Kessler (NASA LEGEND + ORDEM)",
        value_col="value",
        series_key="k",
        grid_size=25,
        persistence_window=10,
        synthetic_start="1970-01-01",
        synthetic_end="2023-01-01",  # 53 years yearly
        synthetic_split="2005-01-01",
        real_start="1970-01-01",
        real_end="2023-01-01",
        real_split="2005-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "n_shells": 10,
            "abm_collision_coeff": 1e-9,
            "ode_alpha": 2.0e-10,
            "ode_beta": 0.02,
            "ode_frag_mult": 500
        },
        driver_cols=["launches"],
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

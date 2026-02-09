"""
validate.py — 17_caso_oceanos (Top-Tier)

Hyperobject: "The Ocean" / "Ocean Heat Content"
- Non-local: Heat distributes globally via currents.
- Viscous: Enormous thermal inertia (decades).
- Phased: Different basins at different phases.
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
        case_name="Ocean (Stommel + Thermohaline ABM)",
        value_col="value",
        series_key="e",
        grid_size=15,
        persistence_window=24,
        synthetic_start="1980-01-01",
        synthetic_end="2023-01-01",
        synthetic_split="2005-01-01",
        real_start="1990-01-01",
        real_end="2023-01-01",
        real_split="2010-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "grid_size": 15,
            "abm_diffusion": 0.1,
            "abm_convection": 0.5,
            "ode_eta1": 3.0,
            "ode_eta2": 1.0
        },
        driver_cols=[],  # CSV solo tiene date, value
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

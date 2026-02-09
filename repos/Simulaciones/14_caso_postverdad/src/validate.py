"""
validate.py — 14_caso_postverdad (Top-Tier)

Hyperobject: "The Infosphere" / "Post-Truth"
- Non-local: Misinformation spreads globally.
- Viscous: Hard to eradicate once widespread.
- Phased: Different populations experience different phases.
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
        case_name="Postverdad (SIS Infodemic)",
        value_col="value",
        series_key="pv",
        grid_size=10,
        persistence_window=12,
        synthetic_start="2015-01-01",
        synthetic_end="2023-01-01", # 8 years weekly
        synthetic_split="2020-01-01",
        real_start="2015-01-01",
        real_end="2023-01-01",
        real_split="2020-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "n_agents": 100,
            "abm_beta": 0.2,
            "abm_gamma": 0.1,
            "ode_beta": 0.3,
            "ode_gamma": 0.15
        },
        driver_cols=["virality"],
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

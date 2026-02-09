"""
validate.py — 13_caso_politicas_estrategicas (Top-Tier)

Hyperobject: "The Policy" / "The Institution"
- Non-local: Affects all agents in the network.
- Viscous: Changes slowly (Institutional Inertia).
- Phased: Different countries experience different phases of adoption.
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
        case_name="Políticas Estratégicas (Bass Diffusion + Inertia)",
        value_col="value",
        series_key="s",
        grid_size=7,   # sqrt(50) approx
        persistence_window=24,
        synthetic_start="1990-01-01",
        synthetic_end="2020-01-01", # 30 years monthly
        synthetic_split="2010-01-01",
        real_start="1990-01-01",
        real_end="2020-01-01",
        real_split="2010-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "n_agents": 50,
            "abm_p": 0.01,
            "abm_q": 0.3,
            "ode_alpha": 0.05,
            "ode_beta": 0.3,
            "ode_gamma": 0.1
        },
        driver_cols=["stringency"], # Policy Stringency as Driver
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

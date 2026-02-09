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
        case_name="Paradigmas Cientificos (Ising)",
        value_col="value",
        series_key="j", # 'j' for justice/judgment/consensus
        grid_size=10,   # Network visualization mapped to 10x10
        persistence_window=20,
        synthetic_start="2000-01-01",
        synthetic_end="2000-02-01", # 1 month hourly (744 steps)
        synthetic_split="2000-01-20",
        real_start="1996-01-01",
        real_end="2022-01-01",
        real_split="2012-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "n_agents": 50, # Reduced size
            "abm_temperature": 2.0, 
            "ode_alpha": 1.0,
            "ode_beta": 1.0
        },
        driver_cols=["journal_articles"],  # Publicaciones científicas WB
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))
    
    # Print Metrics to Stdout
    print("\n--- Validation Results ---")
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        val = edi.get('value', 'N/A') if isinstance(edi, dict) else edi
        print(f"  {phase_name}: EDI={val:.4f} Pass={phase.get('overall_pass', False)}")

if __name__ == "__main__":
    main()

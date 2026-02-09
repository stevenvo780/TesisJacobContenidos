"""validate.py — Caso 11: Movilidad Urbana.

Modelo híbrido: ODE Diagrama Fundamental Macroscópico (MFD) + ABM de
tráfico en red Scale-Free.  Datos: World Bank GDP per capita como
proxy de demanda de movilidad.
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
        case_name="Movilidad Urbana (Traffic)",
        value_col="value",
        series_key="v",
        grid_size=20, # Flow is aggregate, but we track spatial density
        persistence_window=24, # Daily cycle
        synthetic_start="2023-01-01 00:00:00",
        synthetic_end="2023-01-07 23:00:00", # 1 week hourly
        synthetic_split="2023-01-05 00:00:00",
        real_start="1970-01-01",
        real_end="2023-01-01",
        real_split="2005-01-01",
        corr_threshold=0.6,
        extra_base_params={"n_nodes": 50, "n_agents": 200},
        driver_cols=["gdp_per_capita", "air_departures"],  # WB: GDP + tráfico aéreo
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

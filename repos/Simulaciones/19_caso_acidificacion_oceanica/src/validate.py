"""
validate.py — 19_caso_acidificacion_oceanica (Top-Tier)

Hyperobject: "Ocean Acidification" / "The Other CO2 Problem"
- Non-local: Acidification is global, affects all oceans.
- Viscous: Chemical changes persist for millennia.
- Phased: Different regions at different omega levels.

Models Used:
- CO2SYS Carbonate Chemistry (Zeebe & Wolf-Gladrow)
- Marine Calcifier ABM (Ries, Kroeker)
- Revelle Factor ODE (IPCC)
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
        case_name="Acidificación Oceánica (CO2SYS + Revelle Factor)",
        value_col="value",
        series_key="ac",
        grid_size=20,
        persistence_window=24,
        synthetic_start="1980-01-01",
        synthetic_end="2023-01-01",
        synthetic_split="2005-01-01",
        real_start="1990-01-01",
        real_end="2020-01-01",
        real_split="2010-01-01",
        corr_threshold=0.5,
        extra_base_params={
            "grid_size": 20,
            # abm_calc_rate=0.02: Tasa calcificación (Ries et al. 2009: crecimiento ~2%/mes)
            "abm_calc_rate": 0.02,
            # abm_diss_rate=0.05: Tasa disolución (Kroeker 2013: 5%/mes bajo Ω<1)
            "abm_diss_rate": 0.05,
            # abm_stress_thresh=1.0: Umbral Ω aragonita (Feely et al. 2004: Ω=1 = sub-saturación)
            "abm_stress_thresh": 1.0,
            # ode_gamma=0.5: Sensibilidad pH a pCO2 (Zeebe & Wolf-Gladrow 2001)
            "ode_gamma": 0.5
        },
        driver_cols=[],  # CSV solo tiene date, value
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    # Print Metrics
    print("\n--- Validation Results ---")
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        val = edi.get('value', 'N/A') if isinstance(edi, dict) else edi
        print(f"  {phase_name}: EDI={val:.4f} Pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

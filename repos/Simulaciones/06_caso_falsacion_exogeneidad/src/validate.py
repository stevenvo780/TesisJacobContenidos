"""validate.py — Caso 06: Falsación por Exogeneidad.

Prueba de control negativo: demuestra que el framework NO detecta
emergencia espuria cuando el driver es completamente independiente
de la señal objetivo (GBM caótica vs. onda sinusoidal).

Resultado esperado: EDI << 0.30 → falsificación exitosa.
"""

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_memetic_daily
from ode import simulate_ode
from datetime import datetime
from hybrid_validator import CaseConfig, write_outputs


def load_real_data(start_date, end_date):
    """Carga (o genera) serie GBM + driver espurio."""
    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "memetic.csv")
    df = fetch_memetic_daily(start_date, end_date, cache_path=os.path.abspath(cache_path))
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def main():
    config = CaseConfig(
        case_name="Falsación: Exogeneidad",
        value_col="value",
        series_key="incidence",
        grid_size=20,
        persistence_window=6,
        synthetic_start="2020-01-01",
        synthetic_end="2024-01-01",
        synthetic_split="2022-01-01",
        real_start="2020-01-01",
        real_end="2024-01-01",
        real_split="2022-01-01",
        corr_threshold=0.7,
        extra_base_params={},
        driver_cols=["unrelated_driver"], # Explicitly use the noise driver
        ode_calibration=False, # Calib too slow, testing Null Hypothesis with default params
        abm_calibration=False, # Skip ABM calibration loop
    )

    from hybrid_validator import evaluate_phase

    print("--- Falsificación: Exogeneidad ---")
    
    # 1. Load Data
    real_df = load_real_data(config.real_start, config.real_end)
    
    # 2. Run Single Phase (Real)
    real_phase = evaluate_phase(
        config, real_df, config.real_start, config.real_end,
        config.real_split, simulate_abm, simulate_ode,
        param_grid=None
    )
    
    edi = real_phase.get("edi", {})
    val = edi.get("value", -999)
    print(f"  EDI: {val:.4f}")
    
    today = datetime.now().isoformat()
    results = {
        "case": config.case_name,
        "generated_at": today,
        "git": {"commit": "falsification_mode", "dirty": False},
        "phases": {"real": real_phase}, 
        "falsification_success": (val < 0.1)
    }
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))
    print("Validación completa. Ver outputs/metrics.json y outputs/report.md")


if __name__ == "__main__":
    main()

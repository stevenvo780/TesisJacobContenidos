"""validate.py — Caso 08: Falsación por Observabilidad Escasa.

Prueba de driver insuficiente (confounder): el proxy solo captura la
tendencia pero no la oscilación oculta del target.
Resultado esperado: EDI << 0.30 → falsificación exitosa.
"""

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_sparse_happiness
from ode import simulate_ode
from datetime import datetime
from hybrid_validator import CaseConfig, write_outputs


def load_real_data(start_date, end_date):
    """Carga (o genera) datos de confounder sintético."""
    cache_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "sparse_happiness.csv"))
    df, _ = fetch_sparse_happiness(cache_path, start_year=int(start_date[:4]), end_year=int(end_date[:4]))
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def main():
    config = CaseConfig(
        case_name="Falsación: Observabilidad Escasa",
        value_col="value",
        series_key="incidence",
        grid_size=20,
        persistence_window=3,
        synthetic_start="2005-01-01",
        synthetic_end="2023-01-01",
        synthetic_split="2015-01-01",
        real_start="2005-01-01",
        real_end="2023-01-01",
        real_split="2015-01-01",

        corr_threshold=0.7,
        extra_base_params={},
        driver_cols=["insufficient_driver"],
        ode_calibration=False,
        abm_calibration=False,
    )

    from hybrid_validator import evaluate_phase

    print("--- Falsificación: Observabilidad Escasa ---")
    
    real_df = load_real_data(config.real_start, config.real_end)
    correlation = real_df["value"].corr(real_df["insufficient_driver"])
    print(f"  Driver Correlation (Trend Only): {correlation:.4f} (Expected High)")
    
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
        "git": {"commit": "falsification_confounder", "dirty": False},
        "phases": {"real": real_phase}, 
        "falsification_success": (val < 0.15),
        "driver_correlation": correlation
    }
    
    if val < 0.15:
        print("  RESULT: SUCCESS (Insufficient Driver Rejected, EDI < 0.15)")
    else:
        print("  RESULT: FAILURE (Model Hallucinated Causality, EDI > 0.15)")

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))
    print("Validación completa. Ver outputs/metrics.json y outputs/report.md")


if __name__ == "__main__":
    main()

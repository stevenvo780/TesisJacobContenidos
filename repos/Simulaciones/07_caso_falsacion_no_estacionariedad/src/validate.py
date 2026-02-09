"""validate.py — Caso 07: Falsación por No-Estacionariedad.

Prueba de regresión espuria (Granger & Newbold 1974): dos tendencias
lineales independientes producen ρ > 0.9 pero NO hay causalidad.
Resultado esperado: EDI << 0.30 → falsificación exitosa.
"""

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_crypto_daily
from ode import simulate_ode
from datetime import datetime
from hybrid_validator import CaseConfig, write_outputs


def load_real_data(start_date, end_date):
    """Carga (o genera) par de tendencias independientes."""
    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "crypto.csv")
    df = fetch_crypto_daily(start_date, end_date, cache_path=os.path.abspath(cache_path))
    df["date"] = pd.to_datetime(df["date"])
    # Submuestreo semanal para tiempo de ejecución razonable
    df = df.set_index("date").resample("W").mean().dropna().reset_index()
    return df.dropna(subset=["date", "value"])


def main():
    config = CaseConfig(
        case_name="Falsación: No-Estacionariedad",
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
        driver_cols=["spurious_trend"],
        ode_calibration=False,
        abm_calibration=False,
    )

    from hybrid_validator import evaluate_phase

    print("--- Falsificación: No-Estacionariedad ---")
    
    real_df = load_real_data(config.real_start, config.real_end)
    correlation = real_df["value"].corr(real_df["spurious_trend"])
    print(f"  Spurious Correlation (Trend vs Trend): {correlation:.4f} (Expected > 0.9)")
    
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
        "git": {"commit": "falsification_trend", "dirty": False},
        "phases": {"real": real_phase}, 
        "falsification_success": (val < 0.1),
        "spurious_correlation": correlation
    }
    
    if val < 0.1:
        print("  RESULT: SUCCESS (Falsification Passed, EDI < 0.1)")
    else:
        print("  RESULT: FAILURE (Trend Confounded by Model, EDI > 0.1)")

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))
    print("Validación completa. Ver outputs/metrics.json y outputs/report.md")


if __name__ == "__main__":
    main()

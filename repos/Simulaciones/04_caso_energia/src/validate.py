"""
validate.py — Energía (OPSD GB Grid)
Validación híbrida ABM+ODE con protocolo C1-C5.
Generado automáticamente por el framework de validación de hiperobjetos.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_opsd_load_monthly
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):

    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "opsd_gb.csv")
    df = fetch_opsd_load_monthly(start_date, end_date, cache_path=os.path.abspath(cache_path))
    df = df.rename(columns={"demand": "value"})
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    forcing = [0.01 * t for t in range(steps)]
    true_params = {
        "p0": 0.0, "e0": 0.0, "ode_alpha": 0.08, "ode_beta": 0.03,
        "ode_noise": 0.02, "forcing_series": forcing,
        "p0_ode": 0.0,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.08, "beta": 0.03}, "measurement_noise": 0.05}
    return df, meta


def main():
    # ── Configuración del caso ──────────────────────────────────────────
    # grid_size=20: 400 productores de energía.
    # persistence_window=12: 12 meses para estabilidad.
    # Datos mensuales OPSD GB (demanda eléctrica UK).
    # ODE: Lotka-Volterra de competencia fósil vs renovable.
    config = CaseConfig(
        case_name="Energía (OPSD GB Grid)",
        value_col="value",
        series_key="e",
        grid_size=20,
        persistence_window=12,
        synthetic_start="2000-01-01",
        synthetic_end="2019-12-01",
        synthetic_split="2010-01-01",
        real_start="2015-01-01",
        real_end="2020-06-30",
        real_split="2019-01-01",
        corr_threshold=0.7,
        extra_base_params={
            # Nota: la ODE Lotka-Volterra usa ode_alpha y ode_beta como
            # coeficientes de competencia (defaults 0.1 y 0.05 en ode.py).
            # No se sobreescriben aquí para usar los valores estándar.
        },
        # Drivers: temperatura (demanda estacional) y precio (señal de mercado).
        # renewables_share ELIMINADO como driver para evitar circularidad
        # (la variable de salida ODE es cuota renovable).
        driver_cols=["tavg", "price"],
        use_topology=True,
        topology_type="small_world",
        ode_calibration=False,  # Parámetros L-V fijados desde literatura
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        if isinstance(edi, dict):
            print(f"  {phase_name}: EDI={edi.get('value', 'N/A'):.3f}")
        else:
            print(f"  {phase_name}: EDI={edi:.3f}")
        print(f"    overall_pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

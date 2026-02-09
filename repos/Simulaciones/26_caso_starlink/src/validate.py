"""
validate.py — Constelaciones Satelitales (Starlink)
Validación híbrida ABM+ODE con protocolo C1-C5.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_data
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    cache_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv"))
    df, _ = fetch_data(cache_path, start_date=start_date, end_date=end_date)
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=129):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    # Forcing: despliegue satelital con ramp-up suave
    # 0.012*t: tendencia secular (SpaceX 2020: ~60 lanzamientos/año)
    # 0.0004*t^1.3: aceleración por competencia multi-operador
    forcing = [0.012 * t + 0.0004 * t**1.3 for t in range(steps)]
    true_params = {
        "p0": 0.0,
        "ode_inflow": 0.18,   # Alta tasa lanzamiento (Lewis 2011)
        "ode_decay": 0.015,   # Deorbit ~1.5%/año (vida útil ~5 años)
        "ode_noise": 0.03,    # Variabilidad estocástica
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"inflow": 0.18, "decay": 0.015}, "measurement_noise": 0.05}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Constelaciones Satelitales Starlink (Mega-Constellation)",
        value_col="value",
        series_key="st",
        grid_size=25,
        persistence_window=5,
        synthetic_start="1990-01-01",
        synthetic_end="2022-01-01",
        synthetic_split="2010-01-01",
        real_start="1990-01-01",
        real_end="2022-01-01",
        real_split="2010-01-01",
        corr_threshold=0.60,
        ode_noise=0.07,
        base_noise=0.005,
        loe=4,
        n_runs=7,
        ode_calibration=True,
        extra_base_params={
            # ode_saturation=0.002: saturación orbital cuadrática
            #   (Kessler 1978: probabilidad colisión ∝ N²)
            "ode_saturation": 0.002,
            "forcing_scale": 0.12,   # Sensibilidad ABM a lanzamientos
            "macro_coupling": 0.28,  # Acoplamiento macro→micro
        },
        driver_cols=["launches", "collision_events", "debris_new"],  # +basura espacial nueva
        log_transform=True,  # Fix P7: crecimiento exponencial necesita log-transform
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        sym = phase.get("symploke", {})
        print(f"  {phase_name}: overall={phase.get('overall_pass')}"
              f" EDI={edi.get('value', 0):.3f} CR={sym.get('cr', 0):.3f}"
              f" C1={phase.get('c1_convergence')}")
    print("Validación completa.")


if __name__ == "__main__":
    main()

"""
validate.py — Epidemiología (COVID-19 SEIR)
Validación híbrida ABM+ODE con protocolo C1-C5.
Generado automáticamente por el framework de validación de hiperobjetos.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_owid_world_weekly
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):

    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "owid_covid.csv")
    df = fetch_owid_world_weekly(start_date, end_date, cache_path=os.path.abspath(cache_path))
    df = df.rename(columns={"cases": "value"})
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="W")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    forcing = [0.01 * t for t in range(steps)]
    true_params = {
        "beta": 0.3, "sigma": 0.2, "gamma": 0.1, "noise": 0.02,
        "forcing_series": forcing, "s0": 0.999, "e0": 0.001,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = "incidence"
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"beta": 0.3, "sigma": 0.2, "gamma": 0.1}, "measurement_noise": 0.05}
    return df, meta


def main():
    # ── Configuración del caso ──────────────────────────────────────────
    # grid_size=20: red de 400 agentes (ABM usa Barabási-Albert interno).
    # persistence_window=8: 8 semanas de estabilidad.
    # Datos semanales OWID COVID-19 (casos globales).
    # ODE: SEIR Kermack-McKendrick con R₀=2.5.
    # Nota: la ODE lee ode_R0, ode_latent, ode_infectious (defaults en ode.py).
    config = CaseConfig(
        case_name="Epidemiología (COVID-19 SEIR)",
        value_col="value",
        series_key="incidence",
        grid_size=20,
        persistence_window=8,
        synthetic_start="2010-01-03",
        synthetic_end="2020-12-27",
        synthetic_split="2017-01-01",
        real_start="2020-03-01",
        real_end="2023-12-31",
        real_split="2022-01-01",
        corr_threshold=0.7,
        ode_calibration=True,
        extra_base_params={
            # Parámetros ABM epidemiológicos:
            # abm_beta=0.3: SAR ~0.3 para COVID (Bi et al. 2020)
            # abm_latent=3: periodo latente COVID ~3-5 días (Li et al. 2020)
            # noise=0.02: ruido de observación
            "noise": 0.02,
        },
        # Drivers: muertes, vacunación, índice de stringencia.
        # Todos disponibles en OWID COVID-19 dataset.
        driver_cols=["deaths", "vaccinated", "stringency"],
        use_topology=True,
        topology_type="small_world",
        topology_params={"k": 4, "p": 0.1},
        feedback_strength=0.05,  # Feedback micro→macro moderado
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
    print("Validación completa. Ver outputs/metrics.json y outputs/report.md")


if __name__ == "__main__":
    main()

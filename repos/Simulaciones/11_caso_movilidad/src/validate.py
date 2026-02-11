"""validate.py — Caso 11: Movilidad Urbana.

Modelo híbrido: ODE mean-reversion + ABM radial.
Datos: Vehículos registrados (World Bank) + GDP per capita + tráfico aéreo.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    """Carga datos reales de movilidad (vehículos registrados WB)."""
    cache_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    )
    df = pd.read_csv(cache_path, parse_dates=["date"])
    df["date"] = pd.to_datetime(df["date"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    """Serie sintética mensual con tendencia de crecimiento vehicular."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)

    # Forcing: crecimiento logístico de motorización con ciclos económicos
    forcing = [0.5 + 0.01 * t + 0.3 * np.sin(2 * np.pi * t / 48) for t in range(steps)]
    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.10,
        "ode_beta": 0.50,
        "ode_noise": 0.05,
        "forcing_scale": 1.0,
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k != "forcing"][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.08, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.10, "beta": 0.50}, "measurement_noise": 0.08}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Movilidad Urbana (Vehículos)",
        value_col="value",
        series_key="v",
        grid_size=25,
        persistence_window=5,  # 5 años para datos anuales
        synthetic_start="2000-01-01",
        synthetic_end="2019-12-01",
        synthetic_split="2012-01-01",
        real_start="1970-01-01",
        real_end="2023-01-01",
        real_split="2005-01-01",
        corr_threshold=0.5,
        extra_base_params={},
        driver_cols=["gdp_per_capita", "air_departures"],
        use_topology=True,
        topology_type="small_world",
        topology_params={"k": 4, "p": 0.1},
        feedback_strength=0.05,
        loe=5,
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        val = edi.get("value", "N/A") if isinstance(edi, dict) else edi
        print(f"  {phase_name}: EDI={val:.4f} Pass={phase.get('overall_pass', False)}")


if __name__ == "__main__":
    main()

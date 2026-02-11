"""
validate.py — Epidemiología (COVID-19 Global)
Validación híbrida ABM+ODE con protocolo C1-C5.

Variable: log(new_cases_smoothed + 1) semanal (OWID, World).
Drivers: log_deaths (severidad/variante), vaccinated (intervención).
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_covid_data
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):
    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    df = fetch_covid_data(start_date, end_date,
                          cache_path=os.path.abspath(cache_path))
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="W")
    steps = len(dates)

    # Driver 1: log_deaths — simula olas epidémicas con picos y valles.
    # Patrón: tendencia ascendente + componente sinusoidal (olas ~26 sem).
    t_arr = np.arange(steps)
    deaths_synth = (
        6.0                                        # baseline log(deaths)
        + 0.015 * t_arr                            # tendencia leve
        + 1.5 * np.sin(2 * np.pi * t_arr / 52)    # olas anuales
        + rng.normal(0, 0.2, size=steps)           # ruido
    )

    # Driver 2: vaccinated — curva S (0→70% en ~100 semanas).
    # Refleja campaña de vacunación que inicia semana ~40.
    vacc_synth = 70.0 / (1.0 + np.exp(-0.06 * (t_arr - 80)))
    vacc_synth += rng.normal(0, 0.5, size=steps)
    vacc_synth = np.clip(vacc_synth, 0, 75)

    # Z-score drivers
    d_z = (deaths_synth - deaths_synth.mean()) / (deaths_synth.std() + 1e-8)
    v_z = (vacc_synth - vacc_synth.mean()) / (vacc_synth.std() + 1e-8)

    # Forcing: peso dominante en deaths (como en datos reales: w=0.89).
    forcing = (0.85 * d_z + 0.15 * v_z).tolist()

    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.35,
        "ode_beta": 0.50,     # τ = 2 sem → tracking rápido, evita desfase
        "ode_noise": 0.01,
        "forcing_series": forcing,
        "forcing_scale": 1.0,  # Escala unitaria: α controla sensibilidad.
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    obs = np.array(sim["incidence"]) + rng.normal(0.0, 0.01, size=steps)

    df = pd.DataFrame({
        "date": dates,
        "value": obs,
        "log_deaths": deaths_synth.tolist(),
        "vaccinated": vacc_synth.tolist(),
    })
    meta = {
        "ode_true": {"alpha": 0.35, "beta": 0.50, "noise": 0.01},
        "measurement_noise": 0.01,
    }
    return df, meta


def main():
    # ── Configuración del caso ──────────────────────────────────────────
    # 201 puntos semanales (2020-03 a 2023-12). Split 2022-01.
    # Train: ~97 semanas. Val: ~104 semanas.
    # Variable: log(new_cases_smoothed+1) para linearizar 4 OdM de rango.
    # Drivers:
    #   - log_deaths (w=+0.89): mortalidad = proxy severidad/variante
    #   - vaccinated (w=+0.22): cobertura vacunal (intervención externa)
    # r_val = +0.916 (forcing-obs correlación en validación).
    config = CaseConfig(
        case_name="Epidemiología (COVID-19 Global)",
        value_col="value",
        series_key="incidence",
        grid_size=25,
        persistence_window=8,
        corr_threshold=0.5,
        synthetic_start="2010-01-03",
        synthetic_end="2020-12-27",
        synthetic_split="2017-01-01",
        real_start="2020-03-01",
        real_end="2023-12-31",
        real_split="2022-01-01",
        extra_base_params={
            "ode_alpha": 0.30,
            "ode_beta": 0.15,
        },
        ode_calibration=True,
        driver_cols=["log_deaths", "vaccinated"],
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

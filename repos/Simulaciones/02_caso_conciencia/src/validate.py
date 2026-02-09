"""
validate.py — Conciencia Colectiva
Validación híbrida ABM+ODE con protocolo C1-C5.
Dominio: Cognitivo-social
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
    cache_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    )
    df, _ = fetch_data(cache_path, start_date=start_date, end_date=end_date)
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    # Forcing: difusión cultural con saturación logarítmica (Tomasello 2009)
    # Crece rápido al inicio, se satura gradualmente
    forcing = [0.02 * np.log1p(t) for t in range(steps)]
    true_params = {
        "p0": 0.0, "t0": 0.0,
        "ode_alpha": 0.03,   # τ ≈ 33 meses (inercia cognitiva colectiva)
        "ode_beta": 0.05,    # Decaimiento atencional (Barabási 2005)
        "ode_noise": 0.04,   # Alta variabilidad en percepción social
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.06, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.03, "beta": 0.05}, "measurement_noise": 0.06}
    return df, meta


def main():
    # ── Configuración del caso ──────────────────────────────────────────
    # grid_size=4 → ABM local usa 16 módulos cognitivos (4×4) según GWT.
    # persistence_window=12 → 12 meses de ventana para estabilidad temporal.
    # split=2015 → ~11 años de entrenamiento (2004-2014), ~9 años de validación.
    # ode_calibration=False → α y β fijados desde literatura (ver ode.py).
    config = CaseConfig(
        case_name="Conciencia Colectiva",
        value_col="value",
        series_key="c",
        grid_size=4,  # 4×4 = 16 módulos cognitivos (GWT, Baars 1988)
        persistence_window=12,
        synthetic_start="2004-01-01",
        synthetic_end="2023-12-01",
        synthetic_split="2015-01-01",
        real_start="2004-01-01",
        real_end="2023-12-01",
        real_split="2015-01-01",
        corr_threshold=0.7,
        extra_base_params={
            # α = 0.5 mes⁻¹ → τ_rise = 2 meses (Wu & Huberman 2007, PNAS)
            "ode_alpha": 0.5,
            # β = 0.8 mes⁻¹ → τ_decay ≈ 1.25 meses (Candia et al. 2019, Nat. Hum. Behav.)
            "ode_beta": 0.8,
        },
        ode_calibration=False,  # Parámetros fijados desde literatura
        # Tasa de suicidio (World Bank) como proxy de malestar social.
        # Justificación: Durkheim (1897) establece la tasa de suicidio como
        # indicador sociológico clásico de cohesión/anomia social.
        driver_cols=["suicide_rate"],
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

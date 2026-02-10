"""
validate.py — Deforestación Global
Validación híbrida ABM+ODE con protocolo C1-C5.
Generado automáticamente por el framework de validación de hiperobjetos.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm import simulate_abm
from data import fetch_deforestation
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):

    cache_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "wb_deforestation.csv"))
    df, _ = fetch_deforestation(cache_path, start_year=int(start_date[:4]), end_year=int(end_date[:4]))
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=119):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    # Forcing: presión deforestadora creciente (agricultura, ganadería)
    # Componente lineal 0.025*t: tendencia secular de expansión agrícola (FAO 2020)
    # Componente super-lineal 0.0005*t^1.3: aceleración por retroalimentación
    #   (tala → carreteras → más tala; Laurance et al. 2002, Science)
    forcing = [0.025 * t + 0.0005 * t**1.3 for t in range(steps)]
    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.06,   # Tasa de conversión forestal (≈6%/año en frentes activos; Hansen et al. 2013)
        "ode_beta": 0.008,   # Regeneración natural (~0.8%/año; Chazdon et al. 2016, Science)
        "ode_inflow": 0.06,  # Alias de ode_alpha para accumulation_decay
        "ode_decay": 0.008,  # Alias de ode_beta para accumulation_decay
        "ode_noise": 0.04,   # Variabilidad interanual (sequías, políticas)
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.12, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"inflow": 0.06, "decay": 0.008}, "measurement_noise": 0.12}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Deforestación Global (von Thünen Frontier)",
        value_col="value",
        driver_cols=[],  # Dataset univariado (WorldBank AG.LND.FRST.ZS)
        series_key="d",
        grid_size=50,             # 50×50 = 2500 agentes (antes 25×25=625)
        persistence_window=5,
        synthetic_start="1990-01-01",
        synthetic_end="2022-01-01",
        synthetic_split="2010-01-01",
        real_start="1990-01-01",
        real_end="2022-01-01",
        real_split="2010-01-01",
        corr_threshold=0.65,
        ode_noise=0.04,
        base_noise=0.003,
        loe=3,
        n_runs=15,                # 15 réplicas (antes 7) — 32 cores disponibles
        ode_calibration=True,
        extra_base_params={
            "ode_inflow": 0.06,    # Tasa conversión forestal (Hansen et al. 2013)
            "ode_decay": 0.008,    # Regeneración natural (~décadas; Chazdon 2016)
            "forcing_scale": 0.10,  # Sensibilidad ABM a driver externo
            "macro_coupling": 0.25, # Acoplamiento macro: presión global sobre celdas locales
        },
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))

    # Resumen
    for phase_name, phase in results.get("phases", {}).items():
        edi = phase.get("edi", {})
        sym = phase.get("symploke", {})
        print(f"  {phase_name}: overall={phase.get('overall_pass')} "
              f"EDI={edi.get('value', 0):.3f} CR={sym.get('cr', 0):.3f} "
              f"C1={phase.get('c1_convergence')} C2={phase.get('c2_robustness')} "
              f"C3={phase.get('c3_replication')} C4={phase.get('c4_validity')} "
              f"C5={phase.get('c5_uncertainty')}")
    print("Validación completa. Ver outputs/metrics.json y outputs/report.md")


if __name__ == "__main__":
    main()

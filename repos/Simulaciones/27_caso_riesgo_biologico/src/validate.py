"""
validate.py — Riesgo Biológico Global
Validación híbrida ABM+ODE con protocolo C1-C5.
Dominio: Bioseguridad
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
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Forcing: presión zoonótica con tendencia + shock COVID
    # 0.010*t: tendencia secular ~1%/año (Jones et al. 2008: EID events crecientes)
    # 0.0003*t^1.2: aceleración por deforestación/urbanización
    forcing = [0.010 * t + 0.0003 * t**1.2 for t in range(steps)]
    # Shock pandémico tardío (simula evento tipo COVID-19)
    # 0.18: magnitud del shock (WHO 2020: TB incidence spike post-COVID)
    # 0.3: decaimiento del shock por step
    shock_t = int(0.80 * steps)
    for i in range(shock_t, min(shock_t + 3, steps)):
        forcing[i] += 0.18 * (1 - 0.3 * (i - shock_t))

    true_params = {
        "p0": 0.0,
        "ode_alpha": 0.06,      # Acumulación riesgo ~6%/año
        "ode_beta": 0.02,       # Contención sanitaria ~2%/año
        "ode_gamma_bio": 0.03,  # Bio-amplificación (Woolhouse cascade)
        "ode_noise": 0.02,      # Variabilidad interanual
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.06, "beta": 0.02, "gamma_bio": 0.03}, "measurement_noise": 0.05}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Riesgo Biológico Global (TB Incidence — Woolhouse)",
        value_col="value",
        series_key="b",
        grid_size=25,
        persistence_window=5,
        synthetic_start="2000-01-01",
        synthetic_end="2024-01-01",
        synthetic_split="2019-01-01",
        real_start="2000-01-01",
        real_end="2024-01-01",
        real_split="2019-01-01",
        corr_threshold=0.60,
        ode_noise=0.02,
        base_noise=0.004,
        loe=4,
        n_runs=7,
        ode_calibration=True,
        extra_base_params={
            # ode_gamma_bio=0.03: bio-amplificación bilineal
            #   (Woolhouse & Gaunt 2007: cascada zoonótica interconectada)
            "ode_gamma_bio": 0.03,
            "forcing_scale": 0.20,   # Sensibilidad ABM a driver zoonótico
            "macro_coupling": 0.40,  # Acoplamiento macro→micro alto
        },
        driver_cols=["hiv_incidence", "immunization_coverage"],
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

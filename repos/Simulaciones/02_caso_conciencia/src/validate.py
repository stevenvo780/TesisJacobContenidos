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

from abm_numpy import make_abm_adapter
from data import fetch_data
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs

# ABM genérico vectorizado: respeta forcing_scale, macro_coupling, damping
# directamente, lo cual permite calibración efectiva. La ABM custom (GWT)
# no implementa damping y maneja forcing_scale de forma diferente, impidiendo
# que la calibración converja. Se usa init_center=0 (Z-scored data), init_range
# pequeño para datos anuales con poca variabilidad intra-step.
simulate_abm = make_abm_adapter("c", init_center=0.0, init_range=0.05)


def load_real_data(start_date, end_date):
    cache_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
    )
    df, _ = fetch_data(cache_path, start_date=start_date, end_date=end_date)
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["date", "value"])


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    # Datos anuales (como los reales del World Bank)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Forcing: difusión cultural con saturación logarítmica (Tomasello 2009)
    # Escala anual: crece lento, satura gradualmente.
    # Amplitud mayor para que ABM necesite acoplamiento macro (coupling > 0.1)
    forcing = [0.5 * np.log1p(t) + 0.1 * np.sin(t * 0.5) for t in range(steps)]
    true_params = {
        "c0": 0.1, "t0": 0.0,
        # α y β lentos: apropiados para dinámica anual (τ ≈ 10 años)
        "ode_alpha": 0.10,   # Sensibilidad moderada (cambio social lento)
        "ode_beta": 0.04,    # Decaimiento lento (persistencia institucional)
        "ode_noise": 0.02,   # Variabilidad baja para datos limpios
        "forcing_series": forcing,
        "forcing_scale": 1.0,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.03, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.10, "beta": 0.04}, "measurement_noise": 0.03}
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
        grid_size=10,  # 10×10 = 100 agentes, balanceado para 20 datos anuales
        persistence_window=6,  # 6 años de ventana (datos anuales)
        synthetic_start="2004-01-01",
        synthetic_end="2023-12-01",
        synthetic_split="2015-01-01",
        real_start="2004-01-01",
        real_end="2023-12-01",
        real_split="2015-01-01",
        corr_threshold=0.5,  # Más permisivo para 20 puntos
        extra_base_params={
            # ODE lenta para datos anuales: α bajo, β bajo
            # Calibración automática los ajustará, estos son semillas
            "ode_alpha": 0.08,
            "ode_beta": 0.03,
            "ode_noise": 0.03,
        },
        ode_calibration=True,  # CALIBRAR α y β contra datos reales
        # Tasa de suicidio (World Bank) como proxy de malestar social.
        # Justificación: Durkheim (1897) establece la tasa de suicidio como
        # indicador sociológico clásico de cohesión/anomia social.
        # Matrícula terciaria (proxy de participación cognitiva colectiva).
        driver_cols=["suicide_rate", "tertiary_enrollment"],
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

"""
validate.py — Clima Regional (CONUS)
Validación híbrida ABM+ODE con protocolo C1-C5.
Generado automáticamente por el framework de validación de hiperobjetos.
"""

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from abm_numpy import make_abm_adapter
from data import fetch_regional_monthly
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs


def load_real_data(start_date, end_date):

    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "conus_monthly.csv")
    cache_abs = os.path.abspath(cache_path)

    if os.path.exists(cache_abs):
        # Cache existe → usar directamente (GISTEMP anomalías + drivers)
        df = pd.read_csv(cache_abs, parse_dates=["date"])
        df = df.rename(columns={"tavg": "value"})
    else:
        # Sin cache → descargar vía meteostat (lento, fallback)
        df = fetch_regional_monthly(start_date, end_date, cache_path=cache_abs)
        df = df.rename(columns={"tavg": "value"})

    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["date", "value"])

    # ── Desestacionalización ──────────────────────────────────────────
    # Si los datos son temperatura absoluta, quita el ciclo anual (~97% varianza).
    # Si ya son anomalías (GISTEMP), centra restando media mensual residual.
    # Estándar en climatología (IPCC AR6 WG1 Ch2).
    df["month"] = df["date"].dt.month
    clim_mean = df.groupby("month")["value"].mean()
    df["value"] = df["value"] - df["month"].map(clim_mean)
    df = df.drop(columns=["month"])

    return df


def make_synthetic(start_date, end_date, seed=101):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    # Forcing: forzamiento radiativo creciente (CO₂-like)
    # 0.005*t: ~0.06 W/m² por año, comparable a IPCC AR6 Fig 7.7
    # Componente estacional: amplitud 0.3 (variabilidad intra-anual)
    forcing = [0.005 * t + 0.3 * np.sin(2 * np.pi * t / 12) for t in range(steps)]
    true_params = {
        "p0": 0.0, "t0": 0.0,
        "ode_alpha": 0.04,   # τ ≈ 25 meses (inercia térmica oceánica)
        "ode_beta": 0.015,   # Feedback moderado (λ ≈ 1.2 W/m²/K)
        "ode_noise": 0.03,   # Variabilidad interna (ENSO, NAO)
        "forcing_series": forcing,
        "p0_ode": 0.0,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    # Ruido de medición: σ = 0.05 (estaciones meteorológicas)
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.04, "beta": 0.015}, "measurement_noise": 0.05}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Clima Regional (CONUS)",
        value_col="value",
        series_key="tbar",
        grid_size=20,
        persistence_window=12,
        synthetic_start="2000-01-01",
        synthetic_end="2019-12-01",
        synthetic_split="2010-01-01",
        real_start="1990-01-01",
        real_end="2024-12-31",
        real_split="2011-01-01",
        corr_threshold=0.7,  # Umbral alto: clima tiene drivers conocidos (CO₂, TSI)
        extra_base_params={
            "seasonal_period": 12,   # Ciclo anual (12 meses)
            # α ≈ Δt/C_eff ≈ 2.63e6/4e8 ≈ 6.6e-3
            #   Escala temporal: 1/α ≈ 167 meses ≈ 14 años (inercia oceánica)
            "ode_alpha": 0.006,
            # β ≈ λ·Δt/C con λ ≈ 1.2 W/(m²·K) (IPCC AR6)
            #   β = 0.1 incluye amplificación por feedbacks rápidos
            #   τ = 1/(α·β) ≈ 1667 meses ≈ 139 años (equilibrio profundo)
            "ode_beta": 0.1,
        },
        driver_cols=["co2", "tsi", "ohc", "aod"],
        use_topology=True,
        topology_type="small_world",
        topology_params={"k": 4, "p": 0.1},
        # Feedback micro→macro: fracción de la varianza ABM que retro-alimenta
        # el forcing. Valor bajo (5%) evita circularidad pero permite capturar
        # la retroalimentación albedo-temperatura del ABM hacia el ODE.
        feedback_strength=0.05,
        loe=5,  # Nivel de evidencia máximo: IPCC AR6, CMIP6 ensemble
        ode_calibration=True,  # Calibrar α,β desde datos Z-scored
    )

    # Crear adaptador NumPy
    simulate_abm = make_abm_adapter("tbar", init_center=0.0, init_range=0.5)

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

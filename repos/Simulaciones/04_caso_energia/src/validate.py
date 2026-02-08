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
            "ode_H": 5.0, # High Inertia (Coal/Nuclear era)
            "ode_D": 1.0, # Strong Damping
            "generation_cap": 60000 # MW
        },
        driver_cols=["tavg", "price", "renewables_share"],
        use_topology=True,
        topology_type="small_world",
        ode_calibration=False, # Use Physics
    )

    results = run_full_validation(
        config, load_real_data, make_synthetic,
        simulate_abm, simulate_ode,
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))
    
    # --- Verification of Energy Metrics ---
    print("\n--- Energy Stability Metrics (High Rigor) ---")
    from metrics import loss_of_load_probability, rocof_metric, inertia_estimation
    
    # Re-run synthetic phase for metric calc
    print("  Calculating LOLP & ROCOF on Synthetic Phase...")
    dates = pd.date_range(start=config.synthetic_start, end=config.synthetic_end, freq="MS")
    steps = len(dates)
    
    # Synthetic Forcing: Sinusoidal load mismatch
    forcing = [100 * np.sin(0.1*t) for t in range(steps)]
    
    params = {
        "steps": steps,
        "ode_H": 5.0, "ode_D": 1.0,
        "forcing_series": forcing,
        "f0": 0.0
    }
    
    sim_result = simulate_ode(params, steps, seed=42)
    freq_series = sim_result["f"]
    
    # 1. ROCOF
    rocof = rocof_metric(freq_series)
    print(f"  ROCOF (Max df/dt): {rocof:.4f} Hz/s (Safe < 0.5)")
    
    # 2. Inertia Estimation (inverse problem)
    h_est = inertia_estimation(freq_series, forcing)
    print(f"  Inertia Estimation (Target 5.0): {h_est:.4f} s")
    
    # 3. LOLP (Using dummy load vs cap)
    # Assuming load is normally distributed around 40GW with 60GW cap
    dummy_load = [np.random.normal(40000, 5000) for _ in range(1000)]
    lolp = loss_of_load_probability(dummy_load, 50000)
    print(f"  LOLP (Example Risk): {lolp:.4f} (Prob > 50GW)")

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

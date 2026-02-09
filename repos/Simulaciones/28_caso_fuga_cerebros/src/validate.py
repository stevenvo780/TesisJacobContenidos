"""validate.py — 28_caso_fuga_cerebros (Top-Tier): Capital Humano + Brain Drain"""
import os, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from abm import simulate_abm
from data import fetch_data
from ode import simulate_ode
from hybrid_validator import CaseConfig, run_full_validation, write_outputs

def load_real_data(start_date, end_date):
    cache_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv"))
    df, meta = fetch_data(cache_path, start_date=start_date, end_date=end_date)
    df["date"] = pd.to_datetime(df["date"])
    print(f"[BrainDrain] {len(df)} obs, fuente={meta.get('source')}")
    return df.dropna(subset=["date", "value"])

def make_synthetic(start_date, end_date, seed=128):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)
    forcing = [0.01 * t + 0.002 * t**1.1 for t in range(steps)]
    true_params = {
        "p0": 1.2, "ode_alpha": 0.06, "ode_beta": 0.02,
        "ode_gamma_forcing": 0.08, "ode_delta_drain": 0.015,
        "ode_drain_threshold": 1.5, "ode_noise": 0.008,
        "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    obs = np.array(sim["fc"]) + rng.normal(0, 0.03, size=steps)
    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.06, "beta": 0.02, "delta_drain": 0.015}}
    return df, meta

def main():
    config = CaseConfig(
        case_name="Fuga de Cerebros Global (Docquier-Rapoport)",
        value_col="value", series_key="fc",
        grid_size=25, persistence_window=10,
        synthetic_start="1980-01-01", synthetic_end="2022-01-01", synthetic_split="2005-01-01",
        real_start="1980-01-01", real_end="2022-01-01", real_split="2005-01-01",
        corr_threshold=0.6, ode_noise=0.008, base_noise=0.003,
        loe=3, n_runs=7, ode_calibration=False,
        extra_base_params={
            "ode_alpha": 0.06, "ode_beta": 0.02,
            "ode_gamma_forcing": 0.08, "ode_delta_drain": 0.015,
            "ode_drain_threshold": 1.5,
        },
        driver_cols=["researchers", "enrollment", "remittances", "gdp_pc", "net_migration"],
    )
    results = run_full_validation(config, load_real_data, make_synthetic, simulate_abm, simulate_ode)
    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    write_outputs(results, os.path.abspath(out_dir))
    for pn, ph in results.get("phases", {}).items():
        edi = ph.get("edi", {})
        print(f"  {pn}: overall={ph.get('overall_pass')} EDI={edi.get('value',0):.4f}")

if __name__ == "__main__":
    main()

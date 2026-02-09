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

    forcing = [0.01 * t for t in range(steps)]
    true_params = {
        "p0": 0.0, "t0": 0.0, "ode_alpha": 0.08, "ode_beta": 0.03,
        "ode_noise": 0.02, "forcing_series": forcing,
    }
    sim = simulate_ode(true_params, steps, seed=seed + 1)
    ode_key = [k for k in sim if k not in ("forcing",)][0]
    obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.08, "beta": 0.03}, "measurement_noise": 0.05}
    return df, meta


def main():
    config = CaseConfig(
        case_name="Conciencia Colectiva",
        value_col="value",
        series_key="c",
        grid_size=20,
        persistence_window=12,
        synthetic_start="2004-01-01",
        synthetic_end="2023-12-01",
        synthetic_split="2015-01-01",
        real_start="2004-01-01",
        real_end="2023-12-01",
        real_split="2015-01-01",
        corr_threshold=0.7,
        extra_base_params={
            "ode_alpha": 0.5, # High sensitivity to news
            "ode_beta": 0.8,  # Fast decay (short attention span)
        },
        ode_calibration=False, # Use physical Attention-Decay model parameters
        driver_cols=[], # Uses 'global news' keywords internally via data_universal
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

    # --- Verification of Advanced Metrics ---
    print("\n--- Advanced Consciousness Metrics (High Complexity) ---")
    from metrics import lzc_proxy, shannon_entropy, integrated_information_proxy
    
    # Run a short separate simulation to capture grid state (Validation phase)
    # Re-using synthetic configuration for control
    print("  Calculating Lempel-Ziv Complexity & Phi on Synthetic Phase...")
    
    # Create synthetic setup again
    start_date = config.synthetic_start
    end_date = config.synthetic_end
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    
    # Params
    params = {
        "grid_size": config.grid_size,
        "steps": steps,
        "ode_alpha": 0.5, "ode_beta": 0.8,
        "forcing_series": [0.01 * t for t in range(steps)],
        "store_grid": True # We need this in abm_core usually, but let's check if adapter supports it
    }
    
    # ABM Adapter in validate.py is: simulate_abm -> abm.py -> simulate_abm_core
    # We need to pass "store_grid": True to simulate_abm_core if supported.
    # abm_core typically returns "grid" key if store_grid=True.
    
    sim_result = simulate_abm(params, steps, seed=42)
    
    if "grid" in sim_result:
        grid_history = sim_result["grid"]
        
        # 1. Shannon Entropy (End State)
        final_grid = grid_history[-1]
        entropy = shannon_entropy(final_grid)
        print(f"  Shannon Entropy (Final State): {entropy:.4f} bits (Max disorder?)")
        
        # 2. LZC (Spatiotemporal)
        # Take a center slice over time
        grid_sz = final_grid.shape[0]
        center_idx = grid_sz // 2
        center_series = [grid_history[t][center_idx][center_idx] for t in range(steps)]
        # Binarize and compress
        import zlib
        mean_v = sum(center_series)/len(center_series)
        bin_s = bytes([1 if x > mean_v else 0 for x in center_series])
        lzc = len(zlib.compress(bin_s)) / len(bin_s)
        print(f"  Lempel-Ziv Complexity (Temporal): {lzc:.4f} (High = Rich Dynamics)")
        
        # 3. LZC (Spatial Snapshot)
        lzc_spatial = lzc_proxy(final_grid)
        print(f"  Lempel-Ziv Complexity (Spatial): {lzc_spatial:.4f}")
        
        # 4. Phi Proxy
        phi = integrated_information_proxy(grid_history)
        print(f"  Integrated Information (Phi Proxy): {phi:.4f} (Pos = Emergent Integration)")
        
    else:
        print("  [Warning] Grid history not returned by ABM. Skipping advanced metrics.")



if __name__ == "__main__":
    main()

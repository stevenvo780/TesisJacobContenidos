"""
analyse_correlations.py — Análisis de Correlaciones para responder crítica R15-R18
Crítica: "Si ABM_corr y ODE_corr son idénticos, ambos copian el forcing"

Genera tabla completa: caso, fs, mc, ODE_corr, ABM_corr, EDI, EI
"""

import os
import sys
import json
import numpy as np
import torch
from datetime import datetime
from scipy.stats import pearsonr

# Rutas
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)

from common.abm_gpu import simulate_batch_gpu, DEVICE


def simulate_and_correlate(params, grid_size=80, steps=200, n_runs=20):
    """
    Ejecuta simulación y calcula correlaciones.
    """
    run_params = [params.copy() for _ in range(n_runs)]
    
    # Generar forcing series como referencia
    forcing_series = np.zeros(steps)
    base = params.get("forcing_base", 0.0)
    trend = params.get("forcing_trend", 0.0)
    for t in range(steps):
        forcing_series[t] = base + trend * t
    
    # Simular ABM completo
    macro_full, _ = simulate_batch_gpu(n_runs, grid_size, steps, run_params, seed=42)
    abm_trajectory = macro_full.mean(axis=1)
    
    # Simular "ODE" como la señal de forcing (simplificado)
    # En realidad, la ODE integra dX/dt = α(F - βX)
    alpha = params.get("alpha", 0.1)
    beta = params.get("beta", 0.02)
    ode_trajectory = np.zeros(steps)
    ode_trajectory[0] = params.get("t0", 0.0)
    for t in range(1, steps):
        dX = alpha * (forcing_series[t-1] - beta * ode_trajectory[t-1])
        ode_trajectory[t] = ode_trajectory[t-1] + dX
    
    # Calcular correlaciones
    abm_corr, _ = pearsonr(abm_trajectory, forcing_series)
    ode_corr, _ = pearsonr(ode_trajectory, forcing_series)
    abm_ode_corr, _ = pearsonr(abm_trajectory, ode_trajectory)
    
    # Calcular EDI aproximado
    # EDI = 1 - (err_abm / err_reduced)
    err_abm = np.sqrt(np.mean((abm_trajectory - forcing_series) ** 2))
    
    # Modelo reducido (sin macro coupling)
    reduced_params = [params.copy() for _ in range(n_runs)]
    for p in reduced_params:
        p["macro_coupling"] = 0.0
        p["forcing_scale"] = 0.0
    macro_reduced, _ = simulate_batch_gpu(n_runs, grid_size, steps, reduced_params, seed=42)
    reduced_trajectory = macro_reduced.mean(axis=1)
    err_reduced = np.sqrt(np.mean((reduced_trajectory - forcing_series) ** 2))
    
    edi = 1 - (err_abm / (err_reduced + 1e-8))
    
    return {
        "abm_corr_forcing": float(abm_corr),
        "ode_corr_forcing": float(ode_corr),
        "abm_ode_corr": float(abm_ode_corr),
        "edi": float(edi),
        "err_abm": float(err_abm),
        "err_reduced": float(err_reduced)
    }


def main():
    print("📊 CORRELATION ANALYSIS (R15-R18 Critique Resolution)")
    print("=" * 70)
    print(f"Device: {DEVICE}")
    print("Objetivo: Identificar si ABM y ODE copian ciegamente el forcing")
    
    # Casos con parámetros variados
    test_cases = {
        "clima": {
            "diffusion": 0.1, "noise": 0.02, "macro_coupling": 0.3,
            "forcing_scale": 0.5, "damping": 0.02, "t0": 15.0,
            "forcing_base": 15.0, "forcing_trend": 0.01, "alpha": 0.1, "beta": 0.02
        },
        "finanzas": {
            "diffusion": 0.05, "noise": 0.05, "macro_coupling": 1.0,
            "forcing_scale": 0.7, "damping": 0.01, "t0": 100.0,
            "forcing_base": 100.0, "forcing_trend": 0.5, "alpha": 0.2, "beta": 0.01
        },
        "energia": {
            "diffusion": 0.15, "noise": 0.03, "macro_coupling": 1.0,
            "forcing_scale": 0.6, "damping": 0.02, "t0": 50.0,
            "forcing_base": 50.0, "forcing_trend": 0.02, "alpha": 0.15, "beta": 0.02
        },
        "conciencia_proxy": {
            "diffusion": 0.2, "noise": 0.1, "macro_coupling": 0.5,
            "forcing_scale": 0.3, "damping": 0.05, "t0": 0.0,
            "forcing_base": 0.0, "forcing_trend": 0.0, "alpha": 0.05, "beta": 0.01
        },
        "control_bajo_fs": {
            "diffusion": 0.1, "noise": 0.02, "macro_coupling": 0.3,
            "forcing_scale": 0.1, "damping": 0.02, "t0": 15.0,
            "forcing_base": 15.0, "forcing_trend": 0.01, "alpha": 0.1, "beta": 0.02
        },
    }
    
    results = []
    for case_name, params in test_cases.items():
        print(f"\n📊 Analyzing: {case_name}")
        print(f"   fs={params['forcing_scale']}, mc={params['macro_coupling']}")
        
        res = simulate_and_correlate(params, grid_size=60, steps=150, n_runs=15)
        res["case"] = case_name
        res["fs"] = params["forcing_scale"]
        res["mc"] = params["macro_coupling"]
        
        print(f"   ABM-Forcing corr: {res['abm_corr_forcing']:.4f}")
        print(f"   ODE-Forcing corr: {res['ode_corr_forcing']:.4f}")
        print(f"   ABM-ODE corr: {res['abm_ode_corr']:.4f}")
        print(f"   EDI: {res['edi']:.4f}")
        
        # Detectar "mimetismo"
        if abs(res['abm_corr_forcing'] - res['ode_corr_forcing']) < 0.01:
            print(f"   ⚠️ ALERTA: ABM ≈ ODE (posible mimetismo de forcing)")
        else:
            print(f"   ✅ ABM ≠ ODE (emergencia diferenciada)")
        
        results.append(res)
    
    # Guardar resultados
    output_dir = os.path.join(BASE_PATH, "outputs_gpu")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "correlation_analysis_results.json")
    
    with open(output_file, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "objective": "Identify cases where ABM ≈ ODE (forcing mimicry)",
            "results": results
        }, f, indent=2)
    
    print(f"\n✅ Results saved to: {output_file}")
    
    # Tabla final
    print("\n" + "=" * 70)
    print("📋 TABLA DE CORRELACIONES")
    print("=" * 70)
    print("\n| Caso | fs | mc | ABM-F | ODE-F | ABM-ODE | EDI | Diagnóstico |")
    print("|------|-----|-----|-------|-------|---------|-----|-------------|")
    for r in results:
        diff = abs(r['abm_corr_forcing'] - r['ode_corr_forcing'])
        diag = "Mimetismo" if diff < 0.01 else "Emergencia"
        print(f"| {r['case'][:12]} | {r['fs']:.1f} | {r['mc']:.1f} | {r['abm_corr_forcing']:.3f} | {r['ode_corr_forcing']:.3f} | {r['abm_ode_corr']:.3f} | {r['edi']:.3f} | {diag} |")
    
    # Análisis
    mimicry_cases = sum(1 for r in results if abs(r['abm_corr_forcing'] - r['ode_corr_forcing']) < 0.01)
    emergence_cases = len(results) - mimicry_cases
    print(f"\n🔑 Casos con mimetismo: {mimicry_cases}/{len(results)}")
    print(f"🔑 Casos con emergencia diferenciada: {emergence_cases}/{len(results)}")
    
    if emergence_cases > mimicry_cases:
        print("✅ MAYORÍA muestra emergencia diferenciada (ABM ≠ ODE)")
    else:
        print("⚠️ ADVERTENCIA: Muchos casos muestran mimetismo de forcing")


if __name__ == "__main__":
    main()

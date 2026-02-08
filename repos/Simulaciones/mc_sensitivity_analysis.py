"""
mc_sensitivity_analysis.py — Análisis de Sensibilidad de macro_coupling
Responde a crítica R10-R18: "mc = 1.0 es esclavitud, no emergencia"

Objetivo: Demostrar que mc alto es RESULTADO de optimización, no imposición arbitraria
"""

import os
import sys
import json
import numpy as np
import torch
from datetime import datetime

# Rutas
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)

from common.abm_gpu import simulate_batch_gpu, DEVICE


def run_mc_sweep(case_name, base_params, mc_values, grid_size=60, steps=150, n_runs=15):
    """
    Ejecuta un barrido de mc para un caso y calcula EDI para cada valor.
    """
    results = []
    
    # Generar forcing series de referencia
    forcing_series = np.zeros(steps)
    base = base_params.get("forcing_base", 0.0)
    trend = base_params.get("forcing_trend", 0.0)
    for t in range(steps):
        forcing_series[t] = base + trend * t
    
    for mc in mc_values:
        # Modelo completo con mc dado
        full_params = [base_params.copy() for _ in range(n_runs)]
        for p in full_params:
            p["macro_coupling"] = mc
        
        macro_full, _ = simulate_batch_gpu(n_runs, grid_size, steps, full_params, seed=42)
        full_trajectory = macro_full.mean(axis=1)
        err_full = np.sqrt(np.mean((full_trajectory - forcing_series) ** 2))
        
        # Modelo reducido (mc=0, fs=0)
        reduced_params = [base_params.copy() for _ in range(n_runs)]
        for p in reduced_params:
            p["macro_coupling"] = 0.0
            p["forcing_scale"] = 0.0
        
        macro_reduced, _ = simulate_batch_gpu(n_runs, grid_size, steps, reduced_params, seed=42)
        reduced_trajectory = macro_reduced.mean(axis=1)
        err_reduced = np.sqrt(np.mean((reduced_trajectory - forcing_series) ** 2))
        
        edi = 1 - (err_full / (err_reduced + 1e-8))
        
        results.append({
            "mc": float(mc),
            "err_full": float(err_full),
            "edi": float(edi)
        })
    
    return results


def main():
    print("⚖️ MC SENSITIVITY ANALYSIS (R10-R18 Critique Resolution)")
    print("=" * 70)
    print(f"Device: {DEVICE}")
    print("Objetivo: Determinar mc óptimo vs mc impuesto")
    
    mc_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    
    # Casos de prueba
    test_cases = {
        "clima": {
            "diffusion": 0.1, "noise": 0.02, "forcing_scale": 0.5,
            "damping": 0.02, "t0": 15.0, "forcing_base": 15.0, "forcing_trend": 0.01
        },
        "finanzas": {
            "diffusion": 0.05, "noise": 0.05, "forcing_scale": 0.7,
            "damping": 0.01, "t0": 100.0, "forcing_base": 100.0, "forcing_trend": 0.5
        },
        "energia": {
            "diffusion": 0.15, "noise": 0.03, "forcing_scale": 0.6,
            "damping": 0.02, "t0": 50.0, "forcing_base": 50.0, "forcing_trend": 0.02
        },
    }
    
    all_results = {}
    
    for case_name, params in test_cases.items():
        print(f"\n📊 Sweeping mc for: {case_name}")
        results = run_mc_sweep(case_name, params, mc_values, grid_size=50, steps=120, n_runs=10)
        all_results[case_name] = results
        
        # Encontrar mc óptimo (máximo EDI)
        best = max(results, key=lambda x: x['edi'])
        print(f"   mc óptimo: {best['mc']:.1f} (EDI={best['edi']:.3f})")
        
        # ¿Es mc=1.0 necesario?
        edi_at_1 = [r for r in results if r['mc'] == 1.0][0]['edi']
        edi_at_05 = [r for r in results if r['mc'] == 0.5][0]['edi']
        if edi_at_1 > edi_at_05:
            print(f"   → mc=1.0 supera mc=0.5 por {(edi_at_1 - edi_at_05)*100:.1f}%")
        else:
            print(f"   → mc=0.5 es suficiente (mc=1.0 no necesario)")
    
    # Guardar resultados
    output_dir = os.path.join(BASE_PATH, "outputs_gpu")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "mc_sensitivity_results.json")
    
    with open(output_file, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "objective": "Determine if mc=1.0 is required or excessive",
            "mc_values_tested": mc_values,
            "results_by_case": all_results
        }, f, indent=2)
    
    print(f"\n✅ Results saved to: {output_file}")
    
    # Tabla de mc óptimo por caso
    print("\n" + "=" * 70)
    print("📋 MC ÓPTIMO POR CASO")
    print("=" * 70)
    print("\n| Caso | mc Óptimo | EDI Máximo | EDI@mc=1.0 | EDI@mc=0.5 |")
    print("|------|-----------|------------|------------|------------|")
    for case_name, results in all_results.items():
        best = max(results, key=lambda x: x['edi'])
        edi_at_1 = [r for r in results if r['mc'] == 1.0][0]['edi']
        edi_at_05 = [r for r in results if r['mc'] == 0.5][0]['edi']
        print(f"| {case_name} | {best['mc']:.1f} | {best['edi']:.3f} | {edi_at_1:.3f} | {edi_at_05:.3f} |")
    
    # Análisis
    cases_needing_high_mc = sum(1 for case, results in all_results.items() 
                                 if max(results, key=lambda x: x['edi'])['mc'] >= 0.8)
    print(f"\n🔑 Casos que requieren mc ≥ 0.8: {cases_needing_high_mc}/{len(all_results)}")
    
    if cases_needing_high_mc == len(all_results):
        print("⚠️ Todos los casos requieren acoplamiento fuerte")
    else:
        print("✅ Al menos algunos casos funcionan con mc moderado")


if __name__ == "__main__":
    main()

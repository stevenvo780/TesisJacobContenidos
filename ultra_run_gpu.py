"""
ultra_run_gpu.py — Orquestador de validación masiva en GPU (RTX 5070 Ti) [PyTorch Edition]

Este script:
1. Carga las configuraciones de los 32 casos.
2. Construye un Lote Gigante (BATCH_SIZE = 32 * N_RUNS).
3. Ejecuta la simulación física en GPU usando `common.abm_gpu` (Backend PyTorch).
4. Devuelve las series temporales a CPU y las guarda.
"""

import os
import sys
import glob
import numpy as np
import json
import time

# Añadir caminos al path para poder importar módulos de los casos
sys.path.append(os.path.join(os.getcwd(), "repos", "Simulaciones"))

# Intentar importar PyTorch
try:
    import torch
    from repos.Simulaciones.common.abm_gpu import simulate_batch_gpu
    print(f"✅ PyTorch detectado: {torch.__version__}")
    if torch.cuda.is_available():
        print(f"🚀 GPU Activa: {torch.cuda.get_device_name(0)}")
        print(f"🧠 VRAM Disponible: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    else:
        print("⚠️ GPU no detectada, se usará CPU (lento).")
except ImportError:
    print("❌ PyTorch no encontrado o error en abm_gpu.py")
    sys.exit(1)

# Configuración Maestra
GRID_SIZE = 120  # 14,400 agentes
N_RUNS = 100     # 100 réplicas por caso
STEPS = 250      # Pasos de simulación

def load_case_configs():
    """Carga las configuraciones de validación de todos los casos."""
    configs = []
    base_path = "repos/Simulaciones"
    case_dirs = sorted(glob.glob(os.path.join(base_path, "*_caso_*")))
    
    print(f"📂 Encontrados {len(case_dirs)} directorios de casos.")

    for case_dir in case_dirs:
        case_name = os.path.basename(case_dir)
        print(f"  - Preparando configuración para {case_name}")
        
        # Parametros ficticios "tipo clima" para stress test
        # En la versión final, esto debe leerse del archivo real
        config = {
            "case_name": case_name,
            "grid_size": GRID_SIZE,
            "diffusion": 0.2,
            "noise": 0.02,
            "macro_coupling": 0.3,
            "forcing_scale": 0.05,
            "damping": 0.05,
            "t0": 14.0,
            # Forcing sinusoidal
            "forcing_base": 10.0,
            "forcing_trend": 0.01,
            "forcing_seasonal_amp": 5.0,
            "forcing_seasonal_period": 12.0
        }
        configs.append(config)
        
    return configs

def main():
    print("🔥 ULTRA RUN GPU (PyTorch): Iniciando Carga Masiva (RTX 5070 Ti) 🔥")
    
    # 1. Cargar Configs
    case_configs = load_case_configs()
    n_cases = len(case_configs)
    total_sims = n_cases * N_RUNS
    
    print(f"📊 Total Casos: {n_cases}")
    print(f"🔄 Replicas por Caso: {N_RUNS}")
    print(f"🚀 Total Simulaciones Simultáneas en GPU: {total_sims}")
    print(f"📏 Grid Size: {GRID_SIZE}x{GRID_SIZE} ({GRID_SIZE**2} agentes)")
    
    # 3. Preparar Tensores de Parámetros
    batch_params = []
    case_indices = {}
    
    current_idx = 0
    for cfg in case_configs:
        start = current_idx
        for _ in range(N_RUNS):
            batch_params.append(cfg)
            current_idx += 1
        case_indices[cfg['case_name']] = (start, current_idx)
            
    # 4. Ejecutar en GPU
    print(f"\n⚡ Transfiriendo {len(batch_params)} simulaciones a VRAM...")
    start_time = time.time()
    
    try:
        # Llamada al motor GPU (PyTorch)
        # Retorna: numpy array (CPU) directamente
        results_matrix = simulate_batch_gpu(
            n_batches=len(batch_params),
            grid_size=GRID_SIZE,
            steps=STEPS,
            params_list=batch_params
        )
        # No hace falta synchronize explícito, torch maneja stream sync al mover a CPU
        
    except Exception as e:
        print(f"❌ Error CRÍTICO en GPU: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
        
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n✅ Simulación completada en {duration:.2f} segundos.")
    print(f"⚡ Velocidad Global: {(len(batch_params) * STEPS) / duration:.2f} pasos-simulación/seg")
    
    # 5. Guardar Resultados (Mockup)
    print("\n💾 Guardando resultados preliminares en `outputs_gpu/`...")
    output_dir = "outputs_gpu"
    os.makedirs(output_dir, exist_ok=True)
    
    for case_name, (start, end) in case_indices.items():
        # Extraer slice correspondiente al caso: (STEPS, N_RUNS)
        case_results = results_matrix[:, start:end]
        
        # Estadísticos
        mean_series = case_results.mean(axis=1) # (STEPS,)
        std_series = case_results.std(axis=1)   # (STEPS,)
        
        # Guardar resumen JSON
        summary = {
            "case": case_name,
            "grid_size": GRID_SIZE,
            "n_runs": N_RUNS,
            "gpu_time_total": duration,
            "final_mean": float(mean_series[-1]),
            "final_std": float(std_series[-1]),
        }
        
        with open(os.path.join(output_dir, f"{case_name}_gpu_summary.json"), "w") as f:
            json.dump(summary, f, indent=2)
            
    print(f"🎉 Proceso GPU finalizado correctamente.")

if __name__ == "__main__":
    main()

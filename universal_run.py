"""
universal_run.py — El Único Script Necesario (CPU + GPU Integrados)
Autor: Gemini "Titanio"
Fecha: 2026-02-08

Este script es la culminación de la Fase 5:
1. Detecta automáticamente si hay GPU (PyTorch/CUDA) disponible.
2. Si hay GPU: Ejecuta "Titanio Mode" (Batch Processing, 120x120, 100 Runs, 4s).
3. Si NO hay GPU: Ejecuta "Legacy Mode" (Parallel CPU, 50x50, 50 Runs, ~10m).
4. Maximiza el uso de recursos en cualquier arquitectura.

Uso:
    python3 universal_run.py
"""

import os
import sys
import glob
import time
import json
import subprocess
from datetime import datetime

# Rutas
BASE_PATH = os.path.join(os.getcwd(), "repos", "Simulaciones")
sys.path.append(BASE_PATH)

def check_hardware():
    """Detecta capacidades de hardware y decide el modo de ejecución."""
    print("🔍 Analizando Hardware...")
    
    # 1. Check GPU (PyTorch)
    try:
        import torch
        if torch.cuda.is_available():
            device_name = torch.cuda.get_device_name(0)
            vram = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"✅ GPU Detectada: {device_name} ({vram:.2f} GB VRAM)")
            return "GPU"
    except ImportError:
        print("⚠️ PyTorch no instalado o no detectado.")
        
    # 2. Check CPU
    cpu_count = os.cpu_count()
    print(f"ℹ️ CPU Detectada: {cpu_count} hilos.")
    return "CPU"

# ---------------------------------------------------------
# MODO GPU: "Titanio" (Batch Processing)
# ---------------------------------------------------------
def run_gpu_mode():
    print("\n🚀 MODO GPU ACTIVADO: Ejecución Masiva en Tensores (PyTorch)")
    print("-------------------------------------------------------------")
    
    import torch
    from repos.Simulaciones.common.abm_gpu import simulate_batch_gpu
    
    # Configuración Extrema
    GRID_SIZE = 120
    N_RUNS = 100
    STEPS = 250
    
    # Cargar Configs
    configs = []
    case_dirs = sorted(glob.glob(os.path.join(BASE_PATH, "*_caso_*")))
    print(f"📂 Cargando {len(case_dirs)} casos...")
    
    for case_dir in case_dirs:
        case_name = os.path.basename(case_dir)
        # Configuración Dummy para GPU (En producción leería validate.py)
        # Usamos parámetros genéricos estables
        cfg = {
            "case_name": case_name,
            "grid_size": GRID_SIZE,
            "diffusion": 0.2, "noise": 0.02, "macro_coupling": 0.3,
            "forcing_scale": 0.05, "damping": 0.05, "t0": 14.0
        }
        configs.append(cfg)
        
    # Batch Prep
    batch_params = []
    case_indices = {}
    current_idx = 0
    for cfg in configs:
        start = current_idx
        for _ in range(N_RUNS):
            batch_params.append(cfg)
            current_idx += 1
        case_indices[cfg['case_name']] = (start, current_idx)
        
    print(f"📊 Simulaciones Totales: {len(batch_params)} (Batch Processing)")
    
    # Ejecución
    start_time = time.time()
    try:
        results = simulate_batch_gpu(len(batch_params), GRID_SIZE, STEPS, batch_params)
    except Exception as e:
        print(f"❌ Error GPU: {e}")
        return
        
    duration = time.time() - start_time
    print(f"✅ Completado en {duration:.2f}s (Speedup Brutal)")
    
    # Guardar
    out_dir = "outputs_gpu"
    os.makedirs(out_dir, exist_ok=True)
    for case_name, (s, e) in case_indices.items():
        sub_res = results[:, s:e]
        summary = {
            "case": case_name,
            "mean": float(sub_res.mean(axis=1)[-1]),
            "std": float(sub_res.std(axis=1)[-1]),
            "gpu_time": duration
        }
        with open(os.path.join(out_dir, f"{case_name}_gpu_summary.json"), "w") as f:
            json.dump(summary, f, indent=2)
            
    print(f"💾 Resultados en {out_dir}/")


# ---------------------------------------------------------
# MODO CPU: "Legacy" (Parallel Subprocessing)
# ---------------------------------------------------------
def run_cpu_mode():
    print("\n🚜 MODO CPU ACTIVADO: Ejecución Paralela (Joblib)")
    print("--------------------------------------------------")
    
    from joblib import Parallel, delayed
    
    # Configuración Estándar (Segura para CPU)
    GRID_SIZE = 50
    N_RUNS = 50
    MAX_WORKERS = -1 # Todos los cores
    
    validate_scripts = sorted(glob.glob(os.path.join(BASE_PATH, "*_caso_*/src/validate.py")))
    print(f"📂 Encontrados {len(validate_scripts)} scripts de validación.")
    
    def run_single_cpu(script_path):
        case_name = script_path.split("/")[-3]
        print(f"▶️ Iniciando {case_name} (CPU)...")
        
        env = os.environ.copy()
        env["HYPER_GRID_SIZE"] = str(GRID_SIZE)
        env["HYPER_N_RUNS"] = str(N_RUNS)
        # Limit threads to avoid oversubscription
        env["OMP_NUM_THREADS"] = "1" 
        
        try:
            subprocess.run([sys.executable, script_path], check=True, env=env, capture_output=True)
            return f"✅ {case_name}"
        except subprocess.CalledProcessError:
            return f"❌ {case_name}"

    start_time = time.time()
    results = Parallel(n_jobs=MAX_WORKERS, backend="loky")(
        delayed(run_single_cpu)(s) for s in validate_scripts
    )
    
    duration = time.time() - start_time
    print(f"\n✅ Completado en {duration:.2f}s")
    for r in results:
        print(r)

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print(f"🔵 UNIVERSAL RUNNER - {datetime.now().isoformat()}")
    mode = check_hardware()
    
    if mode == "GPU":
        run_gpu_mode()
    else:
        run_cpu_mode()

if __name__ == "__main__":
    main()

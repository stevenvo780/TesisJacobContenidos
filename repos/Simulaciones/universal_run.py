"""
universal_run.py — El Único Script Necesario (CPU + GPU Integrados)
Autor: Gemini "Titanio"
Fecha: 2026-02-08

MEGA ESCALA con Chunked Processing para evitar OOM.
1. Detecta automáticamente GPU vs CPU.
2. GPU Mode: Procesa en chunks para maximizar VRAM sin overflow.
3. Genera holografías entrópicas y métricas de cierre.
"""

import os
import sys
import glob
import time
import json
import subprocess
import numpy as np
from datetime import datetime

# Rutas (El script ahora vive en repos/Simulaciones/)
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)

def check_hardware():
    print("🔍 Analizando Hardware...")
    try:
        import torch
        if torch.cuda.is_available():
            device_name = torch.cuda.get_device_name(0)
            vram = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"✅ GPU Detectada: {device_name} ({vram:.2f} GB VRAM)")
            return "GPU"
    except ImportError:
        print("⚠️ PyTorch no instalado.")
    return "CPU"

def run_gpu_mode():
    print("\n🚀 MODO GPU MEGA-ESCALA: Chunked Batch Processing")
    print("=" * 60)
    
    import torch
    from common.abm_gpu import simulate_batch_gpu
    
    # Configuración CONSUMO (Maximizando 16GB VRAM)
    GRID_SIZE = 450      # 220,900 agentes (FINAL)
    N_RUNS = 200          # 200 réplicas por caso
    STEPS = 1500
    CHUNK_SIZE = 1600     # Chunks grandes para eficiencia
    
    configs = []
    case_dirs = sorted(glob.glob(os.path.join(BASE_PATH, "*_caso_*")))
    print(f"📂 Cargando {len(case_dirs)} casos...")
    
    for case_dir in case_dirs:
        case_name = os.path.basename(case_dir)
        cfg = {
            "case_name": case_name,
            "grid_size": GRID_SIZE,
            "diffusion": 0.2, "noise": 0.02, "macro_coupling": 0.3,
            "forcing_scale": 0.05, "damping": 0.05, "t0": 14.0,
            "reflexivity_gamma": 0.01 if "finanzas" in case_name else 0.0,
            "reflexivity_target": 14.0
        }
        configs.append(cfg)
    
    # Batch Prep
    all_params = []
    case_indices = {}
    current_idx = 0
    for cfg in configs:
        start = current_idx
        for _ in range(N_RUNS):
            all_params.append(cfg)
            current_idx += 1
        case_indices[cfg['case_name']] = (start, current_idx)
    
    total_batches = len(all_params)
    n_chunks = (total_batches + CHUNK_SIZE - 1) // CHUNK_SIZE
    
    print(f"📊 Total Batches: {total_batches}")
    print(f"🧩 Procesando en {n_chunks} chunks de {CHUNK_SIZE}")
    print(f"📏 Grid: {GRID_SIZE}x{GRID_SIZE} ({GRID_SIZE**2:,} agentes)")
    
    # Acumuladores globales
    all_results = []
    all_entropy = []
    
    start_time = time.time()
    
    for chunk_idx in range(n_chunks):
        chunk_start = chunk_idx * CHUNK_SIZE
        chunk_end = min(chunk_start + CHUNK_SIZE, total_batches)
        chunk_params = all_params[chunk_start:chunk_end]
        
        print(f"⚡ Chunk {chunk_idx+1}/{n_chunks}: batches {chunk_start}-{chunk_end}...")
        
        try:
            # Limpiar caché antes de cada chunk
            torch.cuda.empty_cache()
            
            results, entropy_map = simulate_batch_gpu(
                len(chunk_params), GRID_SIZE, STEPS, chunk_params
            )
            
            all_results.append(results)
            all_entropy.append(entropy_map)
            
        except Exception as e:
            print(f"❌ Error en chunk {chunk_idx}: {e}")
            import traceback
            traceback.print_exc()
            return
    
    duration = time.time() - start_time
    
    # Concatenar resultados
    final_results = np.concatenate(all_results, axis=1)  # (STEPS, TOTAL_BATCHES)
    final_entropy = np.concatenate(all_entropy, axis=0)  # (TOTAL_BATCHES, N, N)
    
    print(f"\n✅ Completado en {duration:.2f}s")
    print(f"⚡ Throughput: {(total_batches * STEPS) / duration:,.0f} pasos/seg")
    
    # Guardar
    out_dir = "outputs_gpu"
    os.makedirs(out_dir, exist_ok=True)
    
    for case_name, (s, e) in case_indices.items():
        sub_res = final_results[:, s:e]
        sub_map = final_entropy[s:e].mean(axis=0)
        
        summary = {
            "case": case_name,
            "grid_size": GRID_SIZE,
            "n_runs": N_RUNS,
            "mean": float(sub_res.mean(axis=1)[-1]),
            "std": float(sub_res.std(axis=1)[-1]),
            "gpu_time": duration,
            "closure_metric_global_entropy": float(sub_map.mean()),
            "closure_metric_max_local_entropy": float(sub_map.max())
        }
        
        np.save(os.path.join(out_dir, f"{case_name}_holography.npy"), sub_map)
        with open(os.path.join(out_dir, f"{case_name}_gpu_summary.json"), "w") as f:
            json.dump(summary, f, indent=2)
    
    print(f"💾 Resultados y Holografías en {out_dir}/")

def run_cpu_mode():
    print("\n🚜 MODO CPU: Ejecución Paralela (Joblib)")
    from joblib import Parallel, delayed
    
    GRID_SIZE = 50
    N_RUNS = 50
    
    validate_scripts = sorted(glob.glob(os.path.join(BASE_PATH, "*_caso_*/src/validate.py")))
    
    def run_single(script_path):
        case_name = script_path.split("/")[-3]
        env = os.environ.copy()
        env["HYPER_GRID_SIZE"] = str(GRID_SIZE)
        env["HYPER_N_RUNS"] = str(N_RUNS)
        env["OMP_NUM_THREADS"] = "1"
        try:
            subprocess.run([sys.executable, script_path], check=True, env=env, capture_output=True)
            return f"✅ {case_name}"
        except:
            return f"❌ {case_name}"

    results = Parallel(n_jobs=-1)(delayed(run_single)(s) for s in validate_scripts)
    for r in results:
        print(r)

def main():
    print(f"🔵 UNIVERSAL RUNNER v3.0 (Chunked) - {datetime.now().isoformat()}")
    mode = check_hardware()
    if mode == "GPU":
        run_gpu_mode()
    else:
        run_cpu_mode()

if __name__ == "__main__":
    main()

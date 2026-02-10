#!/usr/bin/env python3
"""Test: verificar que 2 procesos simultáneos eligen GPUs diferentes via nvidia-smi.

Estrategia: P1 aloca ~8 GB de VRAM en GPU 0 y la MANTIENE viva con sleep.
            P2 arranca después, ve GPU 0 ocupada y elige GPU 1.
"""
import subprocess, time, sys

# P1: fuerza GPU 0, aloca 8 GB y mantiene la referencia viva 30 s
SCRIPT_P1 = r"""
import sys, os, time
os.environ["CUDA_VISIBLE_DEVICES"] = "0"   # forzar GPU 0

sys.path.insert(0, "/workspace/repos/Simulaciones/common")
import cupy as cp

cp.cuda.Device(0).use()
info_name = cp.cuda.runtime.getDeviceProperties(0)["name"]
free_before = cp.cuda.runtime.memGetInfo()[0] / 1e9

# Alocar ~14 GB para que GPU 0 quede con menos libre que GPU 1 (~3 GB)
n_floats = int(14e9 / 4)  # 14 GB de float32
big_array = cp.ones(n_floats, dtype=cp.float32)
cp.cuda.stream.get_current_stream().synchronize()

free_after = cp.cuda.runtime.memGetInfo()[0] / 1e9
print(f"[P1] GPU 0 ({info_name})", flush=True)
print(f"[P1] VRAM: {free_before:.1f} → {free_after:.1f} GB libre (alocó {free_before - free_after:.1f} GB)", flush=True)
print(f"[P1] Manteniendo VRAM ocupada 30 s...", flush=True)

# Mantener vivo — no borrar big_array
time.sleep(30)
print(f"[P1] Liberando y saliendo", flush=True)
del big_array
cp.get_default_memory_pool().free_all_blocks()
"""

# P2: NO fuerza GPU, deja que gpu_backend elija la que tenga más VRAM libre
SCRIPT_P2 = r"""
import sys
sys.path.insert(0, "/workspace/repos/Simulaciones/common")
from gpu_backend import gpu_info, get_all_free_vram, get_free_vram
from abm_core_gpu import simulate_abm_batch

vrams = get_all_free_vram()
info = gpu_info()
print(f"[P2] VRAM al iniciar (nvidia-smi):", flush=True)
for v in vrams:
    marker = " << ELEGIDA" if v["id"] == info["device_id"] else ""
    print(f"  GPU {v['id']}: {v['free_gb']:.1f}/{v['total_gb']:.1f} GB{marker}", flush=True)
print(f"[P2] GPU {info['device_id']} ({info['name']})", flush=True)

# Batch ligero para confirmar que corre en la GPU elegida
params = {"grid_size": 100, "diffusion": 0.2, "noise": 0.02, "forcing_base": 0.5,
          "forcing_scale": 0.01, "macro_coupling": 0.3, "damping": 0.02}
variants = [{"forcing_scale": 0.01 + i*0.001} for i in range(20)]
result = simulate_abm_batch(params, variants, 20)
print(f"[P2] Completado: {result.shape}", flush=True)
"""

print("=== Test multi-GPU: distribución automática ===\n", flush=True)

# Paso 1: P1 ocupa GPU 0 con 8 GB persistentes
print("→ Lanzando P1 (GPU 0, retiene 14 GB por 30 s)...", flush=True)
p1 = subprocess.Popen(
    ["docker", "exec", "tesis-gpu", "python3", "-c", SCRIPT_P1],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)

# Paso 2: Esperar 8 s para que CuPy aloque
print("→ Esperando 8 s para que P1 aloque VRAM...", flush=True)
time.sleep(8)

# Paso 3: Verificar que GPU 0 realmente está ocupada
smi = subprocess.check_output(
    ["nvidia-smi", "--query-gpu=index,name,memory.free,memory.total",
     "--format=csv,noheader"],
    text=True
).strip()
print(f"\nnvidia-smi (P1 corriendo):\n{smi}\n", flush=True)

# Paso 4: P2 arranca — debería ver GPU 0 con poca VRAM y elegir GPU 1
print("→ Lanzando P2 (debería elegir GPU 1)...\n", flush=True)
p2 = subprocess.Popen(
    ["docker", "exec", "tesis-gpu", "python3", "-c", SCRIPT_P2],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)

# Recoger salidas
out2, _ = p2.communicate(timeout=60)
out1, _ = p1.communicate(timeout=60)

print("─── P1 ───")
print(out1)
print("─── P2 ───")
print(out2)

# Evaluar resultado: buscar "GPU 1" en la línea que dice el backend asignó
import re
p2_assigned = re.search(r'PID \d+ → GPU (\d+)', out2)
assigned_gpu = p2_assigned.group(1) if p2_assigned else "?"
print(f"→ P2 fue asignado a GPU {assigned_gpu}")
if assigned_gpu == "1":
    print("✅ P2 eligió GPU 1 — distribución multi-GPU funciona!")
    sys.exit(0)
else:
    print(f"❌ P2 eligió GPU {assigned_gpu} en vez de GPU 1 — revisar")
    sys.exit(1)

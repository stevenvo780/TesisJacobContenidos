"""
gpu_backend.py — Abstracción NumPy/CuPy con asignación multi-GPU por proceso.

Estrategia:
    Cada proceso Python se ANCLA a UNA sola GPU al iniciar, eligiendo la que
    tenga más VRAM libre en ese instante. Cuando corren N procesos en paralelo,
    los primeros saturan GPU 0 (más VRAM) y los siguientes caen en GPU 1.
    Así ambas GPUs trabajan simultáneamente con casos diferentes.

    La detección de VRAM libre usa nvidia-smi (ve la VRAM usada por TODOS
    los procesos, a diferencia de CuPy memGetInfo que solo ve el propio).

    NO se intercala entre GPUs dentro de un mismo proceso — eso mata el
    rendimiento por context-switch de CUDA.

Uso:
    from gpu_backend import xp, to_numpy, using_gpu, gpu_info
    from gpu_backend import get_free_vram, n_gpus

    grid = xp.zeros((500, 500))  # Siempre en la GPU asignada a este proceso
    result = to_numpy(grid)       # Siempre devuelve np.ndarray
"""

import os
import sys
import subprocess
import numpy as np

_GPU_AVAILABLE = False
_GPU_DEVICE = 0
_GPU_NAME = "none"
_GPU_MEM_GB = 0.0
_N_GPUS = 0
_REAL_GPU_ID = 0  # ID real de nvidia-smi (antes de CUDA_VISIBLE_DEVICES)

# Info de TODAS las GPUs: [{id, name, total_gb, free_gb}, ...]
_ALL_GPUS = []

# Desactivar GPU por variable de entorno si se desea
_FORCE_CPU = os.environ.get("HYPER_NO_GPU", "").lower() in ("1", "true", "yes")


def _nvidia_smi_free_vram() -> list[dict]:
    """
    Consulta nvidia-smi para obtener VRAM libre REAL de cada GPU.
    nvidia-smi ve la memoria usada por TODOS los procesos (a diferencia de
    CuPy memGetInfo que solo ve el proceso actual).
    Returns: [{"id": 0, "free_mb": X, "total_mb": Y}, ...]
    """
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=index,memory.free,memory.total",
             "--format=csv,noheader,nounits"],
            timeout=5, stderr=subprocess.DEVNULL
        ).decode().strip()
        result = []
        for line in out.split("\n"):
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 3:
                result.append({
                    "id": int(parts[0]),
                    "free_mb": int(parts[1]),
                    "total_mb": int(parts[2]),
                })
        return result
    except Exception:
        return []


if not _FORCE_CPU:
    try:
        # ══════════════════════════════════════════════════════════════════
        # PASO 1: nvidia-smi ANTES de importar CuPy para elegir GPU
        #         sin crear contextos CUDA en GPUs que no vamos a usar.
        # ══════════════════════════════════════════════════════════════════
        smi_info = _nvidia_smi_free_vram()
        preferred = int(os.environ.get("HYPER_GPU_DEVICE", -1))

        if smi_info:
            _N_GPUS = len(smi_info)
            for s in smi_info:
                _ALL_GPUS.append({
                    "id": s["id"],
                    "name": "gpu",  # se actualiza después con CuPy
                    "total_gb": round(s["total_mb"] / 1024, 2),
                })

            if preferred >= 0 and any(s["id"] == preferred for s in smi_info):
                _GPU_DEVICE = preferred
            elif len(smi_info) > 1:
                best = max(smi_info, key=lambda s: s["free_mb"])
                _GPU_DEVICE = best["id"]
            else:
                _GPU_DEVICE = smi_info[0]["id"]

        # ══════════════════════════════════════════════════════════════════
        # PASO 2: CUDA_VISIBLE_DEVICES ANTES de import cupy
        #         Así CuPy solo crea contexto en 1 GPU — cero VRAM en las demás.
        # ══════════════════════════════════════════════════════════════════
        _REAL_GPU_ID = _GPU_DEVICE  # ID real para nvidia-smi queries
        os.environ["CUDA_VISIBLE_DEVICES"] = str(_GPU_DEVICE)

        import cupy as cp

        # Con CUDA_VISIBLE_DEVICES, CuPy ve solo 1 GPU como device 0
        _cupy_dev_count = cp.cuda.runtime.getDeviceCount()
        if _cupy_dev_count > 0:
            cp.cuda.Device(0).use()  # siempre device 0 (la única visible)
            _test = cp.ones(1000, dtype=cp.float64)
            _result = float(cp.sum(_test))
            assert abs(_result - 1000.0) < 1e-6
            del _test, _result

            props = cp.cuda.runtime.getDeviceProperties(0)
            name = props.get("name", b"unknown")
            if isinstance(name, bytes):
                name = name.decode()
            _, total = cp.cuda.runtime.memGetInfo()

            _GPU_NAME = name
            _GPU_MEM_GB = round(total / (1024**3), 2)
            _GPU_DEVICE = 0  # CuPy ve device 0 (mapeado a _REAL_GPU_ID)
            _GPU_AVAILABLE = True

            # Actualizar nombre real en _ALL_GPUS
            for g in _ALL_GPUS:
                if g["id"] == _REAL_GPU_ID:
                    g["name"] = name

            # Log de asignación
            pid = os.getpid()
            smi_info = _nvidia_smi_free_vram()  # re-query fresh
            smi_map = {s["id"]: s for s in smi_info}
            my_free = smi_map.get(_REAL_GPU_ID, {}).get("free_mb", 0)
            print(f"[gpu_backend] PID {pid} → GPU {_REAL_GPU_ID} "
                  f"({_GPU_NAME}, {my_free}MB libre vía nvidia-smi) "
                  f"[CUDA_VISIBLE_DEVICES={_REAL_GPU_ID}]",
                  file=sys.stderr)
            if len(_ALL_GPUS) > 1:
                for g in _ALL_GPUS:
                    s = smi_map.get(g["id"], {})
                    free_mb = s.get("free_mb", 0)
                    total_mb = s.get("total_mb", 0)
                    marker = " ← ASIGNADA" if g["id"] == _REAL_GPU_ID else " (oculta a CuPy)"
                    print(f"  GPU {g['id']}: {g['name']} — "
                          f"{free_mb}MB/{total_mb}MB libre{marker}",
                          file=sys.stderr)
    except Exception as e:
        _GPU_AVAILABLE = False
        if os.environ.get("HYPER_GPU_DEBUG", ""):
            print(f"[gpu_backend] GPU init failed: {e}", file=sys.stderr)


# ── Número de GPUs disponibles ────────────────────────────────────────────────
n_gpus = _N_GPUS


def using_gpu() -> bool:
    """Retorna True si CuPy+GPU está activo."""
    return _GPU_AVAILABLE


def gpu_info() -> dict:
    """Info de la GPU asignada a este proceso (o CPU fallback)."""
    return {
        "available": _GPU_AVAILABLE,
        "device_id": _GPU_DEVICE,
        "name": _GPU_NAME,
        "vram_gb": round(_GPU_MEM_GB, 1),
        "backend": "cupy" if _GPU_AVAILABLE else "numpy",
        "n_gpus": _N_GPUS,
        "all_gpus": _ALL_GPUS[:],
    }


def get_free_vram(device_id: int | None = None) -> float:
    """
    Retorna VRAM libre ACTUAL (en GB) de la GPU asignada a este proceso.
    Usa nvidia-smi para ver la VRAM real (incluye otros procesos).
    Fallback a CuPy memGetInfo si nvidia-smi no disponible.
    """
    if not _GPU_AVAILABLE:
        return 0.0
    # Usar ID real de nvidia-smi (no el device 0 de CuPy)
    dev = device_id if device_id is not None else _REAL_GPU_ID
    # Preferir nvidia-smi (ve TODOS los procesos)
    smi = _nvidia_smi_free_vram()
    for s in smi:
        if s["id"] == dev:
            return s["free_mb"] / 1024.0
    # Fallback a CuPy (solo ve este proceso)
    import cupy as cp
    free, _ = cp.cuda.runtime.memGetInfo()
    return free / (1024**3)


def get_all_free_vram() -> list[dict]:
    """
    Retorna VRAM libre actual de TODAS las GPUs (vía nvidia-smi).
    """
    if not _GPU_AVAILABLE:
        return []
    smi = _nvidia_smi_free_vram()
    result = []
    for g in _ALL_GPUS:
        s = next((x for x in smi if x["id"] == g["id"]), None)
        if s:
            result.append({
                "id": g["id"],
                "name": g["name"],
                "free_gb": round(s["free_mb"] / 1024.0, 2),
                "total_gb": g["total_gb"],
            })
        else:
            result.append({
                "id": g["id"],
                "name": g["name"],
                "free_gb": 0.0,
                "total_gb": g["total_gb"],
            })
    return result


if _GPU_AVAILABLE:
    import cupy as cp  # noqa: F811 — reimport seguro
    xp = cp
else:
    xp = np


def to_numpy(arr) -> np.ndarray:
    """Convierte CuPy array a NumPy (no-op si ya es NumPy)."""
    if _GPU_AVAILABLE and hasattr(arr, "get"):
        return arr.get()
    return np.asarray(arr)


def to_device(arr):
    """Envía array a la GPU asignada a este proceso (no-op si ya está o no hay GPU)."""
    if _GPU_AVAILABLE:
        if isinstance(arr, np.ndarray):
            return cp.asarray(arr)
        if isinstance(arr, (list, tuple)):
            return cp.asarray(np.array(arr))
    return np.asarray(arr) if not isinstance(arr, np.ndarray) else arr


def get_rng(seed: int):
    """Devuelve un RNG apropiado (CuPy o NumPy) en la GPU asignada."""
    if _GPU_AVAILABLE:
        return cp.random.RandomState(seed)
    return np.random.RandomState(seed)


def sync():
    """Sincroniza la GPU asignada a este proceso (no-op en CPU)."""
    if _GPU_AVAILABLE:
        cp.cuda.Device(_GPU_DEVICE).synchronize()


def batch_corrcoef(X: "ndarray", y: "ndarray") -> "ndarray":
    """
    Correlación batch: cada fila de X contra vector y.
    
    X: (M, T) — M series temporales de largo T
    y: (T,) — una serie de referencia
    Returns: (M,) — correlaciones
    
    Usa GPU si disponible, sino NumPy vectorizado.
    """
    _xp = xp
    X = _xp.asarray(X, dtype=_xp.float64)
    y = _xp.asarray(y, dtype=_xp.float64)
    
    X_m = X - X.mean(axis=1, keepdims=True)
    y_m = y - y.mean()
    
    X_std = X.std(axis=1)
    y_std = float(y.std()) if not _GPU_AVAILABLE else y.std()
    
    num = (X_m * y_m[None, :]).sum(axis=1)
    den = X_std * y_std * X.shape[1]
    
    valid = den > 1e-15
    result = _xp.zeros(X.shape[0], dtype=_xp.float64)
    result[valid] = num[valid] / den[valid]
    
    return result


def batch_rmse(predictions: "ndarray", target: "ndarray") -> "ndarray":
    """
    RMSE batch: cada fila de predictions contra target.
    
    predictions: (M, T)
    target: (T,)
    Returns: (M,)
    """
    _xp = xp
    predictions = _xp.asarray(predictions, dtype=_xp.float64)
    target = _xp.asarray(target, dtype=_xp.float64)
    
    diff = predictions - target[None, :]
    return _xp.sqrt(_xp.mean(diff ** 2, axis=1))

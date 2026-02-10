"""
gpu_backend.py — Abstracción NumPy/CuPy para aceleración GPU transparente.

Uso:
    from gpu_backend import xp, to_numpy, using_gpu, gpu_info

    grid = xp.zeros((500, 500))  # GPU si disponible, CPU si no
    result = to_numpy(grid)       # Siempre devuelve np.ndarray

Funciona en:
  - Docker con CUDA 12.8 (contenedor tesis-gpu) → GPU real
  - Host local sin CuPy → fallback a NumPy puro (CPU)

La RTX 5070 Ti (16GB VRAM, 8960 CUDA cores) acelera ~50-100× operaciones
matriciales vs NumPy single-thread para grids ≥ 200×200.
"""

import os
import sys
import numpy as np

_GPU_AVAILABLE = False
_GPU_DEVICE = 0
_GPU_NAME = "none"
_GPU_MEM_GB = 0.0

# Desactivar GPU por variable de entorno si se desea
_FORCE_CPU = os.environ.get("HYPER_NO_GPU", "").lower() in ("1", "true", "yes")

if not _FORCE_CPU:
    try:
        import cupy as cp
        n_gpus = cp.cuda.runtime.getDeviceCount()
        if n_gpus > 0:
            _GPU_DEVICE = int(os.environ.get("HYPER_GPU_DEVICE", 0))
            cp.cuda.Device(_GPU_DEVICE).use()
            # Test funcional real: alocar + operar + sincronizar
            _test = cp.ones(1000, dtype=cp.float64)
            _result = float(cp.sum(_test))
            assert abs(_result - 1000.0) < 1e-6
            del _test, _result
            # Info de la GPU
            props = cp.cuda.runtime.getDeviceProperties(_GPU_DEVICE)
            _GPU_NAME = props.get("name", b"unknown")
            if isinstance(_GPU_NAME, bytes):
                _GPU_NAME = _GPU_NAME.decode()
            mem_total = cp.cuda.runtime.memGetInfo()[1]
            _GPU_MEM_GB = mem_total / (1024**3)
            _GPU_AVAILABLE = True
    except Exception as e:
        _GPU_AVAILABLE = False
        if os.environ.get("HYPER_GPU_DEBUG", ""):
            print(f"[gpu_backend] GPU init failed: {e}", file=sys.stderr)


def using_gpu() -> bool:
    """Retorna True si CuPy+GPU está activo."""
    return _GPU_AVAILABLE


def gpu_info() -> dict:
    """Info de la GPU activa (o CPU fallback)."""
    return {
        "available": _GPU_AVAILABLE,
        "device_id": _GPU_DEVICE,
        "name": _GPU_NAME,
        "vram_gb": round(_GPU_MEM_GB, 1),
        "backend": "cupy" if _GPU_AVAILABLE else "numpy",
    }


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
    """Envía array a GPU (no-op si ya está o no hay GPU)."""
    if _GPU_AVAILABLE:
        if isinstance(arr, np.ndarray):
            return cp.asarray(arr)
        if isinstance(arr, (list, tuple)):
            return cp.asarray(np.array(arr))
    return np.asarray(arr) if not isinstance(arr, np.ndarray) else arr


def get_rng(seed: int):
    """Devuelve un RNG apropiado (CuPy o NumPy)."""
    if _GPU_AVAILABLE:
        return cp.random.RandomState(seed)
    return np.random.RandomState(seed)


def sync():
    """Sincroniza GPU (no-op en CPU)."""
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

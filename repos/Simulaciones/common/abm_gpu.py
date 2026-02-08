"""
abm_gpu.py — Motor ABM vectorizado masivo con PyTorch (CUDA).
Reemplazo de CuPy por robustez.

Diseñado para batch processing: Ejecuta N simulaciones en paralelo en un solo kernel.
Tensor dimensions: (BATCH_SIZE, GRID_SIZE, GRID_SIZE)

Requisitos:
    - torch (pre-instalado y verificado)
"""

import torch
import numpy as np

# Configurar dispositivo global
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if DEVICE.type == 'cpu':
    print("⚠️ ADVERTENCIA: Ejecutando en CPU (Torch no detectó GPU).")

def _neighbor_mean_torch(grid):
    """
    Calcula el promedio de vecinos 4-conectados en GPU usando Torch.
    grid: (BATCH, N, N)
    """
    # Torch roll es equivalente a cp.roll / np.roll
    # axis 1 = filas, axis 2 = columnas
    
    # Acumuladores
    acc = torch.zeros_like(grid)
    count = torch.full_like(grid, 4.0)
    
    # Desplazamientos
    acc += torch.roll(grid, shifts=1, dims=1)   # Arriba
    acc += torch.roll(grid, shifts=-1, dims=1)  # Abajo
    acc += torch.roll(grid, shifts=1, dims=2)   # Izquierda
    acc += torch.roll(grid, shifts=-1, dims=2)  # Derecha
    
    # Corrección de bordes (No periódicos)
    # Fila 0
    acc[:, 0, :] -= torch.roll(grid, shifts=1, dims=1)[:, 0, :]
    count[:, 0, :] -= 1.0
    
    # Fila N-1
    acc[:, -1, :] -= torch.roll(grid, shifts=-1, dims=1)[:, -1, :]
    count[:, -1, :] -= 1.0
    
    # Col 0
    acc[:, :, 0] -= torch.roll(grid, shifts=1, dims=2)[:, :, 0]
    count[:, :, 0] -= 1.0
    
    # Col N-1
    acc[:, :, -1] -= torch.roll(grid, shifts=-1, dims=2)[:, :, -1]
    count[:, :, -1] -= 1.0
    
    return acc / count

def simulate_batch_gpu(
    n_batches,
    grid_size,
    steps,
    params_list,
    seed=None
):
    """
    Ejecuta simulaciones en Torch.
    """
    if seed is not None:
        torch.manual_seed(seed)
        
    # Helpers para tensores de parámetros (BATCH, 1, 1)
    def get_param_tensor(key, default):
        vals = [p.get(key, default) for p in params_list]
        arr = torch.tensor(vals, dtype=torch.float32, device=DEVICE)
        return arr.reshape(n_batches, 1, 1)

    diff = get_param_tensor("diffusion", 0.2)
    noise_amp = get_param_tensor("noise", 0.02)
    mc = get_param_tensor("macro_coupling", 0.3)
    fs = get_param_tensor("forcing_scale", 0.01)
    dmp = get_param_tensor("damping", 0.02)
    
    # Forcing Series (STEPS, BATCH)
    forcing_matrix = torch.zeros((steps, n_batches), dtype=torch.float32, device=DEVICE)
    
    # Pre-calcular forcing en CPU luego mover a GPU
    forcing_cpu = np.zeros((steps, n_batches), dtype=np.float32)
    for i, p in enumerate(params_list):
        forcing_series = p.get("forcing_series")
        if forcing_series is None:
            base = p.get("forcing_base", 0.0)
            trend = p.get("forcing_trend", 0.0)
            amp = p.get("forcing_seasonal_amp", 0.0)
            period = p.get("forcing_seasonal_period", 12.0)
            t_arr = np.arange(steps)
            series = base + trend * t_arr + amp * np.sin(2 * np.pi * t_arr / period)
            forcing_cpu[:, i] = series
        else:
            slen = len(forcing_series)
            if slen >= steps:
                forcing_cpu[:, i] = forcing_series[:steps]
            else:
                 forcing_cpu[:slen, i] = forcing_series
                 forcing_cpu[slen:, i] = forcing_series[-1]

    forcing_matrix = torch.tensor(forcing_cpu, dtype=torch.float32, device=DEVICE)

    # Init State
    init_centers = [p.get("t0", 0.0) for p in params_list]
    init_centers_gpu = torch.tensor(init_centers, dtype=torch.float32, device=DEVICE).reshape(n_batches, 1, 1)
    
    grid = (torch.rand((n_batches, grid_size, grid_size), device=DEVICE) - 0.5) + init_centers_gpu
    
    # Output
    macro_series = torch.zeros((steps, n_batches), dtype=torch.float32, device=DEVICE)
    
    # Loop
    for t in range(steps):
        f = forcing_matrix[t].reshape(n_batches, 1, 1)
        
        # Macrostate
        macro = grid.mean(dim=(1, 2), keepdim=True)
        macro_series[t] = macro.flatten()
        
        # Physics
        nb_mean = _neighbor_mean_torch(grid)
        noise = (torch.rand_like(grid) * 2.0 - 1.0) * noise_amp
        
        delta = (diff * (nb_mean - grid)) + \
                (fs * f) + \
                (mc * (macro - grid)) - \
                (dmp * grid) + \
                noise
                
        grid += delta
        
        # Soft Clipping (Torch clamp)
        grid = torch.clamp(grid, -1e6, 1e6)
        
    return macro_series.cpu().numpy()

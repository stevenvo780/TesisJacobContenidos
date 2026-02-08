"""
abm_gpu.py — Motor ABM vectorizado masivo con PyTorch (CUDA).
Versión 2.0: Soporte para Topología Dispersa, Reflexividad y Holografía Entrópica.

Características:
    - Batch Processing: (BATCH_SIZE, GRID_SIZE, GRID_SIZE)
    - Sparse Topology: Interacción no local via matrices dispersas.
    - Dynamic Reflexivity: Feedback loop Micro -> Macro -> Parámetros.
    - Entropic Holography: Mapa de varianza local per-pixel.
"""

import torch
import numpy as np

# Configurar dispositivo global
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def _neighbor_mean_torch(grid):
    """Promedio de vecinos 4-conectados (Grilla Regular)."""
    acc = torch.zeros_like(grid)
    count = torch.full_like(grid, 4.0)
    
    acc += torch.roll(grid, shifts=1, dims=1)
    acc += torch.roll(grid, shifts=-1, dims=1)
    acc += torch.roll(grid, shifts=1, dims=2)
    acc += torch.roll(grid, shifts=-1, dims=2)
    
    # Corrección bordes
    acc[:, 0, :] -= torch.roll(grid, shifts=1, dims=1)[:, 0, :]
    count[:, 0, :] -= 1.0
    acc[:, -1, :] -= torch.roll(grid, shifts=-1, dims=1)[:, -1, :]
    count[:, -1, :] -= 1.0
    acc[:, :, 0] -= torch.roll(grid, shifts=1, dims=2)[:, :, 0]
    count[:, :, 0] -= 1.0
    acc[:, :, -1] -= torch.roll(grid, shifts=-1, dims=2)[:, :, -1]
    count[:, :, -1] -= 1.0
    
    return acc / count

def _neighbor_mean_sparse(grid, adj_matrix):
    """
    Difusión Dispersa (Red Compleja).
    grid: (BATCH, N, N)
    adj_matrix: (N*N, N*N) Sparse Tensor (Row-Normalized preferred)
    """
    B, N, _ = grid.shape
    # Flatten state: (BATCH, N*N) -> Transpose to (N*N, BATCH)
    flat_state = grid.reshape(B, -1).t()
    
    # Matrix Mult: (N*N, N*N) @ (N*N, BATCH) -> (N*N, BATCH)
    # Result represents sum/mean of neighbors for each agent in each batch
    res_flat = torch.sparse.mm(adj_matrix, flat_state)
    
    # Transpose back and reshape: (BATCH, N*N) -> (BATCH, N, N)
    return res_flat.t().reshape(B, N, N)

def simulate_batch_gpu(
    n_batches,
    grid_size,
    steps,
    params_list,
    seed=None,
    adjacency_matrix=None # Optional: torch.sparse_coo_tensor
):
    if seed is not None:
        torch.manual_seed(seed)
        
    # --- Tensores de Parámetros ---
    def get_param_tensor(key, default):
        vals = [p.get(key, default) for p in params_list]
        return torch.tensor(vals, dtype=torch.float32, device=DEVICE).reshape(n_batches, 1, 1)

    diff = get_param_tensor("diffusion", 0.2)
    noise_amp = get_param_tensor("noise", 0.02)
    mc = get_param_tensor("macro_coupling", 0.3)
    fs = get_param_tensor("forcing_scale", 0.01) # Será dinámico si hay reflexividad
    dmp = get_param_tensor("damping", 0.02)
    
    # Reflexividad
    gamma = get_param_tensor("reflexivity_gamma", 0.0)
    target = get_param_tensor("reflexivity_target", 0.0) # 0.0 = equilibrio neutral
    
    # Forcing Series setup (Pre-calc CPU -> GPU)
    forcing_matrix = torch.zeros((steps, n_batches), dtype=torch.float32, device=DEVICE)
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
    center_tensor = torch.tensor(init_centers, dtype=torch.float32, device=DEVICE).reshape(n_batches, 1, 1)
    grid = (torch.rand((n_batches, grid_size, grid_size), device=DEVICE) - 0.5) + center_tensor
    
    # Output Containers
    macro_series = torch.zeros((steps, n_batches), dtype=torch.float32, device=DEVICE)
    
    # Entropic Holography Accumulators
    # Var(X) = E[X^2] - (E[X])^2
    sum_x = torch.zeros_like(grid)
    sum_sq_x = torch.zeros_like(grid)
    
    # --- Simulation Loop ---
    for t in range(steps):
        # 0. Holography Accumulation
        sum_x += grid
        sum_sq_x += grid ** 2
        
        # 1. Macrostate
        macro = grid.mean(dim=(1, 2), keepdim=True) # (B, 1, 1)
        macro_series[t] = macro.flatten()
        
        # 2. Dynamic Reflexivity (Feedback Loop)
        # fs(t) se actualiza basado en error macro actual
        # Si gamma > 0, el sistema modula su acoplamiento externo
        if torch.any(gamma > 0):
            # Error = Macro - Target
            err = macro - target
            # Regla: Si error pos, aumenta forcing (por ejemplo). O user defined.
            # Implementamos: FS_new = FS_base * (1 + gamma * err)
            # Clip para estabilidad (0.2x a 5.0x)
            modulator = torch.clamp(1.0 + gamma * err, 0.2, 5.0)
            fs_eff = fs * modulator
        else:
            fs_eff = fs

        f_val = forcing_matrix[t].reshape(n_batches, 1, 1)
        
        # 3. Diffusion (Topology switch)
        if adjacency_matrix is not None:
            nb_mean = _neighbor_mean_sparse(grid, adjacency_matrix)
        else:
            nb_mean = _neighbor_mean_torch(grid)
            
        noise = (torch.rand_like(grid) * 2.0 - 1.0) * noise_amp
        
        # 4. Update Rule
        delta = (diff * (nb_mean - grid)) + \
                (fs_eff * f_val) + \
                (mc * (macro - grid)) - \
                (dmp * grid) + \
                noise
                
        grid += delta
        grid = torch.clamp(grid, -1e6, 1e6) # Soft Clipping

    # --- Compute Entropy Map (Variance per pixel) ---
    # Var = Mean(Sq) - Mean(X)^2
    mean_x = sum_x / steps
    mean_sq_x = sum_sq_x / steps
    variance_map = mean_sq_x - (mean_x ** 2)
    # Ensure non-negative (numerical noise)
    variance_map = torch.clamp(variance_map, min=0.0)
        
    return macro_series.cpu().numpy(), variance_map.cpu().numpy()

"""
abm_gpu_v3.py — Motor ABM con Forzamiento NO Uniforme (Gradientes Espaciales)
Versión 3.0: Añade forcing_gradient para generar dom_share heterogéneo

Responde a crítica: "dom_share = 1/N² significa agentes idénticos"
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
    """Difusión Dispersa (Red Compleja)."""
    B, N, _ = grid.shape
    flat_state = grid.reshape(B, -1).t()
    res_flat = torch.sparse.mm(adj_matrix, flat_state)
    return res_flat.t().reshape(B, N, N)


def create_forcing_gradient(grid_size, gradient_type="radial", strength=1.0):
    """
    Crea un mapa de forzamiento espacialmente heterogéneo.
    
    Args:
        grid_size: Tamaño de la grilla (N x N)
        gradient_type: "radial", "linear", "random_hubs"
        strength: Amplitud del gradiente
    
    Returns:
        torch.Tensor (grid_size, grid_size) con multiplicadores de forcing
    """
    if gradient_type == "radial":
        # Mayor forcing en el centro, menor en bordes
        center = grid_size / 2
        y, x = torch.meshgrid(torch.arange(grid_size), torch.arange(grid_size), indexing='ij')
        dist = torch.sqrt((x - center)**2 + (y - center)**2)
        max_dist = center * np.sqrt(2)
        gradient = 1.0 - (dist / max_dist) * strength
        gradient = torch.clamp(gradient, 0.2, 1.0)
    
    elif gradient_type == "linear":
        # Gradiente de izquierda a derecha
        gradient = torch.linspace(1.0 - strength, 1.0, grid_size).unsqueeze(0).repeat(grid_size, 1)
    
    elif gradient_type == "random_hubs":
        # Crear 3-5 "hubs" aleatorios con alto forcing
        n_hubs = 4
        gradient = torch.ones(grid_size, grid_size) * 0.3
        torch.manual_seed(42)
        for _ in range(n_hubs):
            cx, cy = torch.randint(0, grid_size, (2,))
            # Radio de influencia
            y, x = torch.meshgrid(torch.arange(grid_size), torch.arange(grid_size), indexing='ij')
            dist = torch.sqrt((x - cx.float())**2 + (y - cy.float())**2)
            hub_influence = torch.exp(-dist / (grid_size * 0.15)) * strength
            gradient = torch.max(gradient, hub_influence)
        gradient = torch.clamp(gradient, 0.2, 1.0)
    
    else:
        gradient = torch.ones(grid_size, grid_size)
    
    return gradient.to(DEVICE)


def simulate_batch_gpu_v3(
    n_batches,
    grid_size,
    steps,
    params_list,
    seed=None,
    adjacency_matrix=None,
    forcing_gradient=None  # NUEVO: Mapa de forcing heterogéneo
):
    """
    Simulación ABM con forzamiento espacialmente heterogéneo.
    """
    if seed is not None:
        torch.manual_seed(seed)
        
    # --- Tensores de Parámetros ---
    def get_param_tensor(key, default):
        vals = [p.get(key, default) for p in params_list]
        return torch.tensor(vals, dtype=torch.float32, device=DEVICE).reshape(n_batches, 1, 1)

    diff = get_param_tensor("diffusion", 0.2)
    noise_amp = get_param_tensor("noise", 0.02)
    mc = get_param_tensor("macro_coupling", 0.3)
    fs = get_param_tensor("forcing_scale", 0.01)
    dmp = get_param_tensor("damping", 0.02)
    
    gamma = get_param_tensor("reflexivity_gamma", 0.0)
    target = get_param_tensor("reflexivity_target", 0.0)
    
    # Forcing Series setup
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

    # Gradient de forcing (heterogeneidad espacial)
    if forcing_gradient is None:
        forcing_gradient = torch.ones(grid_size, grid_size, device=DEVICE)
    else:
        forcing_gradient = forcing_gradient.to(DEVICE)

    # Init State
    init_centers = [p.get("t0", 0.0) for p in params_list]
    center_tensor = torch.tensor(init_centers, dtype=torch.float32, device=DEVICE).reshape(n_batches, 1, 1)
    grid = (torch.rand((n_batches, grid_size, grid_size), device=DEVICE) - 0.5) + center_tensor
    
    # Output Containers
    macro_series = torch.zeros((steps, n_batches), dtype=torch.float32, device=DEVICE)
    contribution_accumulator = torch.zeros((n_batches, grid_size, grid_size), device=DEVICE)
    
    # Entropic Holography
    sum_x = torch.zeros_like(grid)
    sum_sq_x = torch.zeros_like(grid)
    
    # --- Simulation Loop ---
    for t in range(steps):
        sum_x += grid
        sum_sq_x += grid ** 2
        
        # Macrostate
        macro = grid.mean(dim=(1, 2), keepdim=True)
        macro_series[t] = macro.flatten()
        
        # Contribution tracking (para dom_share)
        # Cada celda contribuye proporcionalmente a |grid - macro|
        contribution = torch.abs(grid - macro)
        contribution_accumulator += contribution
        
        # Dynamic Reflexivity
        if torch.any(gamma > 0):
            err = macro - target
            modulator = torch.clamp(1.0 + gamma * err, 0.2, 5.0)
            fs_eff = fs * modulator
        else:
            fs_eff = fs

        f_val = forcing_matrix[t].reshape(n_batches, 1, 1)
        
        # NUEVO: Aplicar gradiente espacial al forcing
        f_spatial = f_val * forcing_gradient.unsqueeze(0)
        
        # Diffusion
        if adjacency_matrix is not None:
            nb_mean = _neighbor_mean_sparse(grid, adjacency_matrix)
        else:
            nb_mean = _neighbor_mean_torch(grid)
            
        noise = (torch.rand_like(grid) * 2.0 - 1.0) * noise_amp
        
        # Update Rule con forcing espacial
        delta = (diff * (nb_mean - grid)) + \
                (fs_eff * f_spatial) + \
                (mc * (macro - grid)) - \
                (dmp * grid) + \
                noise
                
        grid += delta
        grid = torch.clamp(grid, -1e6, 1e6)

    # --- Compute Entropy Map ---
    mean_x = sum_x / steps
    mean_sq_x = sum_sq_x / steps
    variance_map = mean_sq_x - (mean_x ** 2)
    variance_map = torch.clamp(variance_map, min=0.0)
    
    # --- Compute Dominance Share ---
    # Normalizar contribuciones acumuladas
    total_contribution = contribution_accumulator.sum(dim=(1, 2), keepdim=True)
    dominance_map = contribution_accumulator / (total_contribution + 1e-8)
    dom_share_max = dominance_map.max(dim=2)[0].max(dim=1)[0]  # Max share per batch
        
    return {
        "macro_series": macro_series.cpu().numpy(),
        "variance_map": variance_map.cpu().numpy(),
        "dominance_map": dominance_map.cpu().numpy(),
        "dom_share_max": dom_share_max.cpu().numpy(),
        "agent_std": grid.std(dim=(1, 2)).cpu().numpy()  # Heterogeneidad final
    }


if __name__ == "__main__":
    print("🔬 Testing ABM GPU v3 (Non-Uniform Forcing)")
    print(f"Device: {DEVICE}")
    
    # Test con gradiente radial
    grid_size = 80
    gradient = create_forcing_gradient(grid_size, "random_hubs", strength=0.8)
    
    params = [{
        "diffusion": 0.1, "noise": 0.02, "macro_coupling": 0.3,
        "forcing_scale": 0.5, "damping": 0.02, "t0": 15.0,
        "forcing_base": 15.0, "forcing_trend": 0.01
    }]
    
    print("\n📊 Test 1: Uniform forcing (baseline)")
    res_uniform = simulate_batch_gpu_v3(1, grid_size, 200, params, seed=42)
    print(f"   dom_share_max: {res_uniform['dom_share_max'][0]:.6f}")
    print(f"   agent_std: {res_uniform['agent_std'][0]:.4f}")
    
    print("\n📊 Test 2: Random hubs forcing (heterogeneous)")
    res_hubs = simulate_batch_gpu_v3(1, grid_size, 200, params, seed=42, forcing_gradient=gradient)
    print(f"   dom_share_max: {res_hubs['dom_share_max'][0]:.6f}")
    print(f"   agent_std: {res_hubs['agent_std'][0]:.4f}")
    
    improvement = (res_hubs['dom_share_max'][0] / res_uniform['dom_share_max'][0] - 1) * 100
    print(f"\n✅ dom_share improvement: {improvement:+.1f}%")

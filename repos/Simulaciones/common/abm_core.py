"""
abm_core.py — Motor ABM unificado (CPU, NumPy) con heterogeneidad y acoplamiento macro.

Objetivos:
- Soportar forcing_gradient (heterogeneidad espacial)
- Soportar macro_target_series (acoplamiento ODE→ABM)
- Mantener interfaz compatible: simulate_abm(params, steps, seed) → dict
"""

from __future__ import annotations

import numpy as np


def _neighbor_mean(grid: np.ndarray) -> np.ndarray:
    """Promedio de vecinos 4-conectados con corrección de bordes."""
    acc = np.zeros_like(grid)
    count = np.full_like(grid, 4.0)

    acc += np.roll(grid, 1, axis=0)
    acc += np.roll(grid, -1, axis=0)
    acc += np.roll(grid, 1, axis=1)
    acc += np.roll(grid, -1, axis=1)

    # Corrección bordes
    acc[0, :] -= np.roll(grid, 1, axis=0)[0, :]
    count[0, :] -= 1
    acc[-1, :] -= np.roll(grid, -1, axis=0)[-1, :]
    count[-1, :] -= 1
    acc[:, 0] -= np.roll(grid, 1, axis=1)[:, 0]
    count[:, 0] -= 1
    acc[:, -1] -= np.roll(grid, -1, axis=1)[:, -1]
    count[:, -1] -= 1

    return acc / count


def _neighbor_mean_topology(grid: np.ndarray, adj_matrix) -> np.ndarray:
    """Promedio de vecinos usando matriz de adyacencia (row-normalized)."""
    flat = grid.reshape(-1)
    # Soportar sparse matrix con @ sobre np.ndarray
    nb = adj_matrix @ flat
    return np.asarray(nb).reshape(grid.shape)

def _create_forcing_gradient(n: int, gradient_type: str, strength: float) -> np.ndarray:
    if gradient_type == "radial":
        center = (n - 1) / 2.0
        y, x = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
        dist = np.sqrt((x - center) ** 2 + (y - center) ** 2)
        max_dist = center * np.sqrt(2)
        grad = 1.0 - (dist / max_dist) * strength
        return np.clip(grad, 0.2, 1.0)
    if gradient_type == "linear":
        grad = np.linspace(1.0 - strength, 1.0, n)
        return np.tile(grad, (n, 1))
    if gradient_type == "random_hubs":
        rng = np.random.RandomState(42)
        grad = np.ones((n, n)) * 0.3
        hubs = 4
        for _ in range(hubs):
            cx, cy = rng.randint(0, n, size=2)
            y, x = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
            dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            hub = np.exp(-dist / (n * 0.15)) * strength
            grad = np.maximum(grad, hub)
        return np.clip(grad, 0.2, 1.0)
    return np.ones((n, n))


def _infer_macro_init(params: dict, series_key: str) -> float:
    # Intentos directos
    direct = series_key + "0"
    if direct in params:
        return float(params[direct])

    # Mapeo común
    mapping = {
        "tbar": "t0",
        "incidence": "i0",
        "p": "p0",
        "e": "e0",
        "x": "x0",
        "d": "d0",
        "w": "w0",
        "m": "m0",
        "c": "c0",
        "s": "s0",
        "r": "r0",
        "h": "h0",
        "a": "a0",
        "f": "f0",
    }
    key = mapping.get(series_key)
    if key and key in params:
        return float(params[key])

    # Fallbacks
    for k in ("t0", "x0", "e0", "p0"):
        if k in params:
            return float(params[k])
    return 0.0


def _infer_macro_gain(params: dict) -> float:
    for k in ("macro_gain", "demand_scale", "price_scale", "sentiment_scale",
              "pollution_scale", "attention_scale"):
        if k in params:
            try:
                return float(params[k])
            except Exception:
                continue
    return 0.0


def simulate_abm_core(
    params: dict,
    steps: int,
    seed: int = 2,
    series_key: str = "tbar",
    init_range: float = 0.5,
):
    """
    ABM genérico con heterogeneidad espacial y acoplamiento macro.

    Params relevantes:
    - grid_size, diffusion, noise, macro_coupling, forcing_scale, damping
    - forcing_series (list)
    - forcing_gradient (np.ndarray/list 2D)
    - macro_target_series (list)
    - macro_mode: "mean" | "dynamic"
    - macro_gain (o demand_scale/price_scale/etc)
    - macro_forcing_gain, macro_damping, macro_noise
    - assimilation_series, assimilation_strength
    - perturbation_event {step, magnitude}
    """

    rng = np.random.RandomState(seed)
    n = int(params.get("grid_size", 20))
    diff = float(params.get("diffusion", 0.2))
    noise_amp = float(params.get("noise", 0.02))
    mc = float(params.get("macro_coupling", 0.3))
    fs = float(params.get("forcing_scale", 0.01))
    dmp = float(params.get("damping", 0.02))
    hetero = float(params.get("heterogeneity_strength", 0.0))
    hetero_seed = int(params.get("heterogeneity_seed", seed))

    forcing = params.get("forcing_series")
    if forcing is None:
        base = float(params.get("forcing_base", 0.0))
        trend = float(params.get("forcing_trend", 0.0))
        amp = float(params.get("forcing_seasonal_amp", 0.0))
        period = float(params.get("forcing_seasonal_period", 12.0))
        t_arr = np.arange(steps)
        forcing = base + trend * t_arr + amp * np.sin(2 * np.pi * t_arr / period)
        forcing = forcing.tolist()

    forcing_gradient = params.get("forcing_gradient")
    if forcing_gradient is not None:
        fg = np.asarray(forcing_gradient, dtype=np.float64)
        if fg.shape != (n, n):
            fg = None
    else:
        gtype = params.get("forcing_gradient_type")
        if gtype:
            strength = float(params.get("forcing_gradient_strength", 0.6))
            fg = _create_forcing_gradient(n, gtype, strength)
        else:
            fg = None

    adjacency_matrix = params.get("adjacency_matrix")

    macro_target_series = params.get("macro_target_series")
    macro_mode = params.get("macro_mode")
    macro_gain = _infer_macro_gain(params)
    macro_forcing_gain = float(params.get("macro_forcing_gain", fs))
    macro_damping = float(params.get("macro_damping", dmp))
    macro_noise = float(params.get("macro_noise", noise_amp))

    if macro_mode is None:
        macro_mode = "dynamic" if abs(macro_gain) > 1e-12 else "mean"

    macro_state = _infer_macro_init(params, series_key)
    init_range = float(params.get("init_range", init_range))
    grid_center = float(params.get("grid_center", macro_state))
    grid = grid_center + rng.uniform(-init_range, init_range, (n, n))

    # Heterogeneidad paramétrica por celda
    if hetero > 1e-8:
        rng_h = np.random.RandomState(hetero_seed)
        diff_map = diff * (1.0 + hetero * rng_h.normal(0.0, 1.0, (n, n)))
        dmp_map = dmp * (1.0 + hetero * rng_h.normal(0.0, 1.0, (n, n)))
        noise_map = noise_amp * (1.0 + hetero * rng_h.normal(0.0, 1.0, (n, n)))
        diff_map = np.clip(diff_map, 0.0, 1.0)
        dmp_map = np.clip(dmp_map, 0.0, 1.0)
        noise_map = np.clip(noise_map, 0.0, None)
    else:
        diff_map = diff
        dmp_map = dmp
        noise_map = noise_amp

    assim_series = params.get("assimilation_series")
    assim_strength = float(params.get("assimilation_strength", 0.0))
    perturbation_event = params.get("perturbation_event")

    store_grid = params.get("_store_grid", True)
    grid_series = [] if store_grid else None
    main_series = []

    for t in range(steps):
        f = forcing[t]
        f_spatial = f if fg is None else f * fg

        # Vecinos
        if adjacency_matrix is not None:
            nb_mean = _neighbor_mean_topology(grid, adjacency_matrix)
        else:
            nb_mean = _neighbor_mean(grid)

        macro_mean = float(grid.mean())
        if macro_target_series is not None and t < len(macro_target_series):
            macro_target = float(macro_target_series[t])
        else:
            macro_target = float(macro_state if macro_mode == "dynamic" else macro_mean)

        if isinstance(noise_map, np.ndarray):
            noise = rng.uniform(-1.0, 1.0, (n, n)) * noise_map
        else:
            noise = rng.uniform(-noise_amp, noise_amp, (n, n))
        grid = (
            grid
            + diff_map * (nb_mean - grid)
            + fs * f_spatial
            + mc * (macro_target - grid)
            - dmp_map * grid
            + noise
        )
        if not np.isfinite(grid).all():
            grid = np.nan_to_num(grid, nan=0.0, posinf=1e6, neginf=-1e6)
        grid = np.clip(grid, -1e6, 1e6)

        # Perturbación (viscosidad)
        if perturbation_event and t == perturbation_event.get("step"):
            grid += float(perturbation_event.get("magnitude", 0.0))

        # Assimilation (nudging)
        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                delta = assim_strength * (float(target) - float(grid.mean()))
                grid += delta

        # Update macro_state (si aplica)
        if macro_mode == "dynamic":
            macro_state = (
                macro_state
                + macro_gain * macro_mean
                + macro_forcing_gain * f
                - macro_damping * macro_state
                + rng.uniform(-macro_noise, macro_noise)
            )
            if not np.isfinite(macro_state):
                macro_state = 0.0
            main_series.append(float(macro_state))
        else:
            main_series.append(float(grid.mean()))

        if store_grid:
            grid_series.append(grid.tolist())

    result = {series_key: main_series, "forcing": forcing}
    if store_grid:
        result["grid"] = grid_series
    return result


# ─── Auto-dispatch GPU ────────────────────────────────────────────────────────
# Si CuPy+GPU está disponible, reemplaza simulate_abm_core con la versión GPU
# y expone simulate_abm_batch para calibración masiva.
# Transparente para todos los abm.py que hacen:
#   from abm_core import simulate_abm_core

_cpu_simulate_abm_core = simulate_abm_core  # Guardar referencia CPU
simulate_abm_batch = None  # Disponible solo con GPU

try:
    from gpu_backend import using_gpu
    if using_gpu():
        from abm_core_gpu import simulate_abm_core as _gpu_simulate_abm_core
        from abm_core_gpu import simulate_abm_batch as _gpu_simulate_abm_batch
        simulate_abm_core = _gpu_simulate_abm_core
        simulate_abm_batch = _gpu_simulate_abm_batch
        import sys
        print("[abm_core] GPU detected — using abm_core_gpu backend (batch enabled)", file=sys.stderr)
except ImportError:
    pass  # Sin GPU, se queda con CPU


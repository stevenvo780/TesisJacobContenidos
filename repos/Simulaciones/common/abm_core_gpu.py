"""
abm_core_gpu.py — Motor ABM con aceleración GPU vía CuPy.

Drop-in replacement para abm_core.py cuando hay GPU disponible.
Toda la aritmética del grid se ejecuta en VRAM — solo se copia a
CPU al final para extraer las series. Para grid_size=500 esto es
~100× más rápido que NumPy.

Incluye:
  - simulate_abm_core():  1 simulación en GPU (API idéntico a CPU)
  - simulate_abm_batch(): B simulaciones simultáneas como tensor 3D
                           (B, n, n) en VRAM — satura la GPU.

Uso:
    from abm_core_gpu import simulate_abm_core   # 1 sim
    from abm_core_gpu import simulate_abm_batch  # B sims en paralelo
"""

from __future__ import annotations
import numpy as np

try:
    from gpu_backend import xp, to_numpy, to_device, using_gpu, get_rng, sync
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "common"))
    from gpu_backend import xp, to_numpy, to_device, using_gpu, get_rng, sync


def _neighbor_mean_gpu(grid):
    """Promedio de vecinos 4-conectados — versión GPU."""
    _xp = xp
    n = grid.shape[0]
    acc = _xp.zeros_like(grid)
    count = _xp.full_like(grid, 4.0)

    acc += _xp.roll(grid, 1, axis=0)
    acc += _xp.roll(grid, -1, axis=0)
    acc += _xp.roll(grid, 1, axis=1)
    acc += _xp.roll(grid, -1, axis=1)

    # Corrección bordes (evitar wrap-around)
    acc[0, :] -= _xp.roll(grid, 1, axis=0)[0, :]
    count[0, :] -= 1
    acc[-1, :] -= _xp.roll(grid, -1, axis=0)[-1, :]
    count[-1, :] -= 1
    acc[:, 0] -= _xp.roll(grid, 1, axis=1)[:, 0]
    count[:, 0] -= 1
    acc[:, -1] -= _xp.roll(grid, -1, axis=1)[:, -1]
    count[:, -1] -= 1

    return acc / count


def _create_forcing_gradient_gpu(n: int, gradient_type: str, strength: float):
    """Gradiente de forcing en GPU."""
    _xp = xp
    if gradient_type == "radial":
        center = (n - 1) / 2.0
        y, x = _xp.meshgrid(_xp.arange(n), _xp.arange(n), indexing="ij")
        dist = _xp.sqrt((x - center) ** 2 + (y - center) ** 2)
        max_dist = center * _xp.sqrt(_xp.float64(2))
        grad = 1.0 - (dist / max_dist) * strength
        return _xp.clip(grad, 0.2, 1.0)
    if gradient_type == "linear":
        grad = _xp.linspace(1.0 - strength, 1.0, n)
        return _xp.tile(grad, (n, 1))
    if gradient_type == "random_hubs":
        # Hubs generados en CPU por reproducibilidad, luego a GPU
        rng = np.random.RandomState(42)
        grad_np = np.ones((n, n)) * 0.3
        hubs = 4
        for _ in range(hubs):
            cx, cy = rng.randint(0, n, size=2)
            y, x = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
            dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            hub = np.exp(-dist / (n * 0.15)) * strength
            grad_np = np.maximum(grad_np, hub)
        return to_device(np.clip(grad_np, 0.2, 1.0))
    return _xp.ones((n, n))


def _infer_macro_init(params: dict, series_key: str) -> float:
    """Mismo que abm_core — se ejecuta en CPU (es solo un lookup)."""
    direct = series_key + "0"
    if direct in params:
        return float(params[direct])
    mapping = {
        "tbar": "t0", "incidence": "i0", "p": "p0", "e": "e0",
        "x": "x0", "d": "d0", "w": "w0", "m": "m0",
        "c": "c0", "s": "s0", "r": "r0", "h": "h0", "a": "a0", "f": "f0",
    }
    key = mapping.get(series_key)
    if key and key in params:
        return float(params[key])
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
    ABM genérico con GPU — API idéntico a abm_core.simulate_abm_core.
    
    Si GPU no está disponible, delega al abm_core CPU original.
    Las operaciones de grid (diffusion, forcing, coupling, noise) se
    ejecutan enteramente en VRAM. Solo grid.mean() se transfiere a CPU
    por step para construir main_series.
    """
    if not using_gpu():
        # Fallback transparente a CPU
        from abm_core import simulate_abm_core as _cpu_version
        return _cpu_version(params, steps, seed, series_key, init_range)
    
    _xp = xp
    rng = get_rng(seed)
    n = int(params.get("grid_size", 20))
    diff = float(params.get("diffusion", 0.2))
    noise_amp = float(params.get("noise", 0.02))
    mc = float(params.get("macro_coupling", 0.3))
    fs = float(params.get("forcing_scale", 0.01))
    dmp = float(params.get("damping", 0.02))
    hetero = float(params.get("heterogeneity_strength", 0.0))
    hetero_seed = int(params.get("heterogeneity_seed", seed))

    # Forcing — construir en CPU, enviar a GPU como vector
    forcing = params.get("forcing_series")
    if forcing is None:
        base = float(params.get("forcing_base", 0.0))
        trend = float(params.get("forcing_trend", 0.0))
        amp = float(params.get("forcing_seasonal_amp", 0.0))
        period = float(params.get("forcing_seasonal_period", 12.0))
        t_arr = np.arange(steps)
        forcing = (base + trend * t_arr + amp * np.sin(2 * np.pi * t_arr / period)).tolist()
    forcing_gpu = to_device(np.array(forcing, dtype=np.float64))

    # Forcing gradient
    fg = None
    forcing_gradient = params.get("forcing_gradient")
    if forcing_gradient is not None:
        fg_np = np.asarray(forcing_gradient, dtype=np.float64)
        if fg_np.shape == (n, n):
            fg = to_device(fg_np)
    else:
        gtype = params.get("forcing_gradient_type")
        if gtype:
            strength = float(params.get("forcing_gradient_strength", 0.6))
            fg = _create_forcing_gradient_gpu(n, gtype, strength)

    # Modo macro
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
    
    # Grid inicial en GPU
    grid = to_device(np.full((n, n), grid_center, dtype=np.float64))
    grid += rng.uniform(-init_range, init_range, (n, n))

    # Heterogeneidad paramétrica
    if hetero > 1e-8:
        rng_h = np.random.RandomState(hetero_seed)
        diff_map = to_device(np.clip(diff * (1.0 + hetero * rng_h.normal(0, 1, (n, n))), 0, 1).astype(np.float64))
        dmp_map = to_device(np.clip(dmp * (1.0 + hetero * rng_h.normal(0, 1, (n, n))), 0, 1).astype(np.float64))
        noise_map = to_device(np.clip(noise_amp * (1.0 + hetero * rng_h.normal(0, 1, (n, n))), 0, None).astype(np.float64))
    else:
        diff_map = diff
        dmp_map = dmp
        noise_map = None  # Señal de usar noise_amp escalar

    # Assimilation
    assim_series = params.get("assimilation_series")
    assim_strength = float(params.get("assimilation_strength", 0.0))
    perturbation_event = params.get("perturbation_event")

    store_grid = params.get("_store_grid", True)
    grid_series = [] if store_grid else None
    main_series = []

    # ─── Loop principal: todo en GPU ─────────────────────────────────
    for t in range(steps):
        f = forcing_gpu[t]
        f_spatial = f if fg is None else f * fg

        nb_mean = _neighbor_mean_gpu(grid)
        
        # macro_mean: transferencia GPU→CPU mínima (1 escalar)
        macro_mean = float(grid.mean())
        
        if macro_target_series is not None and t < len(macro_target_series):
            macro_target = float(macro_target_series[t])
        else:
            macro_target = float(macro_state if macro_mode == "dynamic" else macro_mean)

        # Noise en GPU
        if noise_map is not None:
            noise = rng.uniform(-1.0, 1.0, (n, n)) * noise_map
        else:
            noise = rng.uniform(-noise_amp, noise_amp, (n, n))

        # Update — toda la aritmética en VRAM
        grid = (
            grid
            + diff_map * (nb_mean - grid)
            + fs * f_spatial
            + mc * (macro_target - grid)
            - dmp_map * grid
            + noise
        )
        
        # Sanitize
        grid = _xp.clip(_xp.nan_to_num(grid, nan=0.0, posinf=1e6, neginf=-1e6), -1e6, 1e6)

        # Perturbación
        if perturbation_event and t == perturbation_event.get("step"):
            grid += float(perturbation_event.get("magnitude", 0.0))

        # Assimilation (nudging)
        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                delta = assim_strength * (float(target) - macro_mean)
                grid += delta

        # Macro update
        if macro_mode == "dynamic":
            macro_state = (
                macro_state
                + macro_gain * macro_mean
                + macro_forcing_gain * float(f)
                - macro_damping * macro_state
                + float(rng.uniform(-macro_noise, macro_noise))
            )
            if not np.isfinite(macro_state):
                macro_state = 0.0
            main_series.append(float(macro_state))
        else:
            main_series.append(macro_mean)

        if store_grid:
            # Transfer grid GPU→CPU una vez por step
            grid_series.append(to_numpy(grid).tolist())

    sync()
    
    result = {series_key: main_series, "forcing": forcing}
    if store_grid:
        result["grid"] = grid_series
    return result


# ══════════════════════════════════════════════════════════════════════════════
#  BATCH ABM — B simulaciones simultáneas como tensor 3D (B, n, n) en VRAM
# ══════════════════════════════════════════════════════════════════════════════

def _neighbor_mean_batch(grids):
    """
    Promedio de vecinos 4-conectados — versión batch GPU.
    
    grids: (B, n, n) — B grids simultáneos.
    Retorna: (B, n, n) — promedio vecinal para cada grid.
    
    Usa wrap-around (roll) y luego corrige bordes.
    Para B=200, n=500: la GPU opera sobre 50M floats por roll → saturación.
    """
    _xp = xp
    B, n, _ = grids.shape
    acc = _xp.zeros_like(grids)
    count = _xp.full_like(grids, 4.0)
    
    # Rolls sobre axes espaciales (1, 2), axis 0 es el batch
    acc += _xp.roll(grids, 1, axis=1)
    acc += _xp.roll(grids, -1, axis=1)
    acc += _xp.roll(grids, 1, axis=2)
    acc += _xp.roll(grids, -1, axis=2)
    
    # Corrección bordes — evitar wrap-around
    acc[:, 0, :]  -= _xp.roll(grids, 1, axis=1)[:, 0, :]
    count[:, 0, :] -= 1
    acc[:, -1, :] -= _xp.roll(grids, -1, axis=1)[:, -1, :]
    count[:, -1, :] -= 1
    acc[:, :, 0]  -= _xp.roll(grids, 1, axis=2)[:, :, 0]
    count[:, :, 0] -= 1
    acc[:, :, -1] -= _xp.roll(grids, -1, axis=2)[:, :, -1]
    count[:, :, -1] -= 1
    
    return acc / count


def simulate_abm_batch(
    base_params: dict,
    param_variants: list[dict],
    steps: int,
    seed: int = 2,
    series_key: str = "tbar",
    init_range: float = 0.5,
    max_batch: int = 0,
) -> np.ndarray:
    """
    Ejecuta B simulaciones ABM simultáneas en VRAM.
    
    Todas las simulaciones comparten el mismo base_params (grid_size, diffusion,
    noise, forcing, etc.). Solo difieren en los parámetros listados en
    param_variants (típicamente: forcing_scale, macro_coupling, damping).
    
    Parameters
    ----------
    base_params : dict
        Parámetros base compartidos por todas las simulaciones.
    param_variants : list[dict]
        Lista de B dicts. Cada dict contiene SOLO los parámetros que varían
        (e.g., {"forcing_scale": 0.01, "macro_coupling": 0.2, "damping": 0.1}).
    steps : int
        Número de timesteps a simular.
    seed : int
        Semilla base. Cada simulación en el batch usa la misma semilla
        (determinismo reproducible).
    series_key : str
        Clave de la serie de salida.
    init_range : float
        Rango de la perturbación inicial del grid.
    max_batch : int
        Máximo de simulaciones por sub-batch (0 = auto, basado en VRAM).
        Útil para controlar el uso de VRAM en refinamientos masivos.
    
    Returns
    -------
    main_series : np.ndarray, shape (B, steps)
        Series principales de todas las B simulaciones. Ya en CPU (NumPy).
    
    Notas
    -----
    - Para B=200, n=200: VRAM = 200×200×200×8 = 64MB → cabe en cualquier GPU.
    - Para B=2000, n=500: VRAM = 2000×500×500×8 = 4GB → cabe en RTX 5070 Ti.
    - La GPU se satura con B×n²≥1M floats (operaciones vectoriales masivas).
    - Forcing, gradients, macro_mode="mean" soportados. macro_mode="dynamic" NO
      (requiere estado serial → fallback a simulate_abm_core uno por uno).
    """
    if not using_gpu():
        # Sin GPU: ejecutar uno por uno con CPU (no podemos paralelizar así)
        results = []
        for pv in param_variants:
            p = dict(base_params)
            p.update(pv)
            p["assimilation_strength"] = 0.0
            p["assimilation_series"] = None
            p["_store_grid"] = False
            from abm_core import simulate_abm_core as _cpu_fn
            sim = _cpu_fn(p, steps, seed=seed, series_key=series_key, init_range=init_range)
            results.append(sim[series_key][:steps])
        return np.array(results, dtype=np.float64)
    
    _xp = xp
    B = len(param_variants)
    
    if B == 0:
        return np.empty((0, steps), dtype=np.float64)
    
    # Auto-batch: estimar VRAM necesaria y dividir si es necesario
    n = int(base_params.get("grid_size", 20))
    vram_per_sim = n * n * 8 * 6  # ~6 arrays temporales por sim (grid, acc, count, noise, etc.)
    vram_total = B * vram_per_sim
    
    # Calcular límite VRAM (60% de la total para seguridad)
    try:
        from gpu_backend import _GPU_MEM_GB as _mem_gb
        vram_limit = int(_mem_gb * 0.6 * 1024**3)
    except (ImportError, AttributeError):
        vram_limit = 8 * 1024**3
    
    if max_batch > 0:
        effective_batch = max_batch
    else:
        effective_batch = max(1, vram_limit // max(vram_per_sim, 1))
    
    if B > effective_batch:
        # Dividir en sub-batches
        all_results = []
        for i in range(0, B, effective_batch):
            chunk = param_variants[i:i + effective_batch]
            chunk_result = simulate_abm_batch(
                base_params, chunk, steps, seed, series_key, init_range, max_batch=effective_batch
            )
            all_results.append(chunk_result)
        return np.concatenate(all_results, axis=0)
    
    # ─── Extraer parámetros compartidos (con override por variante) ────
    diff_default = float(base_params.get("diffusion", 0.2))
    noise_default = float(base_params.get("noise", 0.02))
    
    # Parámetros que varían: arrays (B,) en GPU
    fs_arr = _xp.array([float(pv.get("forcing_scale", base_params.get("forcing_scale", 0.01)))
                         for pv in param_variants], dtype=_xp.float64)
    mc_arr = _xp.array([float(pv.get("macro_coupling", base_params.get("macro_coupling", 0.3)))
                         for pv in param_variants], dtype=_xp.float64)
    dmp_arr = _xp.array([float(pv.get("damping", base_params.get("damping", 0.02)))
                          for pv in param_variants], dtype=_xp.float64)
    # Diffusion y noise pueden variar por simulación (para C2/C5/noise_sensitivity)
    diff_arr = _xp.array([float(pv.get("diffusion", diff_default))
                           for pv in param_variants], dtype=_xp.float64)
    noise_arr = _xp.array([float(pv.get("noise", pv.get("base_noise", noise_default)))
                            for pv in param_variants], dtype=_xp.float64)
    # Detectar si varían (para optimizar: escalar vs array)
    _diff_varies = not _xp.all(diff_arr == diff_arr[0])
    _noise_varies = not _xp.all(noise_arr == noise_arr[0])
    diff = diff_default if not _diff_varies else None
    noise_amp = noise_default if not _noise_varies else None
    
    # Forcing — construir en CPU, enviar a GPU como vector (steps,)
    forcing = base_params.get("forcing_series")
    if forcing is None:
        base_f = float(base_params.get("forcing_base", 0.0))
        trend = float(base_params.get("forcing_trend", 0.0))
        amp = float(base_params.get("forcing_seasonal_amp", 0.0))
        period = float(base_params.get("forcing_seasonal_period", 12.0))
        t_arr = np.arange(steps)
        forcing = (base_f + trend * t_arr + amp * np.sin(2 * np.pi * t_arr / period)).tolist()
    forcing_gpu = to_device(np.array(forcing[:steps], dtype=np.float64))
    
    # Forcing gradient (compartido)
    fg = None
    forcing_gradient = base_params.get("forcing_gradient")
    if forcing_gradient is not None:
        fg_np = np.asarray(forcing_gradient, dtype=np.float64)
        if fg_np.shape == (n, n):
            fg = to_device(fg_np)
    else:
        gtype = base_params.get("forcing_gradient_type")
        if gtype:
            strength = float(base_params.get("forcing_gradient_strength", 0.6))
            fg = _create_forcing_gradient_gpu(n, gtype, strength)
    
    # Detectar macro_mode
    macro_mode = base_params.get("macro_mode")
    macro_gain = _infer_macro_gain(base_params)
    if macro_mode is None:
        macro_mode = "dynamic" if abs(macro_gain) > 1e-12 else "mean"
    
    if macro_mode == "dynamic":
        # dynamic requiere estado serial → no se puede batchear fácilmente
        # Fallback: ejecutar uno por uno (aún en GPU, pero secuencial)
        results = []
        for pv in param_variants:
            p = dict(base_params)
            p.update(pv)
            p["assimilation_strength"] = 0.0
            p["assimilation_series"] = None
            p["_store_grid"] = False
            sim = simulate_abm_core(p, steps, seed=seed, series_key=series_key, init_range=init_range)
            results.append(sim[series_key][:steps])
        return np.array(results, dtype=np.float64)
    
    # ─── macro_mode == "mean": full batch en GPU ──────────────────────
    rng = get_rng(seed)
    
    # Grid center / init_range compartidos
    macro_init = _infer_macro_init(base_params, series_key)
    grid_center = float(base_params.get("grid_center", macro_init))
    init_range = float(base_params.get("init_range", init_range))
    
    # Grids iniciales: (B, n, n) — todas con el mismo patrón + perturbación
    # Usamos la misma perturbación para todas (reproducibilidad determinista)
    init_noise = rng.uniform(-init_range, init_range, (n, n))  # (n, n) en GPU
    grids = _xp.full((B, n, n), grid_center, dtype=_xp.float64) + init_noise[None, :, :]
    
    # Heterogeneidad (compartida)
    hetero = float(base_params.get("heterogeneity_strength", 0.0))
    hetero_seed = int(base_params.get("heterogeneity_seed", seed))
    if hetero > 1e-8:
        rng_h = np.random.RandomState(hetero_seed)
        diff_map = to_device(np.clip(diff * (1.0 + hetero * rng_h.normal(0, 1, (n, n))), 0, 1).astype(np.float64))
        dmp_base_map = to_device(np.clip(float(base_params.get("damping", 0.02)) * (1.0 + hetero * rng_h.normal(0, 1, (n, n))), 0, 1).astype(np.float64))
        noise_map = to_device(np.clip(noise_amp * (1.0 + hetero * rng_h.normal(0, 1, (n, n))), 0, None).astype(np.float64))
        use_hetero = True
    else:
        use_hetero = False
    
    # Resultado: (B, steps) en GPU
    main_series_gpu = _xp.zeros((B, steps), dtype=_xp.float64)
    
    # ─── Loop temporal: todas las B sims avanzan en paralelo ──────────
    for t in range(steps):
        f = forcing_gpu[t]  # escalar en GPU
        f_spatial = f if fg is None else f * fg  # (n, n) o escalar
        
        # Neighbor mean batch: (B, n, n)
        nb_mean = _neighbor_mean_batch(grids)
        
        # Macro mean por sim: (B,)
        macro_mean = grids.mean(axis=(1, 2))  # (B,)
        
        # Noise batch: (B, n, n)
        if use_hetero:
            noise = rng.uniform(-1.0, 1.0, (B, n, n)) * noise_map[None, :, :]
        elif _noise_varies:
            noise = rng.uniform(-1.0, 1.0, (B, n, n)) * noise_arr[:, None, None]
        else:
            noise = rng.uniform(-noise_amp, noise_amp, (B, n, n))
        
        # Update vectorizado: broadcasting (B,) → (B, 1, 1) sobre (B, n, n)
        if use_hetero:
            grids = (
                grids
                + diff_map[None, :, :] * (nb_mean - grids)
                + fs_arr[:, None, None] * f_spatial
                + mc_arr[:, None, None] * (macro_mean[:, None, None] - grids)
                - dmp_base_map[None, :, :] * dmp_arr[:, None, None] / float(base_params.get("damping", 0.02) or 0.02) * grids
                + noise
            )
        elif _diff_varies:
            grids = (
                grids
                + diff_arr[:, None, None] * (nb_mean - grids)
                + fs_arr[:, None, None] * f_spatial
                + mc_arr[:, None, None] * (macro_mean[:, None, None] - grids)
                - dmp_arr[:, None, None] * grids
                + noise
            )
        else:
            grids = (
                grids
                + diff_default * (nb_mean - grids)
                + fs_arr[:, None, None] * f_spatial
                + mc_arr[:, None, None] * (macro_mean[:, None, None] - grids)
                - dmp_arr[:, None, None] * grids
                + noise
            )
        
        # Sanitize
        grids = _xp.clip(_xp.nan_to_num(grids, nan=0.0, posinf=1e6, neginf=-1e6), -1e6, 1e6)
        
        # Store macro mean por sim
        main_series_gpu[:, t] = grids.mean(axis=(1, 2))
    
    sync()
    
    # Una sola transferencia GPU → CPU al final: (B, steps)
    return to_numpy(main_series_gpu)

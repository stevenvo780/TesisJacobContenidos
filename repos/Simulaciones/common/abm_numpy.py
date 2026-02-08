"""
abm_numpy.py — Motor ABM vectorizado con NumPy.

Reemplaza los loops Python puro por operaciones vectorizadas.
Speedup esperado: 50-100x sobre la implementación de listas.

La dinámica es idéntica a los ABMs individuales:
  new_grid = grid
    + diff * (neighbor_mean - grid)
    + forcing_scale * f
    + macro_coupling * (macro - grid)
    - damping * grid
    + noise

La difusión usa convolución con kernel de vecinos (roll + promedio).
"""

import numpy as np


def _neighbor_mean(grid):
    """Promedio de vecinos 4-conectados usando np.roll (borde periódico corregido)."""
    n = grid.shape[0]
    acc = np.zeros_like(grid)
    count = np.full_like(grid, 4.0)

    acc += np.roll(grid, 1, axis=0)   # arriba
    acc += np.roll(grid, -1, axis=0)  # abajo
    acc += np.roll(grid, 1, axis=1)   # izquierda
    acc += np.roll(grid, -1, axis=1)  # derecha

    # Corregir bordes (no son periódicos en el ABM original)
    # Fila 0: no tiene vecino arriba
    acc[0, :] -= np.roll(grid, 1, axis=0)[0, :]
    count[0, :] -= 1
    # Fila n-1: no tiene vecino abajo
    acc[-1, :] -= np.roll(grid, -1, axis=0)[-1, :]
    count[-1, :] -= 1
    # Col 0: no tiene vecino izquierda
    acc[:, 0] -= np.roll(grid, 1, axis=1)[:, 0]
    count[:, 0] -= 1
    # Col n-1: no tiene vecino derecha
    acc[:, -1] -= np.roll(grid, -1, axis=1)[:, -1]
    count[:, -1] -= 1

    return acc / count


def _neighbor_mean_topology(grid, adj_matrix):
    """
    Promedio de vecinos usando matriz de adyacencia arbitraria.
    grid: (N, N) o (N*N,) flat state
    adj_matrix: (N*N, N*N) sparse or dense matrix
    """
    flat_grid = grid.ravel()
    # Suma de vecinos: A @ x
    neighbor_sum = adj_matrix @ flat_grid
    
    # Conteo de vecinos (degree vector)
    # Se recomienda que adj_matrix ya esté normalizada por fila (Stochastic Matrix)
    # Si no, calculamos degree:
    # degree = np.sum(adj_matrix, axis=1)
    # return (neighbor_sum / degree).reshape(grid.shape)
    
    # Asumimos que la matriz de entrada puede no estar normalizada,
    # pero para eficiencia, si es estática, debería pre-calcularse el normalizador.
    # Aquí calculamos dinámicamente para generalidad (lento si es dense)
    # Optimización: adj_matrix debería ser row-normalized w_ij = a_ij / d_i
    
    return neighbor_sum.reshape(grid.shape)


def simulate_abm_numpy(params, steps, seed=2, series_key="tbar",
                       init_center=0.0, init_range=0.5,
                       store_grid=True, adjacency_matrix=None):
    """
    ABM vectorizado. Compatible con la interfaz de todos los casos.

    Args:
        params: dict con grid_size, diffusion, noise, macro_coupling,
                forcing_scale, damping, forcing_series, etc.
        steps: número de pasos
        seed: semilla para reproducibilidad
        series_key: nombre de la serie principal en el resultado
        init_center: centro de inicialización (default 0.0, clima usa t0)
        init_range: rango de inicialización uniforme
        store_grid: si True, almacena grid completo (necesario para métricas)

    Returns:
        dict con series_key, "grid", "forcing"
    """
    rng = np.random.RandomState(seed)
    n = params.get("grid_size", 20)
    diff = params.get("diffusion", 0.2)
    noise_amp = params.get("noise", 0.02)
    mc = params.get("macro_coupling", 0.3)
    fs = params.get("forcing_scale", 0.01)
    dmp = params.get("damping", 0.02)
    perturbation_event = params.get("perturbation_event", None)  # {"step": t, "magnitude": mag}
    perturbation_event = params.get("perturbation_event", None)  # {"step": t, "magnitude": mag}
    assim_series = params.get("assimilation_series")
    assim_strength = params.get("assimilation_strength", 0.0)
    reflexivity_gamma = params.get("reflexivity_gamma", 0.0)
    reflexivity_target = params.get("reflexivity_target", 0.5)  # Punto de equilibrio homeostático O target dinámico

    # Inicialización
    center = params.get("t0", init_center)
    grid = center + rng.uniform(-init_range, init_range, (n, n))

    forcing = params.get("forcing_series")
    if forcing is None:
        # Generar forcing sinusoidal (caso_clima style)
        base = params.get("forcing_base", 0.0)
        trend = params.get("forcing_trend", 0.0)
        amp = params.get("forcing_seasonal_amp", 0.0)
        period = params.get("forcing_seasonal_period", 12.0)
        t_arr = np.arange(steps)
        forcing = base + trend * t_arr + amp * np.sin(2 * np.pi * t_arr / period)
        forcing = forcing.tolist()

    main_series = []
    grid_series = [] if store_grid else None

    for t in range(steps):
        f = forcing[t]
        macro = grid.mean()

        # Difusión vectorizada
        if adjacency_matrix is not None:
             # Si se provee topología, asumir que es una matriz normalizada (Row-Stochastic)
             # o una matriz de pesos donde (A @ grid) da el "campo medio" local
             nb_mean = _neighbor_mean_topology(grid, adjacency_matrix)
        else:
             # Grilla regular rápida
             nb_mean = _neighbor_mean(grid)

        # Update vectorizado completo
        noise_matrix = rng.uniform(-noise_amp, noise_amp, (n, n))
        grid = (
            grid
            + diff * (nb_mean - grid)
            + fs * f
            + mc * (macro - grid)
            - dmp * grid
            + noise_matrix
        )

        # Perturbación (Test de Viscosidad)
        if perturbation_event and t == perturbation_event["step"]:
            grid += perturbation_event.get("magnitude", 0.0)

        # Nudging
        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                macro_post = grid.mean()
                grid += assim_strength * (target - macro_post)

        macro_final = float(grid.mean())
        
        # Reflexividad: El estado macro altera los parámetros para t+1
        # Ejemplo: Si el sistema se desvía mucho, la 'regulación' (forcing/damping) aumenta
        if reflexivity_gamma > 1e-6:
             # Feedback negativo simple:
             # deviation = macro_final - reflexivity_target
             # forcing_scale (t+1) = forcing_scale (t) * (1 + gamma * deviation)
             # Implementación conservadora: modificar damping o forcing efectivo
             # Aquí modificamos forcing_scale dinámicamente
             
             # Nota: Para estabilidad, clipeamos el cambio
             delta = (macro_final - reflexivity_target)
             fs = max(0.0001, min(1.0, fs * (1.0 + reflexivity_gamma * delta)))
        main_series.append(macro_final)

        if store_grid:
            grid_series.append(grid.tolist())

    result = {
        series_key: main_series,
        "forcing": forcing if isinstance(forcing, list) else forcing.tolist(),
    }
    if store_grid:
        result["grid"] = grid_series
    return result


def make_abm_adapter(series_key, init_center=0.0, init_range=0.5):
    """
    Crea un adaptador compatible con la interfaz simulate_abm(params, steps, seed).

    Usage en validate.py:
        from common.abm_numpy import make_abm_adapter
        simulate_abm = make_abm_adapter("tbar", init_center=14.0, init_range=0.5)
    """
    def simulate_abm(params, steps, seed=2):
        # En calibración no necesitamos grid (ahorra ~80% de memoria)
        store = params.get("_store_grid", True)
        return simulate_abm_numpy(
            params, steps, seed=seed,
            series_key=series_key,
            init_center=params.get("t0", init_center),
            init_range=init_range,
            store_grid=store,
            adjacency_matrix=params.get("adjacency_matrix", None),
        )
    return simulate_abm

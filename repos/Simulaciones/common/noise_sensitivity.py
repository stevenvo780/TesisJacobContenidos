"""
noise_sensitivity.py — Test de sensibilidad al ruido para validación de hiperobjetos.

Verifica que el EDI no sea artefacto del nivel de ruido:
- Re-ejecuta el modelo con 5 niveles de base_noise (0.5×, 0.75×, 1.0×, 1.5×, 2.0× del original)
- El EDI debe mantenerse estable (σ/μ < 0.5 = sensibilidad baja)
- Si EDI colapsa con más ruido → posible artefacto

Paralelizado con joblib para usar todos los cores disponibles.
"""

import os
import numpy as np
from typing import Callable, Dict, List, Tuple, Optional
from joblib import Parallel, delayed

# Niveles de ruido relativos al original
NOISE_MULTIPLIERS = [0.5, 0.75, 1.0, 1.5, 2.0]


def rmse(a, b):
    a, b = np.asarray(a, dtype=np.float64), np.asarray(b, dtype=np.float64)
    n = min(len(a), len(b))
    return float(np.sqrt(np.mean((a[:n] - b[:n])**2)))


def compute_edi(err_coupled, err_reduced):
    if err_reduced < 1e-15:
        return 0.0
    # No clipear a 0: EDI negativo indica coupling contraproducente
    # y eso es estable si se mantiene → información legítima
    raw = (err_reduced - err_coupled) / err_reduced
    return float(np.clip(raw, -1.0, 1.0))


def noise_sensitivity_test(
    base_params: dict,
    eval_params: dict,
    steps: int,
    val_start: int,
    obs_val: np.ndarray,
    simulate_abm_fn: Callable,
    series_key: str,
    original_noise: float = 0.001,
    seed: int = 42,
    multipliers: Optional[List[float]] = None,
) -> Dict:
    """
    Test de sensibilidad al ruido.
    
    Ejecuta el ABM acoplado y desacoplado para cada nivel de ruido,
    calcula EDI en cada caso, y evalúa la estabilidad.
    
    Returns:
        dict con 'edi_per_noise', 'edi_mean', 'edi_std', 'cv', 
        'stable' (bool), 'detail' (lista de dicts)
    """
    if multipliers is None:
        multipliers = NOISE_MULTIPLIERS

    rng = np.random.RandomState(seed)
    # Pre-generar seeds para reproducibilidad (antes de paralelizar)
    level_seeds = [int(rng.randint(0, 100000)) for _ in multipliers]

    def _eval_noise_level(mult, level_seed):
        """Evalúa un nivel de ruido (para paralelizar)."""
        noise_level = original_noise * mult

        # Modelo acoplado (con macro_coupling original)
        params_coupled = dict(eval_params)
        params_coupled["noise"] = noise_level
        params_coupled["base_noise"] = noise_level
        params_coupled["seed"] = level_seed

        try:
            abm_coupled = simulate_abm_fn(params_coupled, steps, seed=level_seed)
        except Exception as e:
            return {
                "noise_mult": mult, "noise_level": noise_level,
                "edi": 0.0, "rmse_coupled": np.nan, "rmse_reduced": np.nan,
                "error": str(e)
            }

        # Modelo reducido (sin macro) — misma seed que coupled
        params_reduced = dict(params_coupled)
        params_reduced["macro_coupling"] = 0.0
        params_reduced["forcing_scale"] = 0.0
        params_reduced["macro_target_series"] = None
        params_reduced["ode_coupling_strength"] = 0.0
        params_reduced["seed"] = level_seed

        try:
            abm_reduced = simulate_abm_fn(params_reduced, steps, seed=level_seed)
        except Exception as e:
            return {
                "noise_mult": mult, "noise_level": noise_level,
                "edi": 0.0, "rmse_coupled": np.nan, "rmse_reduced": np.nan,
                "error": str(e)
            }

        def _reduce(arr):
            arr = np.asarray(arr, dtype=np.float64)
            if arr.ndim == 3:
                return arr.mean(axis=(1, 2))
            return arr

        coupled_val = _reduce(abm_coupled[series_key][val_start:])
        reduced_val = _reduce(abm_reduced[series_key][val_start:])

        n = min(len(coupled_val), len(reduced_val), len(obs_val))
        err_c = rmse(coupled_val[:n], obs_val[:n])
        err_r = rmse(reduced_val[:n], obs_val[:n])
        edi = compute_edi(err_c, err_r)

        return {
            "noise_mult": mult,
            "noise_level": noise_level,
            "edi": edi,
            "rmse_coupled": err_c,
            "rmse_reduced": err_r,
        }

    # Evaluar todos los niveles: GPU serial o CPU paralelo
    try:
        from gpu_backend import using_gpu as _ug
        _has_gpu = _ug()
    except ImportError:
        _has_gpu = False
    
    if _has_gpu:
        results = [_eval_noise_level(mult, lseed) for mult, lseed in zip(multipliers, level_seeds)]
    else:
        n_jobs = min(len(multipliers), os.cpu_count() or 4)
        results = Parallel(n_jobs=n_jobs, backend="loky")(
            delayed(_eval_noise_level)(mult, lseed)
            for mult, lseed in zip(multipliers, level_seeds)
        )

    # Estadísticas
    edis = [r["edi"] for r in results if "error" not in r]
    if len(edis) < 2:
        return {
            "edi_per_noise": edis,
            "edi_mean": np.mean(edis) if edis else 0.0,
            "edi_std": 0.0,
            "cv": 0.0,
            "stable": False,
            "detail": results,
            "message": "Datos insuficientes para test de sensibilidad"
        }

    edi_mean = float(np.mean(edis))
    edi_std = float(np.std(edis))
    cv = edi_std / max(abs(edi_mean), 1e-10)
    stable = cv < 0.5  # Coeficiente de variación < 50%

    # Verificar que EDI no decrezca monótonamente con ruido
    monotonic_decrease = all(
        edis[i] >= edis[i+1] for i in range(len(edis)-1)
    ) and (edis[0] - edis[-1]) > 0.2

    return {
        "edi_per_noise": edis,
        "edi_mean": edi_mean,
        "edi_std": edi_std,
        "cv": cv,
        "stable": stable and not monotonic_decrease,
        "monotonic_decrease": monotonic_decrease,
        "detail": results,
    }


def format_noise_report(result: Dict) -> str:
    """Formatea el resultado del test de sensibilidad en texto legible."""
    lines = ["## Test de Sensibilidad al Ruido", ""]
    lines.append(f"- EDI medio: {result['edi_mean']:.4f} ± {result['edi_std']:.4f}")
    lines.append(f"- CV: {result['cv']:.3f}")
    lines.append(f"- Estable: {'✅ Sí' if result['stable'] else '❌ No'}")
    if result.get("monotonic_decrease"):
        lines.append("- ⚠️ EDI decrece monótonamente con el ruido")
    lines.append("")
    lines.append("| Ruido (×) | Nivel | EDI | RMSE acoplado | RMSE reducido |")
    lines.append("|-----------|-------|-----|---------------|---------------|")
    for d in result.get("detail", []):
        if "error" in d:
            lines.append(f"| {d['noise_mult']:.2f}× | {d['noise_level']:.4f} | ERROR | - | - |")
        else:
            lines.append(
                f"| {d['noise_mult']:.2f}× | {d['noise_level']:.4f} "
                f"| {d['edi']:.4f} | {d['rmse_coupled']:.4f} | {d['rmse_reduced']:.4f} |"
            )
    return "\n".join(lines)

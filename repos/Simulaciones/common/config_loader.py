"""
config_loader.py — Cargador de configuración de ejecución por caso.

Cada caso puede tener un archivo `case_config.json` en su directorio raíz
(repos/Simulaciones/NN_caso_X/case_config.json) con parámetros de ejecución
optimizados: tamaño de grid, iteraciones de refinamiento, etc.

Cadena de prioridad (mayor a menor):
  1. Variables de entorno HYPER_* (override rápido desde bash)
  2. case_config.json del caso
  3. Defaults de CaseConfig en hybrid_validator.py

Uso desde validate.py:
    from config_loader import load_case_config
    overrides = load_case_config()  # auto-detecta el caso desde __file__
    # overrides es un dict que se puede pasar a CaseConfig o usar directamente

Uso desde gpu_run.sh (para leer grid_size sin scraping):
    python3 -c "import json; print(json.load(open('case_config.json'))['execution']['grid_size'])"
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Optional


def find_case_config(start_path: Optional[str] = None) -> Optional[Path]:
    """
    Busca case_config.json subiendo desde start_path hasta la raíz del caso.
    
    Búsqueda: src/ → ../ (raíz del caso) → ../../ (Simulaciones/)
    El archivo se espera en la raíz del caso: NN_caso_X/case_config.json
    """
    if start_path is None:
        # Estrategia 1: usar cwd (validate.py se ejecuta desde src/)
        start_path = os.getcwd()
        
        # Estrategia 2: recorrer la pila buscando un __file__ que no sea
        # de common/ (el caller real es validate.py, no hybrid_validator.py)
        try:
            frame = sys._getframe(1)
            while frame:
                fpath = frame.f_globals.get("__file__", "")
                if fpath and "common" not in os.path.basename(os.path.dirname(os.path.abspath(fpath))):
                    candidate_dir = os.path.dirname(os.path.abspath(fpath))
                    # Verificar que tiene case_config.json cerca
                    if (Path(candidate_dir) / "case_config.json").exists() or \
                       (Path(candidate_dir).parent / "case_config.json").exists():
                        start_path = candidate_dir
                        break
                frame = frame.f_back
        except (ValueError, AttributeError):
            pass
    
    p = Path(start_path).resolve()
    
    # Buscar hasta 3 niveles arriba
    for _ in range(4):
        candidate = p / "case_config.json"
        if candidate.exists():
            return candidate
        # También buscar en el padre (si estamos en src/)
        parent_candidate = p.parent / "case_config.json"
        if parent_candidate.exists():
            return parent_candidate
        p = p.parent
    
    return None


def load_case_config(start_path: Optional[str] = None) -> dict:
    """
    Carga la configuración de ejecución del caso.
    
    Retorna un dict con las secciones:
      - execution: grid_size, n_perm, n_boot, n_refine, n_runs, timeout
      - abm: diffusion, noise, heterogeneity_strength, init_range
      - calibration: param_grid con arrays de búsqueda
    
    Si no hay case_config.json, retorna dict vacío.
    Las variables de entorno HYPER_* tienen prioridad sobre el archivo.
    """
    config_path = find_case_config(start_path)
    
    if config_path is None:
        return {}
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"[config_loader] WARN: Error leyendo {config_path}: {e}", file=sys.stderr)
        return {}
    
    print(f"[config_loader] Cargado: {config_path}", file=sys.stderr)
    return config


def apply_config_to_case(config: dict, case_config_obj) -> None:
    """
    Aplica los overrides del case_config.json al objeto CaseConfig.
    
    Se llama desde CaseConfig.__init__ DESPUÉS de los defaults pero
    ANTES de los overrides de variables de entorno (HYPER_*).
    
    Args:
        config: dict cargado de case_config.json
        case_config_obj: instancia de CaseConfig (se modifica in-place)
    """
    execution = config.get("execution", {})
    abm = config.get("abm", {})
    calibration = config.get("calibration", {})
    
    # Execution overrides
    if "grid_size" in execution and case_config_obj.grid_size > 1:
        # Solo subir grid_size, nunca bajar (protección)
        case_config_obj.grid_size = max(
            case_config_obj.grid_size, 
            int(execution["grid_size"])
        )
    if "n_perm" in execution:
        case_config_obj.n_perm = int(execution["n_perm"])
    if "n_boot" in execution:
        case_config_obj.n_boot = int(execution["n_boot"])
    if "n_refine" in execution:
        case_config_obj.n_refine = int(execution["n_refine"])
    if "n_runs" in execution:
        case_config_obj.n_runs = int(execution["n_runs"])
    if "persistence_window" in execution:
        case_config_obj.persistence_window = int(execution["persistence_window"])
    
    # ABM overrides → extra_base_params
    for key in ("diffusion", "noise", "heterogeneity_strength", "init_range",
                "forcing_gradient_type", "forcing_gradient_strength"):
        if key in abm:
            case_config_obj.extra_base_params[key] = abm[key]
    
    # Calibration overrides
    if "param_grid" in calibration:
        case_config_obj.param_grid = calibration["param_grid"]


def get_grid_size_for_case(case_dir: str) -> Optional[int]:
    """
    Lee el grid_size de un caso desde case_config.json.
    Para uso desde scripts bash vía Python one-liner.
    
    Returns:
        grid_size o None si no hay config.
    """
    config_path = Path(case_dir) / "case_config.json"
    if not config_path.exists():
        return None
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        return config.get("execution", {}).get("grid_size")
    except Exception:
        return None

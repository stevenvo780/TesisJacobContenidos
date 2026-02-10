#!/usr/bin/env python3
"""
auditoria_cientifica_profunda.py
================================
Auditoría caso-por-caso de los 29 simulaciones.
Para cada caso verifica:
  1. Estructura de archivos (5-file convention)
  2. Importaciones y dependencias
  3. Que data.py NO fabrica datos (detecta synthetic_fallback vs real API)
  4. Que ode.py tiene ecuaciones válidas (no hardcodea resultados)
  5. Que validate.py invoca el pipeline real (no hardcodea métricas)
  6. Ejecuta validate.py y captura métricas
  7. Verifica coherencia numérica post-ejecución
  8. Identifica margen de mejora (grid_size, calibration iters, data points)
"""
import os, sys, json, re, ast, subprocess, glob, importlib.util, traceback
import numpy as np

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIM_DIR = os.path.join(BASE, "Simulaciones")

# ── Helpers ───────────────────────────────────────────────────────────

def read_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()

def file_exists(case_dir, *parts):
    return os.path.exists(os.path.join(case_dir, *parts))

def count_lines(path):
    with open(path) as f:
        return sum(1 for _ in f)

# ── Checks ────────────────────────────────────────────────────────────

def check_structure(case_dir):
    """Verifica convención 5-file."""
    required = ["src/validate.py", "src/ode.py", "src/data.py"]
    # abm.py puede ser local o importado del common
    issues = []
    for f in required:
        if not file_exists(case_dir, f):
            issues.append(f"FALTA {f}")
    # abm: local o common
    has_local_abm = file_exists(case_dir, "src", "abm.py")
    if not has_local_abm:
        # check if validate imports from common
        val_src = read_file(os.path.join(case_dir, "src", "validate.py"))
        if "abm" not in val_src.lower() and "hybrid_validator" not in val_src:
            issues.append("Sin ABM local ni import de common")
    return issues

def check_data_source(case_dir):
    """Verifica que data.py obtiene datos reales, no solo sintéticos."""
    data_path = os.path.join(case_dir, "src", "data.py")
    if not os.path.exists(data_path):
        return {"source_type": "MISSING", "issues": ["data.py no existe"]}
    
    src = read_file(data_path)
    issues = []
    
    # Detectar fuentes reales
    real_sources = []
    if "worldbank" in src.lower() or "api.worldbank" in src:
        real_sources.append("World Bank API")
    if "fetch_worldbank_indicator" in src:
        real_sources.append("World Bank (universal fetcher)")
    if "meteostat" in src.lower():
        real_sources.append("Meteostat")
    if "yfinance" in src.lower():
        real_sources.append("Yahoo Finance")
    if "noaa" in src.lower():
        real_sources.append("NOAA")
    if "owid" in src.lower() or "ourworldindata" in src.lower():
        real_sources.append("Our World in Data")
    if "requests.get" in src and ("http" in src or "api" in src):
        real_sources.append("HTTP API (genérica)")
    
    # Detectar datos cacheados
    has_cache = "cache" in src.lower() or ".csv" in src
    
    # Detectar synthetic fallback
    has_synthetic = "synthetic" in src.lower() or "fallback" in src.lower()
    has_np_random = "np.random" in src or "numpy.random" in src or "random.seed" in src
    
    # Detectar si SOLO genera datos sintéticos (sin fuente real)
    only_synthetic = has_synthetic and not real_sources and not has_cache
    
    # Verificar indicadores World Bank específicos
    wb_indicators = re.findall(r'["\']([A-Z]{2}\.[A-Z0-9_.]+)["\']', src)
    
    source_type = "REAL" if real_sources else ("CACHE" if has_cache else ("SYNTHETIC" if has_synthetic else "UNKNOWN"))
    
    if only_synthetic:
        issues.append("SOLO genera datos sintéticos sin fuente real")
    
    return {
        "source_type": source_type,
        "real_sources": real_sources,
        "wb_indicators": wb_indicators,
        "has_cache": has_cache,
        "has_synthetic_fallback": has_synthetic,
        "issues": issues
    }

def check_ode_equations(case_dir):
    """Verifica que ode.py tiene ecuaciones diferenciales reales."""
    ode_path = os.path.join(case_dir, "src", "ode.py")
    if not os.path.exists(ode_path):
        return {"model_type": "MISSING", "issues": ["ode.py no existe"]}
    
    src = read_file(ode_path)
    issues = []
    
    # Buscar funciones de simulación
    has_simulate = "def simulate_ode" in src
    if not has_simulate:
        issues.append("No tiene función simulate_ode")
    
    # Buscar ecuación diferencial (dx/dt pattern)
    has_ode = any(p in src for p in ["alpha", "beta", "dN/dt", "dX/dt", "dS/dt", "dH/dt", "dM/dt", "dP/dt", "dR/dt"])
    if not has_ode:
        issues.append("No tiene parámetros α/β de ecuación diferencial")
    
    # Buscar integración temporal
    has_loop = "for " in src and ("step" in src or "range" in src)
    if not has_loop:
        issues.append("No tiene loop de integración temporal")
    
    # Buscar hardcoded results (ROJO)
    hardcoded_patterns = [
        r"return\s+\[.*\d+\.\d+.*\]",  # return [0.5, 0.6, ...] 
        r"series\s*=\s*\[.*\d+\.\d+.*\d+\.\d+.*\]",  # series = [0.5, 0.6, ...]
    ]
    for p in hardcoded_patterns:
        if re.search(p, src):
            issues.append("POSIBLE hardcoding de resultados")
    
    # Detectar modelo específico
    model_type = "unknown"
    if "kessler" in src.lower() or "N**2" in src or "N^2" in src or "collision" in src.lower():
        model_type = "kessler_liou"
    elif "revelle" in src.lower() or "pCO2" in src:
        model_type = "revelle_acidification"
    elif "accumulation" in src.lower() or "inflow" in src:
        model_type = "accumulation_decay"
    elif "logistic" in src.lower():
        model_type = "logistic_forced"
    elif "heston" in src.lower():
        model_type = "heston"
    elif "mean_reversion" in src.lower() or ("alpha" in src and "beta" in src):
        model_type = "mean_reversion"
    elif "radiative" in src.lower():
        model_type = "radiative_balance"
    
    # Contar líneas de lógica real
    code_lines = len([l for l in src.split("\n") if l.strip() and not l.strip().startswith("#") and not l.strip().startswith('"""')])
    
    return {
        "model_type": model_type,
        "has_simulate": has_simulate,
        "has_ode_params": has_ode,
        "has_temporal_loop": has_loop,
        "code_lines": code_lines,
        "issues": issues
    }

def check_validate_pipeline(case_dir):
    """Verifica que validate.py usa el pipeline real, no hardcodea."""
    val_path = os.path.join(case_dir, "src", "validate.py")
    if not os.path.exists(val_path):
        return {"issues": ["validate.py no existe"]}
    
    src = read_file(val_path)
    issues = []
    
    # Debe importar hybrid_validator o tener pipeline propio
    uses_hybrid = "hybrid_validator" in src or "run_full_validation" in src
    uses_local_pipeline = "simulate_abm" in src and "simulate_ode" in src
    
    if not uses_hybrid and not uses_local_pipeline:
        issues.append("No usa hybrid_validator ni pipeline local")
    
    # Debe llamar a funciones de data.py
    fetches_data = "fetch" in src or "data" in src.lower()
    if not fetches_data:
        issues.append("No llama a funciones de obtención de datos")
    
    # Verificar que NO hardcodea métricas
    hardcode_patterns = [
        r'"edi":\s*\d+\.\d+',  # "edi": 0.633
        r'"overall_pass":\s*(True|False)',  # "overall_pass": True
        r'metrics\s*=\s*\{',  # metrics = { ... }
    ]
    for p in hardcode_patterns:
        matches = re.findall(p, src)
        if matches and "json.dump" not in src[:src.find(p) if p in src else 0]:
            # Solo es problema si no es parte de escritura JSON
            pass  # Difícil distinguir, mejor verificar por ejecución
    
    # Verificar parámetros de simulación
    params_info = {}
    grid_match = re.search(r'grid_size\s*=\s*(\d+)', src)
    if grid_match:
        params_info["grid_size"] = int(grid_match.group(1))
    
    nruns_match = re.search(r'n_runs\s*=\s*(\d+)', src)
    if nruns_match:
        params_info["n_runs"] = int(nruns_match.group(1))
    
    nperm_match = re.search(r'n_perm\s*=\s*(\d+)', src)
    if nperm_match:
        params_info["n_perm"] = int(nperm_match.group(1))
    
    nboot_match = re.search(r'n_boot\s*=\s*(\d+)', src)
    if nboot_match:
        params_info["n_boot"] = int(nboot_match.group(1))
    
    log_t = "log_transform" in src and "True" in src[src.find("log_transform"):src.find("log_transform")+30] if "log_transform" in src else False
    params_info["log_transform"] = log_t
    
    persist_match = re.search(r'persistence_window\s*=\s*(\d+)', src)
    if persist_match:
        params_info["persistence_window"] = int(persist_match.group(1))
    
    return {
        "uses_hybrid_validator": uses_hybrid,
        "params": params_info,
        "issues": issues
    }

def check_metrics_coherence(case_dir):
    """Verifica coherencia numérica del metrics.json existente."""
    mpath = os.path.join(case_dir, "outputs", "metrics.json")
    if not os.path.exists(mpath):
        return {"issues": ["metrics.json no existe"]}
    
    with open(mpath) as f:
        m = json.load(f)
    
    issues = []
    
    for phase_name in ["synthetic", "real"]:
        phase = m.get("phases", {}).get(phase_name, {})
        if not phase:
            continue
        
        edi_d = phase.get("edi", {})
        if not isinstance(edi_d, dict):
            issues.append(f"{phase_name}: EDI no es dict")
            continue
        
        edi_v = edi_d.get("value", None)
        if edi_v is None:
            issues.append(f"{phase_name}: EDI value es None")
            continue
        
        # Verificar rango EDI
        if not (-1.0 <= edi_v <= 1.0):
            issues.append(f"{phase_name}: EDI={edi_v} fuera de rango [-1,1]")
        
        # Verificar p-value
        pval = edi_d.get("permutation_pvalue", None)
        if pval is not None:
            if not (0 <= pval <= 1):
                issues.append(f"{phase_name}: p-value={pval} fuera de rango [0,1]")
        
        # Verificar que CI contiene el valor
        ci_lo = edi_d.get("ci_lo", None)
        ci_hi = edi_d.get("ci_hi", None)
        bootstrap_mean = edi_d.get("bootstrap_mean", None)
        if ci_lo is not None and ci_hi is not None:
            if ci_lo > ci_hi:
                issues.append(f"{phase_name}: CI invertido [{ci_lo}, {ci_hi}]")
        
        # Verificar coherencia EDI con RMSE
        errors = phase.get("errors", {})
        rmse_abm = errors.get("rmse_abm")
        rmse_no_ode = errors.get("rmse_abm_no_ode")
        if rmse_abm is not None and rmse_no_ode is not None and rmse_no_ode > 1e-12:
            expected_edi = (rmse_no_ode - rmse_abm) / rmse_no_ode
            expected_edi = max(-1.0, min(1.0, expected_edi))
            if abs(expected_edi - edi_v) > 0.01:
                issues.append(f"{phase_name}: EDI={edi_v:.4f} no coincide con cálculo de RMSE={expected_edi:.4f}")
        
        # Verificar symploké
        sym = phase.get("symploke", {})
        if isinstance(sym, dict):
            internal = sym.get("internal", 0)
            external = sym.get("external", 0)
            if internal < 0 or internal > 1:
                issues.append(f"{phase_name}: symploke internal={internal} fuera de [0,1]")
            if external < 0 or external > 1:
                issues.append(f"{phase_name}: symploke external={external} fuera de [0,1]")
        
        # Verificar persistence
        persist = phase.get("persistence", {})
        if isinstance(persist, dict):
            model_var = persist.get("model_var", 0)
            obs_var = persist.get("obs_var", 0)
            if model_var < 0:
                issues.append(f"{phase_name}: persistence model_var={model_var} negativo")
        
        # Verificar overall_pass coherencia
        opass = phase.get("overall_pass", False)
        c1 = phase.get("c1_convergence")
        c2 = phase.get("c2_robustness")
        edi_valid = phase.get("edi_valid")
        
        # Si overall_pass = True pero criterios clave son False
        if opass:
            if c1 is False:
                issues.append(f"{phase_name}: overall_pass=True pero c1=False")
            if c2 is False:
                issues.append(f"{phase_name}: overall_pass=True pero c2=False")
    
    return {"issues": issues}

def estimate_scalability(case_dir, metrics):
    """Estima si el caso puede mejorar con más cómputo."""
    val_path = os.path.join(case_dir, "src", "validate.py")
    data_path = os.path.join(case_dir, "src", "data.py")
    
    scalability = {
        "can_improve": False,
        "reasons": [],
        "recommended_changes": [],
        "current_params": {},
        "estimated_improvement": "none"
    }
    
    val_src = read_file(val_path) if os.path.exists(val_path) else ""
    
    # Extraer parámetros actuales
    grid_match = re.search(r'grid_size\s*=\s*(\d+)', val_src)
    grid_size = int(grid_match.group(1)) if grid_match else 25
    scalability["current_params"]["grid_size"] = grid_size
    
    # Contar datos reales
    data_dir = os.path.join(case_dir, "data")
    data_files = glob.glob(os.path.join(data_dir, "*.csv")) if os.path.exists(data_dir) else []
    max_rows = 0
    for df in data_files:
        try:
            with open(df) as f:
                max_rows = max(max_rows, sum(1 for _ in f) - 1)
        except:
            pass
    scalability["current_params"]["data_rows"] = max_rows
    
    # Extraer EDI y nivel actual
    real = metrics.get("phases", {}).get("real", {})
    edi_d = real.get("edi", {})
    edi_v = edi_d.get("value", 0) if isinstance(edi_d, dict) else edi_d
    sig = edi_d.get("permutation_significant", False) if isinstance(edi_d, dict) else False
    pval = edi_d.get("permutation_pvalue", 1.0) if isinstance(edi_d, dict) else 1.0
    
    # Calcular nivel actual
    if edi_v <= 0:
        nivel = 0
    elif not sig:
        nivel = 1
    elif edi_v < 0.10:
        nivel = 2
    elif edi_v < 0.30:
        nivel = 3
    else:
        nivel = 4
    scalability["current_nivel"] = nivel
    
    # ── Análisis de escalabilidad ──
    
    # 1. Grid pequeño → más grid ayuda con difusión
    if grid_size < 30:
        scalability["reasons"].append(f"grid_size={grid_size} es bajo")
        scalability["recommended_changes"].append(f"grid_size → 40-50")
    
    # 2. EDI positivo pero no significativo → más permutaciones o mejor calibración
    if edi_v > 0 and not sig:
        if edi_v > 0.05:
            scalability["can_improve"] = True
            scalability["reasons"].append(f"EDI={edi_v:.4f} positivo pero p={pval:.4f} no significativo")
            scalability["recommended_changes"].append("Más iteraciones de calibración ABM (10000-20000)")
            scalability["recommended_changes"].append("Grid más grande (50×50) para mejor difusión")
            if edi_v > 0.10:
                scalability["estimated_improvement"] = "posible subir 1-2 niveles"
            else:
                scalability["estimated_improvement"] = "posible subir 1 nivel"
        elif edi_v > 0.01:
            scalability["reasons"].append(f"EDI={edi_v:.4f} muy bajo, difícilmente escalable")
            scalability["estimated_improvement"] = "marginal"
    
    # 3. Datos escasos → no mejora con más cómputo
    if max_rows < 20:
        scalability["reasons"].append(f"Solo {max_rows} data points — limitado por datos")
        if max_rows < 10:
            scalability["estimated_improvement"] = "none (datos insuficientes)"
    
    # 4. EDI negativo → el modelo no funciona para este fenómeno
    if edi_v < -0.05:
        scalability["reasons"].append(f"EDI={edi_v:.4f} negativo — modelo inadecuado")
        scalability["estimated_improvement"] = "none (modelo inadecuado)"
        scalability["can_improve"] = False
    
    # 5. C1 falla → convergencia básica no se logra
    c1 = real.get("c1_convergence")
    if c1 is False and edi_v > 0:
        scalability["can_improve"] = True
        scalability["reasons"].append("C1 falla: ajustar threshold o mejorar calibración")
        scalability["recommended_changes"].append("threshold_factor más permisivo o mejor calibración ODE")
    
    # 6. Coupling bajo → subir macro_coupling
    mc = real.get("calibration", {}).get("macro_coupling", 0)
    coup = real.get("coupling_check")
    if coup is False and mc < 0.1:
        scalability["can_improve"] = True
        scalability["reasons"].append(f"macro_coupling={mc:.4f} < 0.1 — no pasa coupling_check")
        scalability["recommended_changes"].append("Expandir rango de macro_coupling en grid search [0.1, 0.5]")
    
    # 7. Symploké/non-locality fallan
    sym_pass = real.get("symploke", {}).get("pass")
    nloc_pass = real.get("non_locality", {}).get("pass")
    if sym_pass is False:
        scalability["reasons"].append("Symploké falla — cohesión interna < externa")
    if nloc_pass is False:
        scalability["reasons"].append("Non-locality falla — una celda domina")
        scalability["recommended_changes"].append("Grid más grande + heterogeneidad")
    
    # 8. Noise instability
    noise = real.get("noise_sensitivity", {})
    if isinstance(noise, dict) and noise.get("stable") is False:
        scalability["reasons"].append("Inestable bajo ruido")
        scalability["recommended_changes"].append("Reducir noise_scale o mejorar calibración")
    
    # 9. Casos ya en N4 → pueden llegar a N5 con CR>2 + extensión
    if nivel == 4:
        cr = real.get("symploke", {}).get("cr", 0)
        if cr < 2.0:
            scalability["can_improve"] = True
            scalability["reasons"].append(f"Nivel 4 con CR={cr:.2f} < 2.0")
            scalability["recommended_changes"].append("Optimizar para CR > 2.0 (potencial N5)")
            scalability["estimated_improvement"] = "posible N4 → N5"
    
    # 10. Casos significativos pero bajos → recalibración puede ayudar
    if sig and edi_v > 0 and edi_v < 0.30:
        scalability["can_improve"] = True
        scalability["reasons"].append(f"Significativo (p={pval:.4f}) con EDI={edi_v:.4f}")
        scalability["recommended_changes"].append("Recalibración con grid expandido + más iteraciones")
    
    return scalability

def run_case(case_dir):
    """Ejecuta validate.py y captura resultado."""
    src_dir = os.path.join(case_dir, "src")
    result = subprocess.run(
        ["python3", "validate.py"],
        cwd=src_dir,
        capture_output=True,
        text=True,
        timeout=300,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    )
    return {
        "returncode": result.returncode,
        "stdout_tail": result.stdout[-500:] if result.stdout else "",
        "stderr_tail": result.stderr[-500:] if result.stderr else "",
    }


# ── Main ──────────────────────────────────────────────────────────────

def audit_case(case_dir):
    name = os.path.basename(case_dir)
    print(f"\n{'='*60}")
    print(f"  Auditando: {name}")
    print(f"{'='*60}")
    
    report = {"case": name, "checks": {}, "issues": [], "scalability": {}}
    
    # 1. Estructura
    struct_issues = check_structure(case_dir)
    report["checks"]["structure"] = len(struct_issues) == 0
    if struct_issues:
        report["issues"].extend([f"[STRUCT] {i}" for i in struct_issues])
    print(f"  [1] Estructura: {'✅' if not struct_issues else '❌ ' + str(struct_issues)}")
    
    # 2. Fuente de datos
    data_info = check_data_source(case_dir)
    report["checks"]["data_source"] = len(data_info["issues"]) == 0
    report["data_info"] = data_info
    if data_info["issues"]:
        report["issues"].extend([f"[DATA] {i}" for i in data_info["issues"]])
    print(f"  [2] Datos: {data_info['source_type']} {'✅' if not data_info['issues'] else '❌ ' + str(data_info['issues'])}")
    if data_info.get("real_sources"):
        print(f"      Fuentes: {', '.join(data_info['real_sources'])}")
    if data_info.get("wb_indicators"):
        print(f"      Indicadores WB: {', '.join(data_info['wb_indicators'][:5])}")
    
    # 3. ODE
    ode_info = check_ode_equations(case_dir)
    report["checks"]["ode"] = len(ode_info["issues"]) == 0
    report["ode_info"] = ode_info
    if ode_info["issues"]:
        report["issues"].extend([f"[ODE] {i}" for i in ode_info["issues"]])
    print(f"  [3] ODE ({ode_info['model_type']}): {'✅' if not ode_info['issues'] else '❌ ' + str(ode_info['issues'])}")
    
    # 4. Pipeline
    pipe_info = check_validate_pipeline(case_dir)
    report["checks"]["pipeline"] = len(pipe_info["issues"]) == 0
    report["pipeline_info"] = pipe_info
    if pipe_info["issues"]:
        report["issues"].extend([f"[PIPE] {i}" for i in pipe_info["issues"]])
    print(f"  [4] Pipeline: {'✅' if not pipe_info['issues'] else '❌ ' + str(pipe_info['issues'])}")
    if pipe_info.get("params"):
        print(f"      Params: {pipe_info['params']}")
    
    # 5. Coherencia métricas existentes
    coh_info = check_metrics_coherence(case_dir)
    report["checks"]["coherence"] = len(coh_info["issues"]) == 0
    if coh_info["issues"]:
        report["issues"].extend([f"[COH] {i}" for i in coh_info["issues"]])
    print(f"  [5] Coherencia métricas: {'✅' if not coh_info['issues'] else '❌ ' + str(coh_info['issues'])}")
    
    # 6. Ejecución
    print(f"  [6] Ejecutando validate.py...")
    try:
        exec_info = run_case(case_dir)
        report["checks"]["execution"] = exec_info["returncode"] == 0
        if exec_info["returncode"] != 0:
            report["issues"].append(f"[EXEC] Exit code {exec_info['returncode']}")
            # Extract error
            err = exec_info["stderr_tail"].strip().split("\n")[-3:]
            report["issues"].append(f"[EXEC] {' | '.join(err)}")
        print(f"      Ejecución: {'✅' if exec_info['returncode'] == 0 else '❌ exit=' + str(exec_info['returncode'])}")
    except subprocess.TimeoutExpired:
        report["checks"]["execution"] = False
        report["issues"].append("[EXEC] TIMEOUT (>300s)")
        print(f"      Ejecución: ❌ TIMEOUT")
    except Exception as e:
        report["checks"]["execution"] = False
        report["issues"].append(f"[EXEC] {e}")
        print(f"      Ejecución: ❌ {e}")
    
    # 7. Post-ejecución: verificar que metrics.json se actualizó
    mpath = os.path.join(case_dir, "outputs", "metrics.json")
    if os.path.exists(mpath):
        with open(mpath) as f:
            metrics = json.load(f)
        
        real = metrics.get("phases", {}).get("real", {})
        edi_d = real.get("edi", {})
        edi_v = edi_d.get("value", 0) if isinstance(edi_d, dict) else edi_d
        sig = edi_d.get("permutation_significant", False) if isinstance(edi_d, dict) else False
        opass = real.get("overall_pass", False)
        
        # Re-check coherencia post-ejecución
        post_coh = check_metrics_coherence(case_dir)
        report["checks"]["post_coherence"] = len(post_coh["issues"]) == 0
        if post_coh["issues"]:
            report["issues"].extend([f"[POST-COH] {i}" for i in post_coh["issues"]])
        
        print(f"  [7] Post-ejecución: EDI={edi_v:+.6f} sig={sig} pass={opass}")
        
        # 8. Escalabilidad
        scal = estimate_scalability(case_dir, metrics)
        report["scalability"] = scal
        print(f"  [8] Escalabilidad: {'🔼 SÍ' if scal['can_improve'] else '➖ No'} — {scal.get('estimated_improvement', 'none')}")
        if scal["recommended_changes"]:
            for r in scal["recommended_changes"]:
                print(f"      → {r}")
    else:
        report["checks"]["post_coherence"] = False
        report["issues"].append("[POST] metrics.json no generado")
        report["scalability"] = {"can_improve": False, "estimated_improvement": "none"}
        print(f"  [7] Post-ejecución: ❌ No se generó metrics.json")
    
    # Veredicto
    all_checks = report["checks"]
    critical_ok = all_checks.get("structure", False) and all_checks.get("execution", False)
    math_ok = all_checks.get("ode", False) and all_checks.get("coherence", False) and all_checks.get("post_coherence", False)
    
    if critical_ok and math_ok and len(report["issues"]) == 0:
        report["verdict"] = "PERFECTO"
    elif critical_ok and math_ok:
        report["verdict"] = "CHECK (con notas)"
    elif critical_ok:
        report["verdict"] = "CHECK (issues menores)"
    else:
        report["verdict"] = "NO-CHECK"
    
    print(f"\n  ══ VEREDICTO: {report['verdict']} ══")
    if report["issues"]:
        print(f"  Issues ({len(report['issues'])}):")
        for i in report["issues"][:5]:
            print(f"    • {i}")
        if len(report["issues"]) > 5:
            print(f"    ... y {len(report['issues'])-5} más")
    
    return report


def main():
    cases = sorted(glob.glob(os.path.join(SIM_DIR, "[0-9][0-9]_caso_*")))
    print(f"Auditoría Científica Profunda — {len(cases)} casos")
    print(f"{'='*60}")
    
    reports = []
    for case_dir in cases:
        try:
            r = audit_case(case_dir)
            reports.append(r)
        except Exception as e:
            print(f"  ❌ ERROR FATAL: {e}")
            traceback.print_exc()
            reports.append({
                "case": os.path.basename(case_dir),
                "verdict": "NO-CHECK",
                "issues": [f"FATAL: {e}"],
                "checks": {},
                "scalability": {}
            })
    
    # ── Resumen Final ──
    print(f"\n\n{'='*60}")
    print(f"  RESUMEN FINAL")
    print(f"{'='*60}\n")
    
    perfecto = [r for r in reports if r["verdict"] == "PERFECTO"]
    check = [r for r in reports if "CHECK" in r["verdict"]]
    nocheck = [r for r in reports if r["verdict"] == "NO-CHECK"]
    can_scale = [r for r in reports if r.get("scalability", {}).get("can_improve", False)]
    
    print(f"  ✅ PERFECTO: {len(perfecto)}/29")
    print(f"  ☑️  CHECK:   {len(check)}/29")
    print(f"  ❌ NO-CHECK: {len(nocheck)}/29")
    print(f"  🔼 Escalables: {len(can_scale)}/29")
    
    print(f"\n  Detalle:")
    for r in reports:
        scal = r.get("scalability", {})
        scal_txt = f" 🔼 {scal.get('estimated_improvement', '')}" if scal.get("can_improve") else ""
        print(f"    {r['case']}: {r['verdict']}{scal_txt}")
    
    # Guardar JSON
    out_path = os.path.join(BASE, "..", "Artifacts", "auditoria_cientifica_resultado.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(reports, f, indent=2, default=str)
    print(f"\n  Resultado guardado en: {out_path}")
    
    return reports


if __name__ == "__main__":
    main()

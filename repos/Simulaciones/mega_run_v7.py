#!/usr/bin/env python3
"""
mega_run_v7.py — Ejecuta los 32 casos de simulación secuencialmente.
Usa multiprocessing para paralelizar la calibración dentro de cada caso.
Diseñado para la torre (32 cores, 128GB RAM).

Uso:
    python3 mega_run_v7.py                  # Todos los 32 casos
    python3 mega_run_v7.py 14 17 31         # Solo casos específicos
    python3 mega_run_v7.py --skip-validated  # Solo no-validados
"""

import json
import os
import sys
import time
import traceback
import shutil
import glob


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COMMON_DIR = os.path.join(BASE_DIR, "common")
TESIS_DIR = os.path.join(BASE_DIR, "..", "TesisDesarrollo", "02_Modelado_Simulacion")

# Todos los 32 casos en orden
ALL_CASES = [
    "01_caso_clima",
    "02_caso_conciencia",
    "03_caso_contaminacion",
    "04_caso_energia",
    "05_caso_epidemiologia",
    "06_caso_estetica",
    "07_caso_falsacion_exogeneidad",
    "08_caso_falsacion_no_estacionariedad",
    "09_caso_falsacion_observabilidad",
    "10_caso_finanzas",
    "11_caso_justicia",
    "12_caso_moderacion_adversarial",
    "13_caso_movilidad",
    "14_caso_paradigmas",
    "15_caso_politicas_estrategicas",
    "16_caso_postverdad",
    "17_caso_rtb_publicidad",
    "18_caso_wikipedia",
    "19_caso_deforestacion",
    "20_caso_oceanos",
    "21_caso_urbanizacion",
    "22_caso_acidificacion_oceanica",
    "23_caso_kessler",
    "24_caso_salinizacion",
    "25_caso_fosforo",
    "26_caso_erosion_dialectica",
    "27_caso_microplasticos",
    "28_caso_acuiferos",
    "29_caso_starlink",
    "30_caso_riesgo_biologico",
    "31_caso_fuga_cerebros",
    "32_caso_iot",
]


def run_case(case_name):
    """Ejecuta un caso individual y retorna (case_name, success, edi, overall_pass, elapsed)."""
    case_dir = os.path.join(BASE_DIR, case_name)
    src_dir = os.path.join(case_dir, "src")
    
    if not os.path.exists(os.path.join(src_dir, "validate.py")):
        return case_name, False, None, None, 0, "No validate.py"
    
    t0 = time.time()
    
    # Ejecutar validate.py desde su directorio src/
    original_dir = os.getcwd()
    original_path = sys.path[:]
    
    try:
        os.chdir(src_dir)
        sys.path.insert(0, src_dir)
        sys.path.insert(0, COMMON_DIR)
        
        # Importar y ejecutar
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "validate", os.path.join(src_dir, "validate.py")
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()
        
        elapsed = time.time() - t0
        
        # Leer resultados
        metrics_path = os.path.join(case_dir, "outputs", "metrics.json")
        if os.path.exists(metrics_path):
            with open(metrics_path) as f:
                m = json.load(f)
            r = m.get("phases", {}).get("real", {})
            edi_raw = r.get("edi", 0)
            edi = edi_raw["value"] if isinstance(edi_raw, dict) else edi_raw
            overall = r.get("overall_pass", False)
            return case_name, True, edi, overall, elapsed, "OK"
        else:
            return case_name, True, None, None, elapsed, "No metrics output"
    
    except Exception as e:
        elapsed = time.time() - t0
        return case_name, False, None, None, elapsed, str(e)[:200]
    
    finally:
        os.chdir(original_dir)
        sys.path[:] = original_path
        # Limpiar módulos importados para evitar colisiones
        for mod_name in list(sys.modules.keys()):
            if mod_name in ("validate", "abm", "ode", "metrics", "data"):
                del sys.modules[mod_name]


def copy_to_tesis(case_name):
    """Copia metrics.json y report.md al directorio de TesisDesarrollo."""
    src_out = os.path.join(BASE_DIR, case_name, "outputs")
    tesis_case = os.path.join(TESIS_DIR, case_name)
    
    if not os.path.exists(tesis_case):
        os.makedirs(tesis_case, exist_ok=True)
    
    for fname in ("metrics.json", "report.md"):
        src = os.path.join(src_out, fname)
        dst = os.path.join(tesis_case, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)


def main():
    skip_validated = "--skip-validated" in sys.argv
    
    # Determinar qué casos ejecutar
    case_nums = [a for a in sys.argv[1:] if a.isdigit()]
    if case_nums:
        cases = []
        for num in case_nums:
            matching = [c for c in ALL_CASES if c.startswith(num.zfill(2))]
            cases.extend(matching)
    else:
        cases = ALL_CASES[:]
    
    if skip_validated:
        filtered = []
        for c in cases:
            mf = os.path.join(TESIS_DIR, c, "metrics.json")
            if os.path.exists(mf):
                m = json.load(open(mf))
                if m.get("phases", {}).get("real", {}).get("overall_pass", False):
                    print(f"⏭️  {c}: ya validado, saltando")
                    continue
            filtered.append(c)
        cases = filtered
    
    total = len(cases)
    print(f"\n{'='*70}")
    print(f"  MEGA RUN v7 — {total} casos a ejecutar")
    print(f"  Inicio: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}\n", flush=True)
    
    results = []
    validated = 0
    failed = 0
    
    for idx, case_name in enumerate(cases, 1):
        print(f"\n[{idx}/{total}] ▶ {case_name}", flush=True)
        print(f"  {'─'*50}", flush=True)
        
        name, success, edi, overall, elapsed, msg = run_case(case_name)
        
        if success:
            edi_str = f"{edi:.3f}" if edi is not None else "N/A"
            status = "✅ VALIDADO" if overall else "❌ Rechazado"
            print(f"  Resultado: {status} | EDI={edi_str} | {elapsed:.1f}s", flush=True)
            
            if overall:
                validated += 1
            
            # Copiar resultados a TesisDesarrollo
            copy_to_tesis(case_name)
        else:
            print(f"  ⚠️  ERROR: {msg} | {elapsed:.1f}s", flush=True)
            failed += 1
        
        results.append({
            "case": name,
            "success": success,
            "edi": edi,
            "overall_pass": overall,
            "elapsed": elapsed,
            "message": msg,
        })
    
    # Resumen final
    print(f"\n{'='*70}")
    print(f"  RESUMEN MEGA RUN v7")
    print(f"  Fin: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}")
    print(f"  Total ejecutados: {total}")
    print(f"  Validados: {validated}")
    print(f"  Rechazados: {total - validated - failed}")
    print(f"  Errores: {failed}")
    print(f"{'='*70}")
    
    # Tabla resumen
    print(f"\n{'Caso':<45} {'EDI':>8} {'Pass':>8} {'Tiempo':>8}")
    print("-" * 72)
    for r in results:
        edi_str = f"{r['edi']:.3f}" if r['edi'] is not None else "N/A"
        pass_str = "✅" if r['overall_pass'] else ("⚠️" if not r['success'] else "❌")
        time_str = f"{r['elapsed']:.1f}s"
        print(f"  {r['case']:<43} {edi_str:>8} {pass_str:>8} {time_str:>8}")
    
    # Guardar log JSON
    log_path = os.path.join(BASE_DIR, "mega_run_v7_results.json")
    with open(log_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nLog guardado en: {log_path}")


if __name__ == "__main__":
    main()

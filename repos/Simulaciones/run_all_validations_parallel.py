"""
run_all_validations_parallel.py
Ejecución paralela de validate.py por caso con logs, EDI parsing y resumen.

Usa ThreadPoolExecutor + subprocess para máximo paralelismo sin contención GIL.
Limita threads BLAS/OpenMP por proceso para evitar over-subscription.

Uso:
    python3 run_all_validations_parallel.py                    # Todos los casos
    python3 run_all_validations_parallel.py --pattern "0[1-5]" # Solo casos 01-05
    python3 run_all_validations_parallel.py --cases 1,2,3      # Casos específicos
    python3 run_all_validations_parallel.py --max-workers 16   # Limitar workers
    python3 run_all_validations_parallel.py --timeout 300      # Timeout por caso
"""

import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from glob import glob

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_PATH, "outputs_run")
LOG_DIR = os.path.join(OUTPUT_DIR, "logs")


def _discover_cases(pattern=None, case_nums=None):
    """Descubre todos los validate.py disponibles, opcionalmente filtrados."""
    paths = sorted(glob(os.path.join(BASE_PATH, "[0-9][0-9]_caso_*", "src", "validate.py")))
    if case_nums:
        paths = [p for p in paths
                 if int(os.path.basename(os.path.dirname(os.path.dirname(p))).split("_")[0]) in case_nums]
    elif pattern:
        rx = re.compile(pattern)
        paths = [p for p in paths if rx.search(p)]
    return paths


def _parse_edi_from_log(log_path):
    """Extrae EDI sintético y real del log."""
    edi_syn, edi_real = None, None
    overall_pass = None
    try:
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                ll = line.lower()
                # Patron: "Phase synthetic: EDI=X.XXX" o "synthetic: ... EDI=X.XXX"
                if "synthetic" in ll and "edi" in ll:
                    m = re.search(r'EDI[=:]\s*([-\d.eE+]+)', line, re.IGNORECASE)
                    if m:
                        try:
                            edi_syn = float(m.group(1))
                        except ValueError:
                            pass
                elif "real" in ll and "edi" in ll:
                    m = re.search(r'EDI[=:]\s*([-\d.eE+]+)', line, re.IGNORECASE)
                    if m:
                        try:
                            edi_real = float(m.group(1))
                        except ValueError:
                            pass
                # overall_pass
                if "overall_pass" in ll:
                    if "true" in ll:
                        overall_pass = True
                    elif "false" in ll:
                        overall_pass = False
    except Exception:
        pass
    return edi_syn, edi_real, overall_pass


def _run_one(validate_path, timeout, env):
    """Ejecuta un validate.py y captura resultado."""
    src_dir = os.path.dirname(validate_path)  # src/ directory — CRUCIAL para imports
    case_dir = os.path.dirname(src_dir)
    case_name = os.path.basename(case_dir)

    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"{case_name}.log")

    start = time.time()
    cmd = [sys.executable, "validate.py"]
    rc = None
    err = None

    with open(log_path, "w", encoding="utf-8") as logf:
        try:
            proc = subprocess.run(
                cmd,
                cwd=src_dir,  # IMPORTANTE: cwd=src/ para que imports funcionen
                stdout=logf,
                stderr=subprocess.STDOUT,
                env=env,
                timeout=timeout,
            )
            rc = proc.returncode
        except subprocess.TimeoutExpired:
            rc = -9
            err = "timeout"
        except Exception as exc:
            rc = -1
            err = str(exc)

    dur = time.time() - start
    edi_syn, edi_real, overall_pass = _parse_edi_from_log(log_path)

    return {
        "case": case_name,
        "returncode": rc,
        "duration_s": round(dur, 2),
        "edi_synthetic": edi_syn,
        "edi_real": edi_real,
        "overall_pass": overall_pass,
        "log": log_path,
        "error": err,
    }


def main():
    parser = argparse.ArgumentParser(description="Ejecución paralela de todas las validaciones")
    parser.add_argument("--pattern", help="Regex para filtrar nombres de caso")
    parser.add_argument("--cases", type=str, help="Números de caso separados por coma (ej: 1,2,3)")
    parser.add_argument("--max-workers", type=int, default=None,
                        help="Workers paralelos (default: min(ncpu, ncasos))")
    parser.add_argument("--timeout", type=int, default=600,
                        help="Timeout por caso en segundos (default: 600)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Solo listar casos sin ejecutar")
    args = parser.parse_args()

    case_nums = None
    if args.cases:
        case_nums = set(int(x.strip()) for x in args.cases.split(","))

    paths = _discover_cases(pattern=args.pattern, case_nums=case_nums)
    if not paths:
        print("No se encontraron validate.py para ejecutar.")
        return 1

    if args.dry_run:
        for p in paths:
            case_name = os.path.basename(os.path.dirname(os.path.dirname(p)))
            print(f"  {case_name}: {p}")
        print(f"\nTotal: {len(paths)} casos")
        return 0

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)

    cpu = os.cpu_count() or 4
    max_workers = args.max_workers or min(cpu, len(paths))

    # Evitar over-subscription: 1 thread BLAS por subproceso
    env = os.environ.copy()
    env["OMP_NUM_THREADS"] = "1"
    env["MKL_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    env["NUMEXPR_NUM_THREADS"] = "1"
    env.setdefault("SIM_SHARED_CACHE", os.path.join(BASE_PATH, "data_cache", "shared"))

    print("=" * 72)
    print(f"  VALIDACIÓN PARALELA — {len(paths)} casos")
    print(f"  Workers: {max_workers} | CPUs: {cpu} | Timeout: {args.timeout}s")
    print(f"  Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 72)
    print()

    results = []
    completed = 0
    start_all = time.time()

    with cf.ThreadPoolExecutor(max_workers=max_workers) as ex:
        future_to_case = {}
        for p in paths:
            case_name = os.path.basename(os.path.dirname(os.path.dirname(p)))
            fut = ex.submit(_run_one, p, args.timeout, env)
            future_to_case[fut] = case_name

        for fut in cf.as_completed(future_to_case):
            res = fut.result()
            results.append(res)
            completed += 1

            status = "✅" if res["returncode"] == 0 else "❌"
            edi_str = f"EDI_syn={res['edi_synthetic']:.3f}" if res['edi_synthetic'] is not None else "EDI=?"
            edi_r_str = f"EDI_real={res['edi_real']:.3f}" if res['edi_real'] is not None else ""
            err_str = f" [{res['error']}]" if res['error'] else ""
            print(f"  [{completed:2d}/{len(paths)}] {status} {res['case']:<42} "
                  f"{edi_str:<18} {edi_r_str:<20} {res['duration_s']:>6.1f}s{err_str}")

    total_time = round(time.time() - start_all, 2)
    seq_time = sum(r["duration_s"] for r in results)

    results.sort(key=lambda r: r["case"])

    print()
    print("=" * 72)
    print("  RESUMEN DE RESULTADOS")
    print("=" * 72)
    print()
    print(f"  {'#':<4} {'Caso':<42} {'EDI_syn':<10} {'EDI_real':<10} {'Pass':<6} {'St':<5} {'Time'}")
    print("  " + "-" * 86)

    ok = fail = edi_valid_count = 0
    for r in results:
        num = r["case"].split("_")[0]
        name = r["case"]
        e_s = f"{r['edi_synthetic']:.4f}" if r['edi_synthetic'] is not None else "N/A"
        e_r = f"{r['edi_real']:.4f}" if r['edi_real'] is not None else "N/A"
        op = "✅" if r.get("overall_pass") else "❌" if r.get("overall_pass") is False else "?"
        st = "OK" if r["returncode"] == 0 else "FAIL"

        if r["returncode"] == 0:
            ok += 1
        else:
            fail += 1
        if r["edi_synthetic"] is not None and 0.30 <= r["edi_synthetic"] <= 0.90:
            edi_valid_count += 1

        print(f"  {num:<4} {name:<42} {e_s:<10} {e_r:<10} {op:<6} {st:<5} {r['duration_s']:.1f}s")

    print("  " + "-" * 86)
    print()
    print(f"  Ejecución:  {ok} OK / {fail} FAIL de {len(results)} casos")
    print(f"  EDI válido (0.30-0.90 sintético): {edi_valid_count}/{len(results)}")
    print(f"  Tiempo total: {total_time:.1f}s (paralelo)")
    print(f"  Tiempo secuencial estimado: {seq_time:.1f}s")
    if total_time > 0:
        print(f"  Speedup: {seq_time / total_time:.1f}x")
    print()

    summary = {
        "generated_at": datetime.now().isoformat(),
        "total_cases": len(results),
        "success": ok,
        "failed": fail,
        "edi_valid_count": edi_valid_count,
        "total_time_s": total_time,
        "sequential_time_s": round(seq_time, 2),
        "speedup": round(seq_time / total_time, 2) if total_time > 0 else 0,
        "workers": max_workers,
        "results": results,
    }

    summary_path = os.path.join(OUTPUT_DIR, "validation_parallel_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, default=str)

    print(f"  Resumen JSON: {summary_path}")
    print(f"  Logs individuales: {LOG_DIR}/")
    print()
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

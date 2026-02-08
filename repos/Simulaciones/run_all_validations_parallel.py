"""
run_all_validations_parallel.py
Ejecución paralela de validate.py por caso con logs y resumen.
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


def _discover_cases(pattern=None):
    paths = glob(os.path.join(BASE_PATH, "[0-9][0-9]_caso_*", "src", "validate.py"))
    paths = sorted(paths)
    if pattern:
        rx = re.compile(pattern)
        paths = [p for p in paths if rx.search(p)]
    return paths


def _run_one(validate_path, timeout, env):
    case_dir = os.path.dirname(os.path.dirname(validate_path))
    case_name = os.path.basename(case_dir)
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"{case_name}.log")

    start = time.time()
    cmd = [sys.executable, validate_path]
    rc = None
    err = None
    with open(log_path, "w", encoding="utf-8") as logf:
        try:
            proc = subprocess.run(
                cmd,
                cwd=case_dir,
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
    return {
        "case": case_name,
        "path": validate_path,
        "returncode": rc,
        "duration_s": round(dur, 3),
        "log": log_path,
        "error": err,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pattern", help="Regex para filtrar casos")
    parser.add_argument("--max-workers", type=int, default=None)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    paths = _discover_cases(args.pattern)
    if not paths:
        print("No hay validate.py que ejecutar.")
        return 1

    if args.dry_run:
        for p in paths:
            print(p)
        return 0

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)

    cpu = os.cpu_count() or 4
    max_workers = args.max_workers or min(cpu, 12)

    env = os.environ.copy()
    env.setdefault("OMP_NUM_THREADS", "1")
    env.setdefault("MKL_NUM_THREADS", "1")
    env.setdefault("OPENBLAS_NUM_THREADS", "1")
    env.setdefault("NUMEXPR_NUM_THREADS", "1")
    env.setdefault("SIM_SHARED_CACHE", os.path.join(BASE_PATH, "data_cache", "shared"))

    print(f"Casos: {len(paths)} | max_workers={max_workers} | timeout={args.timeout}s")

    results = []
    start_all = time.time()
    with cf.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(_run_one, p, args.timeout, env) for p in paths]
        for fut in cf.as_completed(futures):
            res = fut.result()
            results.append(res)
            status = "OK" if res["returncode"] == 0 else "FAIL"
            print(f"[{status}] {res['case']} ({res['duration_s']}s)")

    total = round(time.time() - start_all, 3)
    ok = sum(1 for r in results if r["returncode"] == 0)
    fail = len(results) - ok

    summary = {
        "generated_at": datetime.now().isoformat(),
        "total_cases": len(results),
        "success": ok,
        "failed": fail,
        "total_time_s": total,
        "results": sorted(results, key=lambda r: r["case"]),
    }

    summary_path = os.path.join(OUTPUT_DIR, "validation_parallel_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Resumen: {ok} OK / {fail} FAIL | total={total}s")
    print(f"Resumen JSON: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

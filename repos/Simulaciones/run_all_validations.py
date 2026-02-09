#!/usr/bin/env python3
"""
run_all_validations.py — Parallel Execution of All 20 Cases

Runs all case validations in parallel using multiprocessing
to maximize CPU utilization.

Usage:
    python3 run_all_validations.py
    python3 run_all_validations.py --cases 1,2,3  # Run specific cases
    python3 run_all_validations.py --workers 4     # Limit parallelism
"""

import os
import sys
import time
import argparse
import subprocess
from multiprocessing import Pool, cpu_count
from datetime import datetime

# All 20 cases (excluding 21-29 which are handled by someone else)
ALL_CASES = [
    "01_caso_clima",
    "02_caso_conciencia", 
    "03_caso_contaminacion",
    "04_caso_energia",
    "05_caso_epidemiologia",
    "06_caso_falsacion_exogeneidad",
    "07_caso_falsacion_no_estacionariedad",
    "08_caso_falsacion_observabilidad",
    "09_caso_finanzas",
    "10_caso_justicia",
    "11_caso_movilidad",
    "12_caso_paradigmas",
    "13_caso_politicas_estrategicas",
    "14_caso_postverdad",
    "15_caso_wikipedia",
    "16_caso_deforestacion",
    "17_caso_oceanos",
    "18_caso_urbanizacion",
    "19_caso_acidificacion_oceanica",
    "20_caso_kessler",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_single_case(case_name):
    """Run a single case validation and return results."""
    start_time = time.time()
    case_dir = os.path.join(BASE_DIR, case_name, "src")
    validate_script = os.path.join(case_dir, "validate.py")
    
    if not os.path.exists(validate_script):
        return {
            "case": case_name,
            "status": "SKIP",
            "error": f"No validate.py found",
            "duration": 0,
            "edi": None
        }
    
    try:
        result = subprocess.run(
            [sys.executable, validate_script],
            cwd=case_dir,
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout per case
        )
        
        duration = time.time() - start_time
        
        # Parse EDI from output
        edi = None
        for line in result.stdout.split('\n'):
            if 'EDI=' in line:
                try:
                    edi_str = line.split('EDI=')[1].split()[0]
                    edi = float(edi_str)
                except:
                    pass
        
        if result.returncode == 0:
            return {
                "case": case_name,
                "status": "OK",
                "error": None,
                "duration": duration,
                "edi": edi,
                "stdout": result.stdout[-500:] if len(result.stdout) > 500 else result.stdout
            }
        else:
            return {
                "case": case_name,
                "status": "FAIL",
                "error": result.stderr[-500:] if len(result.stderr) > 500 else result.stderr,
                "duration": duration,
                "edi": edi
            }
            
    except subprocess.TimeoutExpired:
        return {
            "case": case_name,
            "status": "TIMEOUT",
            "error": "Exceeded 10 minute timeout",
            "duration": 600,
            "edi": None
        }
    except Exception as e:
        return {
            "case": case_name,
            "status": "ERROR",
            "error": str(e),
            "duration": time.time() - start_time,
            "edi": None
        }


def main():
    parser = argparse.ArgumentParser(description="Run all case validations in parallel")
    parser.add_argument("--cases", type=str, help="Comma-separated list of case numbers to run (e.g., 1,2,3)")
    parser.add_argument("--workers", type=int, default=None, help="Number of parallel workers (default: CPU count)")
    args = parser.parse_args()
    
    # Determine cases to run
    if args.cases:
        case_nums = [int(x.strip()) for x in args.cases.split(",")]
        cases_to_run = [c for c in ALL_CASES if int(c.split("_")[0]) in case_nums]
    else:
        cases_to_run = ALL_CASES
        
    # Determine worker count
    n_workers = args.workers or max(1, cpu_count() - 1)  # Leave one core free
    
    print(f"=" * 60)
    print(f"  PARALLEL VALIDATION OF {len(cases_to_run)} CASES")
    print(f"  Workers: {n_workers} | CPUs: {cpu_count()}")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"=" * 60)
    print()
    
    start_total = time.time()
    
    # Run in parallel
    with Pool(processes=n_workers) as pool:
        results = pool.map(run_single_case, cases_to_run)
    
    total_duration = time.time() - start_total
    
    # Print results
    print()
    print(f"=" * 60)
    print(f"  RESULTS SUMMARY")
    print(f"=" * 60)
    print()
    print(f"{'Case':<40} {'Status':<8} {'EDI':<10} {'Time':<10}")
    print("-" * 68)
    
    ok_count = 0
    fail_count = 0
    
    for r in results:
        status = r["status"]
        case = r["case"]
        edi = f"{r['edi']:.4f}" if r['edi'] is not None else "N/A"
        duration = f"{r['duration']:.1f}s"
        
        if status == "OK":
            ok_count += 1
            status_str = "✅ OK"
        elif status == "SKIP":
            status_str = "⏭️ SKIP"
        elif status == "TIMEOUT":
            fail_count += 1
            status_str = "⏰ TIMEOUT"
        else:
            fail_count += 1
            status_str = "❌ FAIL"
            
        print(f"{case:<40} {status_str:<8} {edi:<10} {duration:<10}")
        
        if r.get("error"):
            print(f"    Error: {r['error'][:100]}...")
            
    print("-" * 68)
    print(f"Total: {ok_count} OK, {fail_count} Failed, {len(results) - ok_count - fail_count} Skipped")
    print(f"Total Time: {total_duration:.1f}s (parallelized)")
    print(f"Sequential Time (est): {sum(r['duration'] for r in results):.1f}s")
    print(f"Speedup: {sum(r['duration'] for r in results) / total_duration:.1f}x")
    print()
    
    # Write results to file
    results_file = os.path.join(BASE_DIR, "validation_results.txt")
    with open(results_file, "w") as f:
        f.write(f"Validation Results - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        for r in results:
            f.write(f"{r['case']}: {r['status']} | EDI={r.get('edi', 'N/A')} | {r['duration']:.1f}s\n")
            if r.get("error"):
                f.write(f"  Error: {r['error']}\n")
        f.write(f"\nTotal: {ok_count}/{len(results)} OK\n")
        
    print(f"Results saved to: {results_file}")
    
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
replay_and_verify.py — Re-ejecuta todos los casos y verifica integridad.

Uso:
  # Generar hashes de referencia (primera vez)
  python replay_and_verify.py --generate

  # Verificar contra hashes existentes
  python replay_and_verify.py --verify

  # Re-ejecutar un solo caso
  python replay_and_verify.py --case caso_clima --generate
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent  # repos/Simulaciones
CASES_DIR = REPO_ROOT / "caso_clima"  # Detect parent
if not CASES_DIR.exists():
    REPO_ROOT = Path(__file__).resolve().parent  # Already in Simulaciones
HASH_FILE = REPO_ROOT / "replay_hashes.json"


def find_cases(repo_root: Path):
    """Encuentra todos los directorios caso_* con validate.py."""
    cases = []
    for d in sorted(repo_root.iterdir()):
        if d.is_dir() and d.name.startswith("caso_"):
            validate = d / "src" / "validate.py"
            if validate.exists():
                cases.append(d.name)
    return cases


def run_case(case_name: str, repo_root: Path, timeout: int = 120) -> dict:
    """Ejecuta un caso y retorna status + hash del metrics.json."""
    src_dir = repo_root / case_name / "src"
    outputs_dir = repo_root / case_name / "outputs"
    metrics_file = outputs_dir / "metrics.json"

    # Limpiar outputs previos
    if metrics_file.exists():
        metrics_file.unlink()

    try:
        result = subprocess.run(
            [sys.executable, "validate.py"],
            cwd=str(src_dir),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        exit_code = result.returncode
        stderr_tail = result.stderr[-500:] if result.stderr else ""
    except subprocess.TimeoutExpired:
        return {
            "case": case_name,
            "exit_code": -1,
            "error": "TIMEOUT",
            "hash": None,
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        return {
            "case": case_name,
            "exit_code": -1,
            "error": str(e),
            "hash": None,
            "timestamp": datetime.now().isoformat(),
        }

    # Calcular hash del metrics.json
    metrics_hash = None
    edi_value = None
    overall_pass = None
    if metrics_file.exists():
        content = metrics_file.read_bytes()
        metrics_hash = hashlib.md5(content).hexdigest()
        try:
            m = json.loads(content)
            real = m.get("real", {})
            edi_value = real.get("edi", {}).get("value")
            overall_pass = real.get("overall_pass")
        except Exception:
            pass

    return {
        "case": case_name,
        "exit_code": exit_code,
        "hash": metrics_hash,
        "edi": edi_value,
        "overall_pass": overall_pass,
        "error": stderr_tail if exit_code != 0 else None,
        "timestamp": datetime.now().isoformat(),
    }


def generate_hashes(repo_root: Path, case_filter: str = None):
    """Ejecuta todos los casos y guarda hashes de referencia."""
    cases = find_cases(repo_root)
    if case_filter:
        cases = [c for c in cases if case_filter in c]

    print(f"📋 Generando hashes para {len(cases)} casos...")
    results = {}

    for i, case in enumerate(cases, 1):
        print(f"  [{i}/{len(cases)}] {case}...", end=" ", flush=True)
        r = run_case(case, repo_root)
        results[case] = r
        status = "✅" if r["exit_code"] == 0 else "❌"
        edi_str = f"EDI={r['edi']:.4f}" if r["edi"] is not None else "no-EDI"
        print(f"{status} exit={r['exit_code']} {edi_str} hash={r['hash'][:8] if r['hash'] else 'N/A'}")

    # Guardar
    output = {
        "generated": datetime.now().isoformat(),
        "python": sys.executable,
        "n_cases": len(cases),
        "results": results,
    }

    with open(HASH_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n💾 Hashes guardados en {HASH_FILE}")
    
    # Resumen
    ok = sum(1 for r in results.values() if r["exit_code"] == 0)
    print(f"📊 Resumen: {ok}/{len(cases)} exitosos")


def verify_hashes(repo_root: Path):
    """Re-ejecuta y compara contra hashes guardados."""
    if not HASH_FILE.exists():
        print("❌ No hay archivo de hashes. Ejecuta primero con --generate")
        sys.exit(1)

    with open(HASH_FILE) as f:
        ref = json.load(f)

    ref_results = ref["results"]
    cases = list(ref_results.keys())
    print(f"🔍 Verificando {len(cases)} casos contra hashes de {ref['generated']}...")

    matches = 0
    mismatches = 0
    errors = 0

    for i, case in enumerate(cases, 1):
        print(f"  [{i}/{len(cases)}] {case}...", end=" ", flush=True)
        r = run_case(case, repo_root)
        ref_hash = ref_results[case].get("hash")

        if r["exit_code"] != 0:
            print(f"❌ ERROR exit={r['exit_code']}")
            errors += 1
        elif r["hash"] == ref_hash:
            print(f"✅ MATCH hash={r['hash'][:8]}")
            matches += 1
        else:
            print(f"⚠️  MISMATCH ref={ref_hash[:8] if ref_hash else 'N/A'} new={r['hash'][:8] if r['hash'] else 'N/A'}")
            # Comparar EDIs
            ref_edi = ref_results[case].get("edi")
            if ref_edi is not None and r["edi"] is not None:
                delta = abs(r["edi"] - ref_edi)
                print(f"     EDI: ref={ref_edi:.4f} new={r['edi']:.4f} Δ={delta:.4f}")
            mismatches += 1

    print(f"\n📊 Resumen: {matches} matches, {mismatches} mismatches, {errors} errores")
    if mismatches > 0 or errors > 0:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Replay & Verify simulaciones")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", action="store_true", help="Generar hashes de referencia")
    group.add_argument("--verify", action="store_true", help="Verificar contra hashes")
    parser.add_argument("--case", type=str, default=None, help="Filtrar por nombre de caso")
    args = parser.parse_args()

    # Detectar raíz del repo
    repo_root = Path(__file__).resolve().parent
    if not (repo_root / "caso_clima").exists():
        repo_root = repo_root.parent
    if not (repo_root / "caso_clima").exists():
        print("❌ No se encuentra el directorio de casos")
        sys.exit(1)

    global HASH_FILE
    HASH_FILE = repo_root / "replay_hashes.json"

    if args.generate:
        generate_hashes(repo_root, args.case)
    else:
        verify_hashes(repo_root)


if __name__ == "__main__":
    main()

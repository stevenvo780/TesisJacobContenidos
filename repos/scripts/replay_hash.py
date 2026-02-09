#!/usr/bin/env python3
"""
replay_hash.py — Genera y verifica hashes MD5 de todos los outputs de simulación.

Uso:
  python3 replay_hash.py                  # Genera hashes para todos los casos
  python3 replay_hash.py --verify         # Verifica contra hashes guardados
  python3 replay_hash.py --save           # Guarda baseline de hashes
  python3 replay_hash.py --case 01_caso_clima  # Solo un caso

Salida: tabla por caso con hash de metrics.json + report.md
"""

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

SIMS_DIR = Path(__file__).resolve().parent.parent / "Simulaciones"
THESIS_DIR = Path(__file__).resolve().parent.parent.parent / "TesisDesarrollo" / "02_Modelado_Simulacion"
HASH_BASELINE = Path(__file__).resolve().parent / "replay_baseline.json"


def md5_file(path: Path) -> str:
    """Computa MD5 de un archivo."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_hashes(case_filter: str = None) -> dict:
    """Recoge hashes de metrics.json y report.md para cada caso."""
    results = {}

    for caso_dir in sorted(SIMS_DIR.glob("[0-9]*_caso_*")):
        caso_name = caso_dir.name
        if case_filter and case_filter not in caso_name:
            continue

        outputs_dir = caso_dir / "outputs"
        entry = {"metrics_md5": None, "report_md5": None}

        metrics_path = outputs_dir / "metrics.json"
        report_path = outputs_dir / "report.md"

        if metrics_path.exists():
            entry["metrics_md5"] = md5_file(metrics_path)
        if report_path.exists():
            entry["report_md5"] = md5_file(report_path)

        # También checkear en TesisDesarrollo
        thesis_pattern = list(THESIS_DIR.glob(f"*{caso_name}*"))
        if thesis_pattern:
            thesis_metrics = thesis_pattern[0] / "metrics.json"
            thesis_report = thesis_pattern[0] / "report.md"
            if thesis_metrics.exists():
                entry["thesis_metrics_md5"] = md5_file(thesis_metrics)
            if thesis_report.exists():
                entry["thesis_report_md5"] = md5_file(thesis_report)
            # Coherencia: metrics.json en Simulaciones == TesisDesarrollo?
            if entry["metrics_md5"] and entry.get("thesis_metrics_md5"):
                entry["sync"] = entry["metrics_md5"] == entry["thesis_metrics_md5"]

        results[caso_name] = entry

    return results


def print_table(hashes: dict):
    """Imprime tabla de hashes en consola."""
    print(f"{'Caso':<40} {'metrics.json':<34} {'report.md':<34} {'sync':>5}")
    print("-" * 115)
    for caso, h in sorted(hashes.items()):
        m = h.get("metrics_md5", "—") or "—"
        r = h.get("report_md5", "—") or "—"
        s = "✓" if h.get("sync") else ("✗" if h.get("sync") is False else "—")
        print(f"{caso:<40} {m:<34} {r:<34} {s:>5}")


def save_baseline(hashes: dict):
    """Guarda baseline de hashes a disco."""
    with open(HASH_BASELINE, "w") as f:
        json.dump(hashes, f, indent=2)
    print(f"\n✅ Baseline guardado en {HASH_BASELINE} ({len(hashes)} casos)")


def verify_baseline(hashes: dict) -> bool:
    """Verifica hashes actuales contra baseline guardado."""
    if not HASH_BASELINE.exists():
        print("❌ No existe baseline. Ejecuta primero con --save")
        return False

    with open(HASH_BASELINE) as f:
        baseline = json.load(f)

    changed = []
    missing = []
    ok = 0

    for caso, bh in sorted(baseline.items()):
        current = hashes.get(caso, {})
        if not current.get("metrics_md5"):
            missing.append(caso)
            continue
        if current["metrics_md5"] != bh.get("metrics_md5"):
            changed.append(caso)
        else:
            ok += 1

    new_cases = set(hashes.keys()) - set(baseline.keys())

    print(f"\n📊 Resultado de verificación:")
    print(f"  ✓ Sin cambios: {ok}")
    print(f"  ✗ Cambiados:   {len(changed)}")
    print(f"  ? Faltantes:   {len(missing)}")
    print(f"  + Nuevos:      {len(new_cases)}")

    if changed:
        print(f"\n⚠️  Casos con hash diferente al baseline:")
        for c in changed:
            print(f"    {c}: {baseline[c].get('metrics_md5','—')[:12]}… → {hashes[c].get('metrics_md5','—')[:12]}…")

    return len(changed) == 0 and len(missing) == 0


def main():
    parser = argparse.ArgumentParser(description="Replay hash — verificación de reproducibilidad")
    parser.add_argument("--verify", action="store_true", help="Verifica contra baseline guardado")
    parser.add_argument("--save", action="store_true", help="Guarda baseline de hashes")
    parser.add_argument("--case", type=str, default=None, help="Filtrar por nombre de caso")
    args = parser.parse_args()

    hashes = collect_hashes(args.case)
    print_table(hashes)

    if args.save:
        save_baseline(hashes)
    elif args.verify:
        ok = verify_baseline(hashes)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Genera un resumen de metricas para todas las simulaciones.

Uso:
  python3 scripts/evaluar_simulaciones.py > /tmp/reporte.md

Opcional:
  python3 scripts/evaluar_simulaciones.py --write
"""
from pathlib import Path
import json
import math
import argparse

ROOT = Path(__file__).resolve().parents[2]
CASES_ROOT = ROOT / 'TesisDesarrollo' / '02_Modelado_Simulacion'
OUTPUT = CASES_ROOT / 'Reporte_General_Simulaciones.md'

# Mapeo categoría → nivel de cierre operativo
NIVEL_MAP = {
    'strong': 4, 'weak': 3, 'suggestive': 2, 'trend': 1, 'null': 0,
    'falsification': None,
}


def read_metrics(case_dir: Path):
    p = case_dir / 'metrics.json'
    if not p.exists():
        return None
    return json.loads(p.read_text())


def compute_metrics(metrics_obj):
    if not metrics_obj:
        return None
    ph = metrics_obj.get('phases', {}).get('real') or metrics_obj.get('phases', {}).get('synthetic')
    if not ph:
        return None
    # EDI: leer valor directo (calculado por hybrid_validator)
    edi = ph.get('edi', {}).get('value')
    # CR: usar campo 'cr' de symploké (abs(internal/external))
    symploke = ph.get('symploke', {})
    cr = symploke.get('cr')
    if cr is None:
        internal = symploke.get('internal')
        external = symploke.get('external')
        if internal is not None and external not in (None, 0):
            cr = abs(internal / external)
    taxonomy = ph.get('emergence_taxonomy', {})
    category = taxonomy.get('category', '?')
    nivel = taxonomy.get('nivel')
    if nivel is None:
        nivel = NIVEL_MAP.get(category)
    return {
        'edi': edi,
        'cr': cr,
        'overall_pass': ph.get('overall_pass'),
        'category': category,
        'nivel': nivel,
    }


def fmt(x):
    if x is None:
        return 'n/a'
    if isinstance(x, float):
        if math.isinf(x):
            return '∞'
        if math.isnan(x):
            return 'NaN'
    return f"{x:.3f}"


def build_table():
    rows = []
    for case_dir in sorted(CASES_ROOT.glob('*_caso_*')):
        metrics_obj = read_metrics(case_dir)
        m = compute_metrics(metrics_obj)
        case = case_dir.name
        report_link = f"`{case_dir.name}/report.md`"
        rows.append((case, m, report_link))

    lines = []
    lines.append("# Reporte General de Simulaciones")
    lines.append("")
    lines.append("| Caso | EDI | CR | Cat | Nivel | Reporte |")
    lines.append("| :--- | ---: | ---: | :--- | :---: | :--- |")
    for case, m, report_link in rows:
        edi = fmt(m['edi']) if m else 'n/a'
        cr = fmt(m['cr']) if m else 'n/a'
        cat = m.get('category', '?') if m else 'n/a'
        nivel = m.get('nivel') if m else None
        nivel_s = str(nivel) if nivel is not None else '—'
        lines.append(f"| {case} | {edi} | {cr} | {cat} | {nivel_s} | {report_link} |")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='Write to Reporte_General_Simulaciones.md')
    args = parser.parse_args()

    table = build_table()
    if args.write:
        OUTPUT.write_text(table.strip() + "\n", encoding='utf-8')
    else:
        print(table)


if __name__ == '__main__':
    main()

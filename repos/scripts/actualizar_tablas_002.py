#!/usr/bin/env python3
"""Actualiza tablas de 02_Modelado_Simulacion usando metrics.json.

- Genera Reporte_General_Simulaciones.md
- Reemplaza la tabla en 02_Modelado_Simulacion.md
"""
from pathlib import Path
import json
import math
import re

ROOT = Path(__file__).resolve().parents[2]
CASES_ROOT = ROOT / 'TesisDesarrollo' / '02_Modelado_Simulacion'
MAIN_DOC = CASES_ROOT / '02_Modelado_Simulacion.md'
REPORT_DOC = CASES_ROOT / 'Reporte_General_Simulaciones.md'


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
    edi_pval = ph.get('edi', {}).get('permutation_pvalue')
    edi_sig = ph.get('edi', {}).get('permutation_significant', False)
    # CR: usar campo 'cr' de symploké (abs(internal/external))
    symploke = ph.get('symploke', {})
    cr = symploke.get('cr')
    if cr is None:
        internal = symploke.get('internal')
        external = symploke.get('external')
        if internal is not None and external not in (None, 0):
            cr = abs(internal / external)
    # Taxonomía
    taxonomy = ph.get('emergence_taxonomy', {})
    category = taxonomy.get('category', '?')
    return {
        'edi': edi,
        'edi_pval': edi_pval,
        'edi_sig': edi_sig,
        'cr': cr,
        'overall_pass': ph.get('overall_pass'),
        'category': category,
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


def build_rows():
    rows = []
    for case_dir in sorted(CASES_ROOT.glob('*_caso_*')):
        metrics_obj = read_metrics(case_dir)
        m = compute_metrics(metrics_obj)
        case = case_dir.name
        report_link = f"`{case_dir.name}/report.md`"
        rows.append((case, m, report_link))
    return rows


def build_table(rows):
    lines = []
    lines.append("| Caso | EDI | p-perm | sig | CR | Cat | Pass | Reporte |")
    lines.append("| :--- | ---: | ---: | :---: | ---: | :--- | :---: | :--- |")
    for case, m, report_link in rows:
        if m:
            edi = fmt(m['edi'])
            pval = fmt(m.get('edi_pval'))
            sig = '✅' if m.get('edi_sig') else '❌'
            cr = fmt(m['cr'])
            cat = m.get('category', '?')
            state = '✅' if m.get('overall_pass') else '❌'
        else:
            edi = pval = cr = 'n/a'
            sig = state = 'n/a'
            cat = 'n/a'
        lines.append(f"| {case} | {edi} | {pval} | {sig} | {cr} | {cat} | {state} | {report_link} |")
    return "\n".join(lines)


def update_report(rows):
    table = build_table(rows)
    content = "# Reporte General de Simulaciones\n\n" + table + "\n"
    REPORT_DOC.write_text(content, encoding='utf-8')


def update_main(rows):
    table = build_table(rows)
    block = "\n".join([
        "## Resultados Consolidados (Matriz de Validación Técnica)",
        "",
        table,
        "",
        "Para recalcular este reporte de forma automatica, usar:",
        "`python3 scripts/actualizar_tablas_002.py`",
        "",
    ])
    text = MAIN_DOC.read_text(encoding='utf-8', errors='ignore')
    # Match both old and new header variants
    text = re.sub(
        r"## Resultados[^\n]*?Matriz de Validaci.n T.cnica\)[\s\S]*?(?=\n## |\Z)",
        block.rstrip(), text
    )
    MAIN_DOC.write_text(text.strip() + "\n", encoding='utf-8')


def main():
    rows = build_rows()
    update_report(rows)
    update_main(rows)


if __name__ == '__main__':
    main()

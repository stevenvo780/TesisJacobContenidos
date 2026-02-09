#!/usr/bin/env python3
"""Audita consistencia documental y metrica de simulaciones sin modificar resultados.

Lee los metrics.json generados por hybrid_validator.py y produce una tabla de
auditoría en Markdown. No modifica ni recalcula ningún resultado: solo lee y
reporta.
"""
from pathlib import Path
import json
import math
import re

ROOT = Path(__file__).resolve().parents[2]
CASES_ROOT = ROOT / 'TesisDesarrollo' / '02_Modelado_Simulacion'
OUTPUT = CASES_ROOT / 'Auditoria_Simulaciones.md'


def read_metrics(case_dir: Path):
    p = case_dir / 'metrics.json'
    if not p.exists():
        return None
    return json.loads(p.read_text())


def compute_metrics(metrics_obj):
    """Extrae métricas de la fase preferida (real > synthetic)."""
    if not metrics_obj:
        return None
    ph = metrics_obj.get('phases', {}).get('real') or metrics_obj.get('phases', {}).get('synthetic')
    if not ph:
        return None

    # EDI: leer directamente de edi.value (calculado por hybrid_validator)
    edi_obj = ph.get('edi', {})
    edi = edi_obj.get('value')
    edi_pval = edi_obj.get('permutation_pvalue')
    edi_sig = edi_obj.get('permutation_significant', False)

    # Symploké: usar campo 'cr' directo (es abs(internal/external))
    symploke = ph.get('symploke', {})
    cr = symploke.get('cr')  # campo canónico calculado por hybrid_validator
    if cr is None:
        # Fallback: calcular desde internal/external (legacy)
        internal = symploke.get('internal')
        external = symploke.get('external')
        if internal is not None and external not in (None, 0):
            cr = abs(internal / external)
    cr_valid = symploke.get('cr_valid')

    # Campos v2.0
    c1_detail = ph.get('c1_detail', {})
    taxonomy = ph.get('emergence_taxonomy', {})
    noise = ph.get('noise_sensitivity', {})
    persistence = ph.get('persistence', {})

    return {
        'edi': edi,
        'edi_pval': edi_pval,
        'edi_sig': edi_sig,
        'cr': cr,
        'cr_valid': cr_valid,
        'overall_pass': ph.get('overall_pass'),
        'c1': ph.get('c1_convergence'),
        'c1_relative': c1_detail.get('c1_relative'),
        'c1_absolute': c1_detail.get('c1_absolute'),
        'category': taxonomy.get('category', '?'),
        'noise_stable': noise.get('stable'),
        'noise_cv': noise.get('cv'),
        'persistence_pass': persistence.get('pass'),
        'persistence_ratio': persistence.get('std_ratio'),
    }


def fmt(x):
    """Formatea un número; maneja None, inf y nan."""
    if x is None:
        return 'n/a'
    if isinstance(x, float):
        if math.isinf(x):
            return '∞'
        if math.isnan(x):
            return 'NaN'
    return f"{x:.3f}"


def report_has_results(report_path: Path):
    if not report_path.exists():
        return False
    text = report_path.read_text(encoding='utf-8', errors='ignore')
    return bool(re.search(r"resultado|result|metric|edi|cr", text, re.IGNORECASE))


def audit_case(case_dir: Path):
    issues = []
    metrics_obj = read_metrics(case_dir)
    m = compute_metrics(metrics_obj)

    # Completitud de archivos básicos
    if not (case_dir / 'README.md').exists():
        issues.append('README.md faltante')
    if not (case_dir / 'report.md').exists():
        issues.append('report.md faltante')
    elif not report_has_results(case_dir / 'report.md'):
        issues.append('report.md sin resultados')

    # Docs opcionales (solo reportar si la carpeta docs/ existe pero incompleta)
    docs = case_dir / 'docs'
    if docs.exists():
        required_docs = [
            'arquitectura.md', 'protocolo_simulacion.md',
            'indicadores_metricas.md', 'reproducibilidad.md',
            'validacion_c1_c5.md',
        ]
        missing_docs = [d for d in required_docs if not (docs / d).exists()]
        if missing_docs:
            issues.append(f'docs/ incompleto ({len(missing_docs)} faltantes)')

    # Cordura de métricas
    if m is None:
        issues.append('metrics.json faltante o ilegible')
    else:
        if m['edi'] is None:
            issues.append('EDI no disponible')
        if m['cr'] is not None:
            if math.isinf(m['cr']):
                issues.append('CR=∞ (ext≈0)')
            elif m['cr'] < 0:
                issues.append('CR<0 (anomalía)')
        else:
            issues.append('CR no disponible')
        if m['edi'] is not None and (m['edi'] < -5 or m['edi'] > 5):
            issues.append('EDI fuera de rango')
        if m['overall_pass'] is None:
            issues.append('overall_pass no registrado')

    return m, issues


def main():
    lines = []
    lines.append('# Auditoría de Simulaciones')
    lines.append('')
    lines.append('Criterios: consistencia documental, presencia de métricas y señales de posibles anomalías sin forzar resultados.')
    lines.append('')

    rows = []
    # Contadores para resumen
    n_total = 0
    n_pass = 0
    n_sig = 0
    n_ns = 0
    n_per = 0
    cats = {}

    for case_dir in sorted(CASES_ROOT.glob('*_caso_*')):
        m, issues = audit_case(case_dir)
        case = case_dir.name
        rows.append((case, m, issues))

        # Acumular conteos
        if m:
            n_total += 1
            if m.get('overall_pass'):
                n_pass += 1
            if m.get('edi_sig'):
                n_sig += 1
            if m.get('noise_stable'):
                n_ns += 1
            if m.get('persistence_pass'):
                n_per += 1
            cat = m.get('category', '?')
            cats[cat] = cats.get(cat, 0) + 1

    # Tabla principal
    lines.append('| Caso | EDI | p-perm | sig | CR | C1 | Categoría | NS | Per | Pass | Hallazgos |')
    lines.append('| :--- | ---: | ---: | :---: | ---: | :---: | :--- | :---: | :---: | :---: | :--- |')
    for case, m, issues in rows:
        if m:
            edi = fmt(m['edi'])
            pval = fmt(m.get('edi_pval'))
            sig = '✅' if m.get('edi_sig') else '❌'
            cr = fmt(m['cr'])
            c1 = '✅' if m.get('c1') else '❌'
            cat = m.get('category', '?')
            ns = '✅' if m.get('noise_stable') else '❌'
            per = '✅' if m.get('persistence_pass') else '❌'
            state = '✅' if m.get('overall_pass') else '❌'
        else:
            edi = pval = cr = 'n/a'
            sig = c1 = ns = per = state = 'n/a'
            cat = 'n/a'
        hall = '; '.join(issues) if issues else 'OK'
        lines.append(f'| {case} | {edi} | {pval} | {sig} | {cr} | {c1} | {cat} | {ns} | {per} | {state} | {hall} |')

    # Resumen
    lines.append('')
    lines.append('## Resumen')
    lines.append('')
    lines.append(f'| Métrica | Valor |')
    lines.append(f'| :--- | :--- |')
    lines.append(f'| Total de casos | {n_total} |')
    lines.append(f'| overall_pass (EDI∈[0.30,0.90]) | {n_pass}/{n_total} |')
    lines.append(f'| Significancia (p<0.05 + EDI>0.01) | {n_sig}/{n_total} |')
    lines.append(f'| Estabilidad numérica | {n_ns}/{n_total} |')
    lines.append(f'| Persistencia (std_ratio<5) | {n_per}/{n_total} |')
    lines.append('')
    lines.append('### Distribución por categoría')
    lines.append('')
    lines.append('| Categoría | Casos |')
    lines.append('| :--- | ---: |')
    for cat in ['strong', 'weak', 'suggestive', 'trend', 'null', 'falsification']:
        if cat in cats:
            lines.append(f'| {cat} | {cats[cat]} |')
    for cat in sorted(cats):
        if cat not in ['strong', 'weak', 'suggestive', 'trend', 'null', 'falsification']:
            lines.append(f'| {cat} | {cats[cat]} |')

    lines.append('')
    lines.append('## Recomendaciones')
    lines.append('')
    lines.append('- Si EDI o CR es n/a, revisar el pipeline de cálculo y los datos fuente.')
    lines.append('- CR=∞ indica acoplamiento externo nulo: la macro no recibe señal del entorno.')
    lines.append('- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.')

    OUTPUT.write_text('\n'.join(lines).strip() + '\n', encoding='utf-8')
    print(f"Auditoría escrita en {OUTPUT}")
    print(f"  overall_pass: {n_pass}/{n_total}")
    print(f"  significancia: {n_sig}/{n_total}")
    print(f"  estabilidad: {n_ns}/{n_total}")
    print(f"  persistencia: {n_per}/{n_total}")


if __name__ == '__main__':
    main()

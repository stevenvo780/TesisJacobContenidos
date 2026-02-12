#!/usr/bin/env python3
"""
tesis.py — CLI para operativizar la tesis "Irrealismo Operativo de Hiperobjetos"

Subcomandos:
    scaffold   Genera estructura completa de un caso nuevo desde plantillas
    build      Ensambla TesisFinal/Tesis.md desde secciones de TesisDesarrollo
    sync       Sincroniza metrics.json → bloques AUTO en docs (sin tocar prosa)
    audit      Verifica consistencia estructural y numérica de todos los casos
    validate   Ejecuta simulaciones y actualiza métricas

Uso:
    python3 scripts/tesis.py scaffold --id 19 --name biodiversidad --title "Biodiversidad"
    python3 scripts/tesis.py build
    python3 scripts/tesis.py sync
    python3 scripts/tesis.py audit
    python3 scripts/tesis.py validate --case caso_clima
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─── Rutas ────────────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPTS_DIR / "templates" / "caso"
MANIFEST_PATH = SCRIPTS_DIR / "tesis_manifest.json"

TESIS_DEV = ROOT / "TesisDesarrollo"
TESIS_FINAL = ROOT / "TesisFinal"
CASES_DIR = TESIS_DEV / "02_Modelado_Simulacion"
REPOS_SIM = ROOT / "repos" / "Simulaciones"


# ─── Motor de plantillas ─────────────────────────────────────────────────────

def render(template_str, ctx):
    """Reemplaza {{key}} con ctx[key]. Deja intactos los no encontrados."""
    def _repl(m):
        key = m.group(1).strip()
        return str(ctx.get(key, m.group(0)))
    return re.sub(r'\{\{(\w+)\}\}', _repl, template_str)


def render_file(path, ctx):
    return render(path.read_text(encoding="utf-8"), ctx)


# ─── Utilidades ───────────────────────────────────────────────────────────────

def git_info():
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(ROOT), text=True, stderr=subprocess.DEVNULL
        ).strip()
        dirty = bool(subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=str(ROOT), text=True, stderr=subprocess.DEVNULL
        ).strip())
        return {"commit": commit, "dirty": dirty}
    except Exception:
        return {"commit": "unknown", "dirty": True}


def load_manifest():
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def find_cases():
    """Descubre directorios XX_caso_* en TesisDesarrollo/02_Modelado_Simulacion."""
    if not CASES_DIR.exists():
        return []
    return sorted(
        d for d in CASES_DIR.iterdir()
        if d.is_dir() and re.match(r'\d{2}_caso_', d.name)
    )


def case_slug(case_dir):
    """Extrae el slug (sin número) de un directorio de caso."""
    m = re.match(r'\d{2}_(caso_\w+)', case_dir.name)
    return m.group(1) if m else case_dir.name


def load_metrics(case_dir):
    """Busca metrics.json en TesisDesarrollo y repos."""
    candidates = [
        case_dir / "metrics.json",
        REPOS_SIM / case_slug(case_dir) / "outputs" / "metrics.json",
        REPOS_SIM / case_slug(case_dir) / "metrics.json",
    ]
    for mf in candidates:
        if mf.exists():
            return json.loads(mf.read_text(encoding="utf-8"))
    return None


def compute_edi(errors):
    """Calcula EDI desde errores de un phase."""
    rmse_abm = errors.get("rmse_abm", 0)
    rmse_reduced = errors.get("rmse_reduced", 0)
    if rmse_reduced > 0:
        return (rmse_reduced - rmse_abm) / rmse_reduced
    return 0.0


def compute_cr(symploke):
    """Calcula CR desde symploké de un phase."""
    internal = symploke.get("internal", 0)
    external = symploke.get("external", 0)
    if external > 0:
        return internal / external
    return 0.0


# ─── SCAFFOLD ─────────────────────────────────────────────────────────────────

def cmd_scaffold(args):
    """Genera estructura completa de un caso nuevo desde plantillas."""
    case_id = f"{int(args.id):02d}"
    case_name = args.name.lower().replace(" ", "_").replace("-", "_")
    dir_name = f"{case_id}_caso_{case_name}"
    target = CASES_DIR / dir_name

    if target.exists():
        print(f"[ERROR] Ya existe: {target.relative_to(ROOT)}")
        return 1

    title = args.title or case_name.replace("_", " ").title()
    ctx = {
        "case_id": case_id,
        "case_name": case_name,
        "case_title": title,
        "domain": args.domain or "general",
        "description": args.description or
            f"Validación del hiperobjeto «{title}» mediante modelo híbrido ABM+ODE.",
        "hypothesis": args.hypothesis or
            f"El sistema «{title}» presenta emergencia causal (EDI > 0.30) "
            f"que justifica su tratamiento como hiperobjeto.",
        "observable": args.observable or "Variable macro del dominio (por definir)",
        "data_source": args.data_source or "Fuente de datos por definir",
        "macro_description": args.macro_desc or
            "Balance agregado: dX/dt = α(F - βX) + ruido + asimilación",
        "micro_description": args.micro_desc or
            "Agentes en retícula N×N con difusión espacial y acoplamiento macro",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "git_commit": git_info()["commit"],
    }

    # Crear directorios
    (target / "docs").mkdir(parents=True)

    # Renderizar cada plantilla
    files_created = []
    for tpl_path in TEMPLATES_DIR.rglob("*"):
        if not tpl_path.is_file():
            continue
        rel = tpl_path.relative_to(TEMPLATES_DIR)
        out_path = target / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        content = render_file(tpl_path, ctx)
        out_path.write_text(content, encoding="utf-8")
        files_created.append(str(rel))

    print(f"[OK] Caso creado: {target.relative_to(ROOT)}")
    for f in sorted(files_created):
        print(f"   - {f}")
    print(f"\n   Siguiente paso: editar README.md y docs/ con contenido del dominio «{ctx['domain']}»")
    return 0


# ─── BUILD ────────────────────────────────────────────────────────────────────

def cmd_build(args):
    """Ensambla TesisFinal/Tesis.md desde secciones + tabla de casos automática."""
    manifest = load_manifest()
    meta = manifest.get("metadata", {})
    sections = manifest.get("thesis_sections", [])

    parts = []
    toc_entries = []

    # Header
    parts.append(
        f"# {meta.get('title', 'Tesis')}\n"
        f"**{meta.get('subtitle', '')}**  \n"
        f"**Autor:** {meta.get('author', '')}  \n"
        f"**Fecha:** {meta.get('date', '')}  \n"
        f"\n> Documento ensamblado automáticamente por `tesis.py build` "
        f"el {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  \n"
        f"> Fuente de verdad: `TesisDesarrollo/`\n"
    )

    # Ensamblar secciones
    loaded = 0
    case_table = _build_case_summary_table()
    case_table_injected = False
    
    for sec in sections:
        source = ROOT / sec["source"]
        if not source.exists():
            if sec.get("optional"):
                continue
            print(f"[WARN] No encontrada: {source.relative_to(ROOT)}")
            continue

        content = source.read_text(encoding="utf-8").strip()
        
        # Inyectar tabla de casos si hay placeholder
        if "<!-- AUTO:MATRIZ_DETALLADA -->" in content and case_table:
            content = content.replace("<!-- AUTO:MATRIZ_DETALLADA -->", case_table)
            case_table_injected = True
        
        loaded += 1

        # Extraer título para TOC
        h_match = re.search(r'^#{1,2}\s+(.+)$', content, re.MULTILINE)
        title = h_match.group(1) if h_match else sec.get("title", f"Sección {loaded}")
        anchor = re.sub(r'[^\w\s-]', '', title.lower()).strip().replace(' ', '-')
        anchor = re.sub(r'-+', '-', anchor)
        toc_entries.append(f"{loaded}. [{title}](#{anchor})")

        parts.append(content)

    # Generar tabla resumen de casos al final SOLO si no fue inyectada antes
    if case_table and not case_table_injected:
        parts.append(case_table)

    # Componer documento final (temporal para extraer headers)
    separator = "\n\n---\n\n"
    temp_content = parts[0] + "\n\n" + separator.join(parts[1:])
    
    # Generar nueva TOC detallada
    toc_lines = ["## Tabla de Contenidos\n"]
    headers = []
    lines = temp_content.splitlines()
    thesis_title = meta.get('title', 'Tesis')
    
    for i, line in enumerate(lines):
        if line.startswith("#"):
            # Ignorar el título principal exacto si está al inicio
            if i == 0 and thesis_title in line:
                continue
            # Ignorar la propia tabla de contenidos si ya existe o se detecta
            if "Tabla de Contenidos" in line:
                continue
            headers.append(line)

    for header in headers:
        level = 0
        while level < len(header) and header[level] == '#':
            level += 1
        if level > 4: continue # Limitar profundidad
        
        title = header.lstrip('#').strip()
        # Generar anchor
        anchor = title.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor).strip().replace(' ', '-')
        anchor = re.sub(r'-+', '-', anchor)
        
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    
    toc = "\n".join(toc_lines) + "\n"
    final = parts[0] + "\n\n" + toc + separator + separator.join(parts[1:])

    # Escribir
    TESIS_FINAL.mkdir(exist_ok=True)
    output = TESIS_FINAL / "Tesis.md"
    output.write_text(final, encoding="utf-8")

    line_count = final.count("\n") + 1
    print(f"[OK] Tesis ensamblada: {output.relative_to(ROOT)}")
    print(f"   Secciones: {loaded} | Líneas: {line_count}")
    print(f"   Índice detallado generado.")
    return 0




# Mapeo categoría → nivel de cierre operativo (Irrealismo Operativo)
NIVEL_MAP = {
    'strong': 4, 'weak': 3, 'suggestive': 2, 'trend': 1, 'null': 0,
    'falsification': None,  # Control — no se clasifica
}



def _build_case_summary_table():
    """Genera Matriz de Protocolo Completa (32 × 11 criterios) desde metrics.json."""
    cases = find_cases()
    if not cases:
        return ""

    rows_validated = []
    rows_rejected_high = []
    rows_rejected_low = []
    rows_falsacion = []

    def yn(v):
        return "Si" if v else "No"

    def _get_bool(phase, key_dict, key_bool):
        """Extrae booleano de un campo que puede ser dict o bool."""
        val = phase.get(key_dict, {})
        if isinstance(val, dict):
            return val.get(key_bool, False)
        return bool(val)

    for case_dir in cases:
        name = case_dir.name
        metrics = load_metrics(case_dir)
        if not metrics:
            continue

        phases = metrics.get("phases", {})
        phase = phases.get("real", phases.get("synthetic", {}))
        if not phase:
            continue

        errors = phase.get("errors", {})
        edi_d = phase.get("edi", {})
        if isinstance(edi_d, dict):
            edi = edi_d.get("value", compute_edi(errors))
        else:
            edi = edi_d if edi_d else compute_edi(errors)

        c1 = phase.get("c1_convergence", False)
        c2 = phase.get("c2_robustness", False)
        c3 = phase.get("c3_replication", False)
        c4 = phase.get("c4_validity", False)
        c5 = phase.get("c5_uncertainty", False)
        sym = _get_bool(phase, "symploke", "pass")
        nl = _get_bool(phase, "non_locality", "pass")
        per = _get_bool(phase, "persistence", "pass")
        emr = _get_bool(phase, "emergence", "pass")
        cp_d = phase.get("coupling_check", {})
        cp = _get_bool(phase, "coupling_check", "coupling_ok") if isinstance(cp_d, dict) else bool(cp_d)

        overall = phase.get("overall_pass", False)
        is_falsacion = "falsacion" in name

        num = name.split("_")[0]
        pretty = " ".join(name.split("_")[2:]).title()

        if is_falsacion:
            result = "Control (Rechazado)"
            nivel_s = "—"
        elif overall:
            # Leer nivel de metrics o mapear
            etax = phase.get("emergence_taxonomy", {})
            nivel = etax.get("nivel")
            if nivel is None:
                cat = etax.get("category", "null")
                nivel = NIVEL_MAP.get(cat, 0)
            nivel_s = str(nivel)
            result = "**Validado**"
        else:
            etax = phase.get("emergence_taxonomy", {})
            nivel = etax.get("nivel")
            if nivel is None:
                cat = etax.get("category", "null")
                nivel = NIVEL_MAP.get(cat, 0)
            nivel_s = str(nivel) if nivel is not None else "0"
            result = "Rechazado"

        row = (f"| {num} | {pretty} | {edi:.3f} "
               f"| {yn(c1)} | {yn(c2)} | {yn(c3)} | {yn(c4)} | {yn(c5)} "
               f"| {yn(sym)} | {yn(nl)} | {yn(per)} | {yn(emr)} | {yn(cp)} "
               f"| {nivel_s} | {result} |")

        if is_falsacion:
            rows_falsacion.append(row)
        elif overall:
            rows_validated.append((edi, row))
        elif edi > 0.30:
            rows_rejected_high.append((edi, row))
        else:
            rows_rejected_low.append((edi, row))

    # Sort validated and rejected by EDI descending
    rows_validated.sort(key=lambda x: -x[0])
    rows_rejected_high.sort(key=lambda x: -x[0])

    # Count failure modes in rejected genuine
    failure_counts = {"C1": 0, "Emergence": 0, "Symploké": 0,
                      "Persistencia": 0, "C5": 0, "C2": 0}
    n_rejected = 0
    for case_dir in cases:
        name = case_dir.name
        if "falsacion" in name:
            continue
        metrics = load_metrics(case_dir)
        if not metrics:
            continue
        phase = metrics.get("phases", {}).get("real", {})
        if phase.get("overall_pass", False):
            continue
        n_rejected += 1
        if not phase.get("c1_convergence"): failure_counts["C1"] += 1
        if not _get_bool(phase, "emergence", "pass"): failure_counts["Emergence"] += 1
        if not _get_bool(phase, "symploke", "pass"): failure_counts["Symploké"] += 1
        if not _get_bool(phase, "persistence", "pass"): failure_counts["Persistencia"] += 1
        if not phase.get("c5_uncertainty"): failure_counts["C5"] += 1
        if not phase.get("c2_robustness"): failure_counts["C2"] += 1

    # Build output
    lines = [
        "\n# Resumen de Simulaciones",
        "",
        "> Tabla generada automáticamente desde `metrics.json` de cada caso.",
        "",
        "## Matriz de Clasificación Operativa (29 casos × 13 criterios + Nivel)",
        "",
        "Cada celda = resultado del criterio en **Fase Real** (`assimilation_strength = 0.0`). "
        "**Nivel** = grado de cierre operativo (0–4, control = —). "
        "**Validado** = 13 condiciones se cumplen simultáneamente (incluye EDI válido y EDI significativo).",
        "",
        "| # | Caso | EDI | C1 | C2 | C3 | C4 | C5 | Sym | NL | Per | Emr | Cp | Nivel | Result |",
        "| :--- | :--- | ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    # Validated first, then falsación, then rejected high EDI, then low EDI
    for _, row in rows_validated:
        lines.append(row)
    for row in rows_falsacion:
        lines.append(row)
    for _, row in rows_rejected_high:
        lines.append(row)
    for _, row in rows_rejected_low:
        lines.append(row)

    lines.append("")
    lines.append(f"**Resumen:** {len(rows_validated)} validados (Nivel 4), "
                 f"{len(rows_rejected_high)} rechazados con EDI > 0.30 (selectividad), "
                 f"{len(rows_falsacion)} controles de falsación, "
                 f"{len(rows_rejected_low)} rechazados con EDI bajo (Nivel 0–1).")
    lines.append("")

    # Failure mode table
    if n_rejected > 0:
        lines.append("## Distribución de Modos de Fallo")
        lines.append("")
        lines.append(f"En los {n_rejected} rechazados genuinos:")
        lines.append("")
        lines.append("| Criterio | Fallos | % |")
        lines.append("| :--- | :---: | :---: |")
        for k in ["C1", "Emergence", "Symploké", "Persistencia", "C5", "C2"]:
            v = failure_counts[k]
            pct = 100 * v // n_rejected if n_rejected > 0 else 0
            lines.append(f"| {k} | {v}/{n_rejected} | {pct}% |")
        lines.append("")

    return "\n".join(lines)


# ─── SYNC ─────────────────────────────────────────────────────────────────────

def cmd_sync(args):
    """Sincroniza metrics.json → bloques AUTO en docs. No toca prosa humana."""
    cases = find_cases()
    updated = 0
    synced_cases = 0

    for case_dir in cases:
        metrics = load_metrics(case_dir)
        if not metrics:
            continue

        summary = _extract_summary(metrics)
        case_updated = False

        for md_file in case_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            new_content = _replace_auto_blocks(content, summary)
            if new_content != content:
                md_file.write_text(new_content, encoding="utf-8")
                updated += 1
                case_updated = True
                print(f"  [MOD] {md_file.relative_to(ROOT)}")

        if case_updated:
            synced_cases += 1

    print(f"\n[OK] Sync: {updated} archivos en {synced_cases} casos actualizados")
    return 0


def _extract_summary(metrics):
    """Extrae resumen plano de métricas para inyectar en docs."""
    summary = {"generated_at": metrics.get("generated_at", "—")}

    for phase_name, phase in metrics.get("phases", {}).items():
        p = phase_name  # "synthetic" o "real"
        errors = phase.get("errors", {})
        corrs = phase.get("correlations", {})
        symp = phase.get("symploke", {})

        edi = compute_edi(errors)
        cr = compute_cr(symp)

        summary[f"{p}_edi"] = f"{edi:.3f}"
        summary[f"{p}_cr"] = f"{cr:.3f}"
        summary[f"{p}_rmse_abm"] = f"{errors.get('rmse_abm', 0):.4f}"
        summary[f"{p}_rmse_ode"] = f"{errors.get('rmse_ode', 0):.4f}"
        summary[f"{p}_corr_abm"] = f"{corrs.get('abm_obs', 0):.4f}"
        summary[f"{p}_corr_ode"] = f"{corrs.get('ode_obs', 0):.4f}"

        for ci, key in enumerate(["c1_convergence", "c2_robustness",
                                   "c3_replication", "c4_validity",
                                   "c5_uncertainty"], 1):
            val = phase.get(key)
            summary[f"{p}_c{ci}"] = "Si" if val else ("No" if val is False else "—")

        all_pass = all(phase.get(k) for k in [
            "c1_convergence", "c2_robustness", "c3_replication",
            "c4_validity", "c5_uncertainty"
        ])
        summary[f"{p}_status"] = "VALIDADO" if all_pass else "NO VALIDADO"

    # Top-level: preferir real
    for key in ["edi", "cr", "status"]:
        summary[key] = summary.get(f"real_{key}", summary.get(f"synthetic_{key}", "—"))

    return summary


def _replace_auto_blocks(content, summary):
    """Reemplaza bloques <!-- AUTO:RESULTS:START/END --> con datos frescos."""

    def _results_table(m):
        return (
            "<!-- AUTO:RESULTS:START -->\n"
            "| Métrica | Sintético | Real |\n"
            "|---------|-----------|------|\n"
            f"| EDI     | {summary.get('synthetic_edi', '—')} | {summary.get('real_edi', '—')} |\n"
            f"| CR      | {summary.get('synthetic_cr', '—')} | {summary.get('real_cr', '—')} |\n"
            f"| RMSE ABM| {summary.get('synthetic_rmse_abm', '—')} | {summary.get('real_rmse_abm', '—')} |\n"
            f"| RMSE ODE| {summary.get('synthetic_rmse_ode', '—')} | {summary.get('real_rmse_ode', '—')} |\n"
            f"| Corr ABM| {summary.get('synthetic_corr_abm', '—')} | {summary.get('real_corr_abm', '—')} |\n"
            f"| Corr ODE| {summary.get('synthetic_corr_ode', '—')} | {summary.get('real_corr_ode', '—')} |\n"
            f"| C1      | {summary.get('synthetic_c1', '—')} | {summary.get('real_c1', '—')} |\n"
            f"| C2      | {summary.get('synthetic_c2', '—')} | {summary.get('real_c2', '—')} |\n"
            f"| C3      | {summary.get('synthetic_c3', '—')} | {summary.get('real_c3', '—')} |\n"
            f"| C4      | {summary.get('synthetic_c4', '—')} | {summary.get('real_c4', '—')} |\n"
            f"| C5      | {summary.get('synthetic_c5', '—')} | {summary.get('real_c5', '—')} |\n"
            f"| Estado  | {summary.get('synthetic_status', '—')} | {summary.get('real_status', '—')} |\n"
            "<!-- AUTO:RESULTS:END -->"
        )

    content = re.sub(
        r'<!-- AUTO:RESULTS:START -->.*?<!-- AUTO:RESULTS:END -->',
        _results_table,
        content,
        flags=re.DOTALL
    )

    # Valores inline: <!-- AUTO:key -->valor<!-- /AUTO:key -->
    def _inline_val(m):
        key = m.group(1)
        return f"<!-- AUTO:{key} -->{summary.get(key, m.group(2))}<!-- /AUTO:{key} -->"

    content = re.sub(
        r'<!-- AUTO:(\w+) -->(.+?)<!-- /AUTO:\1 -->',
        _inline_val,
        content
    )

    return content


# ─── AUDIT ────────────────────────────────────────────────────────────────────

def cmd_audit(args):
    """Verifica consistencia estructural y numérica de todos los casos."""
    manifest = load_manifest()
    required_docs = manifest.get("required_docs", [])
    thresholds = manifest.get("validation_thresholds", {})
    cases = find_cases()
    issues = []
    stats = {"total": len(cases), "ok": 0, "warn": 0}

    print(f"🔍 Auditando {len(cases)} casos...\n")

    for case_dir in cases:
        name = case_dir.name
        case_issues = []

        # Estructura de archivos
        for required in ["README.md", "report.md", "metrics.json"]:
            if not (case_dir / required).exists():
                case_issues.append(f"Falta {required}")

        docs_dir = case_dir / "docs"
        if docs_dir.exists():
            for doc in required_docs:
                if not (docs_dir / doc).exists():
                    case_issues.append(f"Falta docs/{doc}")
        else:
            case_issues.append("Falta directorio docs/")

        # Verificar marcadores AUTO en README.md (para sync)
        readme = case_dir / "README.md"
        if readme.exists():
            text = readme.read_text(encoding="utf-8")
            if "<!-- AUTO:RESULTS:START -->" not in text:
                case_issues.append("README.md sin marcadores AUTO (sync no funcionará)")

        # Métricas numéricas
        metrics = load_metrics(case_dir)
        if metrics:
            for p_name, phase in metrics.get("phases", {}).items():
                errors = phase.get("errors", {})
                edi = compute_edi(errors)
                rmse_abm = errors.get("rmse_abm", 0)

                if edi > thresholds.get("edi_max", 0.90):
                    case_issues.append(
                        f"{p_name}: EDI={edi:.3f} > {thresholds['edi_max']} (posible tautología)")
                if 0 < rmse_abm < thresholds.get("rmse_floor", 1e-10):
                    case_issues.append(
                        f"{p_name}: RMSE={rmse_abm:.2e} < umbral (posible sobreajuste)")

            # Consistencia timestamps
            report_path = case_dir / "report.md"
            if report_path.exists():
                report_text = report_path.read_text(encoding="utf-8")
                gen_at = metrics.get("generated_at", "")
                if gen_at and gen_at not in report_text:
                    case_issues.append("report.md desincronizado (timestamp ≠ metrics.json)")

        # Resultado
        if case_issues:
            stats["warn"] += 1
            print(f"  [WARN] {name}")
            for iss in case_issues:
                print(f"     └─ {iss}")
                issues.append((name, iss))
        else:
            stats["ok"] += 1
            print(f"  [OK] {name}")

    # Resumen
    print(f"\n{'═' * 60}")
    print(f"Casos: {stats['total']} | OK: {stats['ok']} | Con problemas: {stats['warn']}")
    print(f"Total de problemas: {len(issues)}")

    if args.output:
        _write_audit_report(cases, issues, stats, args.output)

    return 0 if not issues else 1


def _write_audit_report(cases, issues, stats, output_path):
    lines = [
        "# Auditoría de Simulaciones",
        f"\n**Fecha:** {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"**Casos auditados:** {stats['total']}",
        f"**OK:** {stats['ok']} | **Con problemas:** {stats['warn']}",
        f"**Total de problemas:** {len(issues)}",
        "",
    ]
    if issues:
        lines += [
            "| Caso | Problema |",
            "|------|----------|",
        ]
        for name, iss in issues:
            lines.append(f"| {name} | {iss} |")
    else:
        lines.append("Sin problemas detectados.")

    Path(output_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n📄 Reporte: {output_path}")


# ─── VALIDATE ─────────────────────────────────────────────────────────────────

def cmd_validate(args):
    """Ejecuta simulaciones y opcionalmente sincroniza métricas."""
    targets = []

    if args.case:
        vpy = REPOS_SIM / args.case / "src" / "validate.py"
        if not vpy.exists():
            print(f"[ERROR] No encontrado: {vpy.relative_to(ROOT)}")
            return 1
        targets.append((args.case, vpy))
    else:
        for d in sorted(REPOS_SIM.iterdir()):
            if d.is_dir():
                vpy = d / "src" / "validate.py"
                if vpy.exists():
                    targets.append((d.name, vpy))

    if not targets:
        print("[WARN] No se encontraron casos con código ejecutable")
        return 1

    print(f">> Ejecutando {len(targets)} validación(es)...\n")

    results = {}
    for name, vpy in targets:
        print(f"  ▶ {name}...", end=" ", flush=True)
        try:
            result = subprocess.run(
                [sys.executable, str(vpy)],
                capture_output=True, text=True, timeout=300
            )
            ok = result.returncode == 0
            results[name] = ok
            print("[OK]" if ok else "[FAIL]")
            if not ok and result.stderr:
                for line in result.stderr.strip().split("\n")[:5]:
                    print(f"     {line}")
        except subprocess.TimeoutExpired:
            results[name] = False
            print("[TIMEOUT] Timeout")

    passed = sum(1 for v in results.values() if v)
    print(f"\n{'═' * 60}")
    print(f"Resultados: {passed}/{len(results)} exitosos")

    if not args.no_sync and passed > 0:
        print("\n>> Sincronizando métricas → docs...")
        cmd_sync(argparse.Namespace())

    return 0 if all(results.values()) else 1


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="tesis",
        description="CLI para operativizar la tesis «Irrealismo Operativo de Hiperobjetos»",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            "  python3 scripts/tesis.py scaffold --id 19 --name biodiversidad\n"
            "  python3 scripts/tesis.py build\n"
            "  python3 scripts/tesis.py sync\n"
            "  python3 scripts/tesis.py audit --output auditoria.md\n"
            "  python3 scripts/tesis.py validate --case caso_clima\n"
        )
    )
    sub = parser.add_subparsers(dest="command")

    # scaffold
    p = sub.add_parser("scaffold", help="Genera estructura de un caso nuevo")
    p.add_argument("--id", required=True, help="Número del caso (ej: 19)")
    p.add_argument("--name", required=True, help="Slug del caso (ej: biodiversidad)")
    p.add_argument("--title", help="Título legible (ej: Biodiversidad)")
    p.add_argument("--domain", help="Dominio (ej: ecología)")
    p.add_argument("--description", help="Descripción del caso")
    p.add_argument("--hypothesis", help="Hipótesis específica")
    p.add_argument("--observable", help="Variable observable")
    p.add_argument("--data-source", dest="data_source", help="Fuente de datos")
    p.add_argument("--macro-desc", dest="macro_desc", help="Modelo macro")
    p.add_argument("--micro-desc", dest="micro_desc", help="Modelo micro")

    # build
    sub.add_parser("build", help="Ensambla TesisFinal/Tesis.md")

    # sync
    sub.add_parser("sync", help="Sincroniza metrics.json → docs")

    # audit
    p = sub.add_parser("audit", help="Audita consistencia de todos los casos")
    p.add_argument("--output", "-o", help="Ruta del reporte de auditoría (.md)")

    # validate
    p = sub.add_parser("validate", help="Ejecuta simulaciones")
    p.add_argument("--case", help="Caso específico (ej: caso_clima)")
    p.add_argument("--no-sync", action="store_true", help="No sincronizar tras validar")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "scaffold": cmd_scaffold,
        "build": cmd_build,
        "sync": cmd_sync,
        "audit": cmd_audit,
        "validate": cmd_validate,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())

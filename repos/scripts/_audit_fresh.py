#!/usr/bin/env python3
"""Auditoría fresca de todos los metrics.json generados."""
import os, json

base = os.path.join(os.path.dirname(__file__), '..', 'Simulaciones')
cases = sorted([d for d in os.listdir(base) if '_caso_' in d and os.path.isdir(os.path.join(base, d))])

sig_cases = []
ns_fail = []
per_fail = []
op_pass = []
cats = {}
bcs = {}
niveles = {}  # Conteo por nivel de cierre operativo

# Mapeo categoría → nivel de cierre operativo
NIVEL_MAP = {
    'strong': 4, 'weak': 3, 'suggestive': 2, 'trend': 1, 'null': 0,
    'falsification': None,
}

header = "{:<4} {:<35} {:>8} {:>10} {:>5} {:>5} {:>5} {:>5} {:<25} {:>3} {:<12}".format(
    '#', 'Caso', 'EDI', 'perm_p', 'sig', 'ns', 'per', 'op', 'category', 'nv', 'bc')
print(header)
print('-' * len(header))

for c in cases:
    mpath = os.path.join(base, c, 'outputs', 'metrics.json')
    if not os.path.exists(mpath):
        print(f"{c}: NO METRICS")
        continue
    with open(mpath) as f:
        m = json.load(f)
    ph = m.get('phases', {}).get('real') or m.get('phases', {}).get('synthetic', {})
    if not ph:
        print(f"{c}: NO PHASE DATA")
        continue

    edi = ph.get('edi', {})
    edi_val = edi.get('value', None)
    pval = edi.get('permutation_pvalue', None)
    sig = edi.get('permutation_significant', False)
    ns = ph.get('noise_sensitivity', {}).get('stable', None)
    per_obj = ph.get('persistence', {})
    per = per_obj.get('pass', None)
    per_ratio = per_obj.get('std_ratio', None)
    op = ph.get('overall_pass', False)
    cat = ph.get('emergence_taxonomy', {}).get('category', '?')
    bc = ph.get('bias_correction', {}).get('mode', '?')

    num = c.split('_')[0]
    edi_s = "{:.4f}".format(edi_val) if isinstance(edi_val, (int, float)) else 'N/A'
    p_s = "{:.4f}".format(pval) if isinstance(pval, (int, float)) else 'MISSING'

    # Nivel de cierre operativo
    tax = ph.get('emergence_taxonomy', {})
    nivel = tax.get('nivel')
    if nivel is None:
        nivel = NIVEL_MAP.get(cat)
    nv_s = str(nivel) if nivel is not None else '—'

    line = "{:<4} {:<35} {:>8} {:>10} {:>5} {:>5} {:>5} {:>5} {:<25} {:>3} {:<12}".format(
        num, c[3:38], edi_s, p_s, str(sig), str(ns), str(per), str(op), cat, nv_s, bc)
    print(line)

    if sig:
        sig_cases.append(num)
    if ns == False:
        ns_fail.append(num)
    if per == False:
        per_fail.append("{} (ratio={:.2f})".format(num, per_ratio) if per_ratio else num)
    if op:
        op_pass.append(num)
    cats[cat] = cats.get(cat, 0) + 1
    bcs[bc] = bcs.get(bc, 0) + 1
    if nivel is not None:
        niveles[nivel] = niveles.get(nivel, 0) + 1

print()
print("=" * 60)
print("RESUMEN")
print("=" * 60)
print(f"  overall_pass : {len(op_pass)}/29 → {op_pass}")
print(f"  sig (perm)   : {len(sig_cases)}/29 → {sig_cases}")
print(f"  ns stable    : {29 - len(ns_fail)}/29 (fail: {ns_fail})")
print(f"  per pass     : {29 - len(per_fail)}/29 (fail: {per_fail})")
print(f"  Categories   : {dict(sorted(cats.items()))}")
print(f"  Niveles      : {dict(sorted(niveles.items()))}")
print(f"  BC modes     : {dict(sorted(bcs.items()))}")

# Check for missing fields
print()
print("CAMPO FALTANTE CHECK:")
missing_fields = {}
for c in cases:
    mpath = os.path.join(base, c, 'outputs', 'metrics.json')
    if not os.path.exists(mpath):
        continue
    with open(mpath) as f:
        m = json.load(f)
    ph = m.get('phases', {}).get('real') or m.get('phases', {}).get('synthetic', {})
    num = c.split('_')[0]
    
    required = ['edi', 'bias_correction', 'emergence_taxonomy', 'persistence',
                'noise_sensitivity', 'symploke', 'non_locality', 'overall_pass']
    for field in required:
        if field not in ph:
            if field not in missing_fields:
                missing_fields[field] = []
            missing_fields[field].append(num)
    
    # Check edi sub-fields
    edi = ph.get('edi', {})
    edi_required = ['value', 'permutation_pvalue', 'permutation_significant', 'ci_lo', 'ci_hi']
    for sf in edi_required:
        if sf not in edi:
            key = f"edi.{sf}"
            if key not in missing_fields:
                missing_fields[key] = []
            missing_fields[key].append(num)

if missing_fields:
    for field, nums in sorted(missing_fields.items()):
        print(f"  MISSING {field}: cases {nums}")
else:
    print("  ✅ Todos los campos requeridos presentes en 29/29 casos")

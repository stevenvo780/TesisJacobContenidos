import json, glob, os
from datetime import datetime

cases = sorted(glob.glob('/workspace/Simulaciones/[0-9][0-9]_caso_*/'))
for c in cases:
    name = os.path.basename(c.rstrip('/'))
    cfg_path = os.path.join(c, 'case_config.json')
    met_path = os.path.join(c, 'outputs', 'metrics.json')
    cfg = json.load(open(cfg_path)) if os.path.exists(cfg_path) else {}
    met = json.load(open(met_path)) if os.path.exists(met_path) else {}
    ph = met.get('phases', {})
    real = ph.get('real', ph.get('falsification', {}))
    synth = ph.get('synthetic', {})
    edi_d = real.get('edi', {})
    edi_v = edi_d.get('value', 'N/A') if isinstance(edi_d, dict) else edi_d
    p_v = edi_d.get('permutation_pvalue', 'N/A') if isinstance(edi_d, dict) else 'N/A'
    sig = edi_d.get('permutation_significant', False) if isinstance(edi_d, dict) else False
    overall = real.get('overall_pass', False)
    gated = real.get('gated_by_synthetic', False)
    syn_pass = synth.get('overall_pass', 'N/A')
    grid = cfg.get('grid_size', '?')
    freq = cfg.get('frequency', '?')
    syn_start = cfg.get('synthetic_start', '?')
    syn_end = cfg.get('synthetic_end', '?')
    syn_split = cfg.get('synthetic_split', '?')
    real_start = cfg.get('real_start', '?')
    real_end = cfg.get('real_end', '?')
    real_split = cfg.get('real_split', '?')
    cal = real.get('calibration', {})
    best = cal.get('best_params', {})
    mc = best.get('macro_coupling', '?')
    damp = best.get('damping', '?')
    fs = best.get('forcing_scale', '?')
    c1 = real.get('c1_edi_positive', '?')
    c2 = real.get('c2_robustness', '?')
    c3 = real.get('c3_replication', '?')
    c4 = real.get('c4_sensitivity', '?')
    c5 = real.get('c5_parsimony', '?')
    sym = real.get('symploke', {})
    sym_ok = sym.get('symploke_ok', '?') if isinstance(sym, dict) else '?'
    nl = real.get('non_locality', {})
    nl_ok = nl.get('non_local_ok', '?') if isinstance(nl, dict) else '?'
    persist = real.get('persistence', {})
    per_ok = persist.get('persist_ok', '?') if isinstance(persist, dict) else '?'
    em = real.get('emergence', {})
    em_ok = em.get('emergence_detected', '?') if isinstance(em, dict) else '?'
    coup = real.get('coupling_strength', {})
    coup_ok = coup.get('coupling_significant', '?') if isinstance(coup, dict) else '?'
    syn_c2 = synth.get('c2_robustness', '?')
    syn_c3 = synth.get('c3_replication', '?')
    syn_steps = '?'
    try:
        s = datetime.strptime(str(syn_start)[:10], '%Y-%m-%d')
        e = datetime.strptime(str(syn_end)[:10], '%Y-%m-%d')
        if 'Y' in str(freq): syn_steps = e.year - s.year
        elif 'M' in str(freq): syn_steps = (e.year - s.year)*12 + (e.month - s.month)
        elif 'D' in str(freq): syn_steps = (e-s).days
        else: syn_steps = e.year - s.year
    except: pass
    real_steps = '?'
    try:
        s = datetime.strptime(str(real_start)[:10], '%Y-%m-%d')
        e = datetime.strptime(str(real_end)[:10], '%Y-%m-%d')
        sp = datetime.strptime(str(real_split)[:10], '%Y-%m-%d')
        if 'Y' in str(freq): real_steps = e.year - s.year; val_steps = e.year - sp.year
        elif 'M' in str(freq): real_steps = (e.year-s.year)*12+(e.month-s.month); val_steps = (e.year-sp.year)*12+(e.month-sp.month)
        elif 'D' in str(freq): real_steps = (e-s).days; val_steps = (e-sp).days
        else: real_steps = e.year - s.year; val_steps = e.year - sp.year
    except: val_steps = '?'
    
    print(f"=== {name} ===")
    print(f"  grid={grid} freq={freq} synth_steps~{syn_steps} real_steps~{real_steps} val_steps~{val_steps}")
    print(f"  params: mc={mc}, damp={damp}, fs={fs}")
    edi_s = f"{edi_v:.4f}" if isinstance(edi_v, float) else str(edi_v)
    p_s = f"{p_v:.4f}" if isinstance(p_v, float) else str(p_v)
    print(f"  EDI={edi_s} p={p_s} sig={sig} pass={overall} gated={gated}")
    print(f"  synth: pass={syn_pass} c2={syn_c2} c3={syn_c3}")
    print(f"  C1={c1} C2={c2} C3={c3} C4={c4} C5={c5}")
    print(f"  sym={sym_ok} nl={nl_ok} per={per_ok} em={em_ok} coup={coup_ok}")
    
    # Failure diagnosis
    fails = []
    if not overall:
        if c1 == False: fails.append('C1')
        if c2 == False: fails.append('C2')
        if c3 == False: fails.append('C3')
        if c4 == False: fails.append('C4')
        if c5 == False: fails.append('C5')
        if sym_ok == False: fails.append('sym')
        if nl_ok == False: fails.append('nl')
        if per_ok == False: fails.append('per')
        if em_ok == False: fails.append('em')
        if coup_ok == False: fails.append('coup')
        if not sig: fails.append('NOT_SIG')
        if isinstance(edi_v, float) and edi_v < 0.10: fails.append('EDI<0.10')
        if gated: fails.append('GATED_BY_SYNTH')
    print(f"  FAILS: {fails if fails else 'NONE (PASS)'}")
    print()

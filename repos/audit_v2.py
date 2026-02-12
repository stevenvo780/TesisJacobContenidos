import json, glob, os

cases = sorted(glob.glob('/workspace/Simulaciones/[0-9][0-9]_caso_*/'))
for c in cases:
    name = os.path.basename(c.rstrip('/'))
    cfg_f = os.path.join(c, 'case_config.json')
    met_f = os.path.join(c, 'outputs', 'metrics.json')
    cfg = json.load(open(cfg_f)) if os.path.exists(cfg_f) else {}
    met = json.load(open(met_f)) if os.path.exists(met_f) else {}
    
    # Config
    dates = cfg.get('dates', {})
    exe = cfg.get('execution', {})
    grid = exe.get('grid_size', '?')
    freq = cfg.get('synthetic', {}).get('freq', '?')
    syn_s = dates.get('synthetic_start', '?')[:10]
    syn_e = dates.get('synthetic_end', '?')[:10]
    real_s = dates.get('real_start', '?')[:10]
    real_e = dates.get('real_end', '?')[:10]
    real_sp = dates.get('real_split', '?')[:10]
    ode_m = cfg.get('ode_model', '?')
    n_runs = exe.get('n_runs', '?')
    loe = cfg.get('loe', '?')
    
    # Metrics - real phase
    ph = met.get('phases', {})
    real = ph.get('real', ph.get('falsification', {}))
    synth = ph.get('synthetic', {})
    
    edi_d = real.get('edi', {})
    edi_v = edi_d.get('value', 'N/A') if isinstance(edi_d, dict) else edi_d
    p_v = edi_d.get('permutation_pvalue', 'N/A') if isinstance(edi_d, dict) else 'N/A'
    sig = edi_d.get('permutation_significant', False) if isinstance(edi_d, dict) else False
    overall = real.get('overall_pass', False)
    gated = real.get('gated_by_synthetic', False)
    
    cal = real.get('calibration', {})
    best = cal.get('best_params', {})
    mc = best.get('macro_coupling', '?')
    damp = best.get('damping', '?')
    fs = best.get('forcing_scale', '?')
    
    c1 = real.get('c1_convergence', real.get('c1_edi_positive', '?'))
    c2 = real.get('c2_robustness', '?')
    c3 = real.get('c3_replication', '?')
    c4 = real.get('c4_validity', real.get('c4_sensitivity', '?'))
    c5 = real.get('c5_uncertainty', real.get('c5_parsimony', '?'))
    
    sym_d = real.get('symploke', {})
    sym_ok = sym_d.get('symploke_ok', '?') if isinstance(sym_d, dict) else '?'
    nl_d = real.get('non_locality', {})
    nl_ok = nl_d.get('non_local_ok', '?') if isinstance(nl_d, dict) else '?'
    per_d = real.get('persistence', {})
    per_ok = per_d.get('persist_ok', '?') if isinstance(per_d, dict) else '?'
    em_d = real.get('emergence', {})
    em_ok = em_d.get('emergence_detected', '?') if isinstance(em_d, dict) else '?'
    coup_d = real.get('coupling_check', real.get('coupling_strength', {}))
    coup_ok = coup_d.get('coupling_significant', '?') if isinstance(coup_d, dict) else '?'
    
    # C2 detail
    c2_det = real.get('c2_detail', {})
    c2_rel_mean = c2_det.get('relative_mean', '?') if isinstance(c2_det, dict) else '?'
    c2_rel_var = c2_det.get('relative_var', '?') if isinstance(c2_det, dict) else '?'
    
    # Synth
    syn_pass = synth.get('overall_pass', 'N/A')
    syn_c2 = synth.get('c2_robustness', '?')
    syn_c3 = synth.get('c3_replication', '?')
    syn_gated = synth.get('gated_by_synthetic', False)
    
    # Taxonomy
    tax = real.get('emergence_taxonomy', {})
    level = tax.get('level', '?') if isinstance(tax, dict) else '?'
    label = tax.get('label', '?') if isinstance(tax, dict) else '?'
    
    # Criteria dict
    crit = real.get('criteria', {})
    rmse_fraud = crit.get('rmse_fraud', '?') if isinstance(crit, dict) else '?'
    edi_valid = crit.get('edi_valid', '?') if isinstance(crit, dict) else '?'
    
    print(f"=== {name} (ode={ode_m}, loe={loe}) ===")
    print(f"  CONFIG: grid={grid} freq={freq} n_runs={n_runs}")
    print(f"  DATES: syn={syn_s}..{syn_e} | real={real_s}..{real_e} split={real_sp}")
    print(f"  PARAMS: mc={mc:.3f}, damp={damp:.3f}, fs={fs:.3f}" if all(isinstance(x,float) for x in [mc,damp,fs]) else f"  PARAMS: mc={mc}, damp={damp}, fs={fs}")
    edi_s = f"{edi_v:.4f}" if isinstance(edi_v, float) else str(edi_v)
    p_s = f"{p_v:.4f}" if isinstance(p_v, float) else str(p_v)
    print(f"  EDI={edi_s} p={p_s} sig={sig} | Level={level} ({label})")
    print(f"  PASS={overall} gated={gated}")
    print(f"  SYNTH: pass={syn_pass} c2={syn_c2} c3={syn_c3}")
    print(f"  C1={c1} C2={c2} C3={c3} C4={c4} C5={c5}")
    c2m_s = f"{c2_rel_mean:.4f}" if isinstance(c2_rel_mean, float) else str(c2_rel_mean)
    c2v_s = f"{c2_rel_var:.4f}" if isinstance(c2_rel_var, float) else str(c2_rel_var)
    print(f"  C2_detail: rel_mean={c2m_s} rel_var={c2v_s} (need both <0.5)")
    print(f"  sym={sym_ok} nl={nl_ok} per={per_ok} em={em_ok} coup={coup_ok}")
    print(f"  rmse_fraud={rmse_fraud} edi_valid={edi_valid}")
    
    # Failure diagnosis
    fails = []
    if not overall:
        if c1 == False: fails.append('C1(EDI<=0)')
        if c2 == False: fails.append(f'C2(rm={c2m_s},rv={c2v_s})')
        if c3 == False: fails.append('C3')
        if c4 == False: fails.append('C4')
        if c5 == False: fails.append('C5')
        if sym_ok == False: fails.append('symploke')
        if nl_ok == False: fails.append('non_local')
        if per_ok == False: fails.append('persist')
        if em_ok == False: fails.append('emergence')
        if coup_ok == False: fails.append('coupling')
        if rmse_fraud == True: fails.append('RMSE_FRAUD')
        if not sig: fails.append('NOT_SIGNIFICANT')
        if isinstance(edi_v, float) and edi_v < 0.10: fails.append('EDI<0.10')
        if gated: fails.append('GATED_SYNTH')
    print(f"  --> DIAGNOSIS: {fails if fails else 'ALL PASS'}")
    print()

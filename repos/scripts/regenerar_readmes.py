#!/usr/bin/env python3
"""
Regenera los README.md de TesisDesarrollo/02_Modelado_Simulacion/{NN}_caso_*/
usando datos reales de los metrics.json de repos/Simulaciones/{NN}_caso_*/outputs/.

Corrige:
- Numeración incorrecta (casos 19-29 tenían numeración vieja)
- Rutas de pipeline incorrectas  
- Métricas fabricadas/desactualizadas
- Formato inconsistente entre casos 01-18 vs 19-29
"""
import json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SIM_BASE = os.path.join(ROOT, 'repos', 'Simulaciones')
TD_BASE = os.path.join(ROOT, 'TesisDesarrollo', '02_Modelado_Simulacion')

NIVEL_MAP = {
    'strong': 4, 'weak': 3, 'suggestive': 2, 'trend': 1, 'null': 0,
    'falsification': None,
}

# Nombres legibles para cada caso
NOMBRES = {
    '01': 'Clima Regional',
    '02': 'Conciencia',
    '03': 'Contaminación',
    '04': 'Energía',
    '05': 'Epidemiología',
    '06': 'Falsación: Exogeneidad',
    '07': 'Falsación: No Estacionariedad',
    '08': 'Falsación: Observabilidad',
    '09': 'Finanzas Globales',
    '10': 'Justicia',
    '11': 'Movilidad',
    '12': 'Paradigmas',
    '13': 'Políticas Estratégicas',
    '14': 'Postverdad',
    '15': 'Wikipedia',
    '16': 'Deforestación Global',
    '17': 'Emisiones CO₂ Océanos',
    '18': 'Urbanización Global',
    '19': 'Acidificación Oceánica',
    '20': 'Síndrome de Kessler',
    '21': 'Salinización de Suelos',
    '22': 'Ciclo del Fósforo',
    '23': 'Erosión Dialéctica del Discurso',
    '24': 'Contaminación por Microplásticos',
    '25': 'Depleción de Acuíferos',
    '26': 'Constelaciones Satelitales (Starlink)',
    '27': 'Riesgo Biológico Global',
    '28': 'Fuga de Cerebros Global',
    '29': 'Emergencia IoT',
}


def fmt_edi(v):
    """Formatea un valor EDI como string."""
    if v is None:
        return 'N/A'
    if isinstance(v, (int, float)):
        return f'{v:.3f}'
    return str(v)


def fmt_corr(v):
    if v is None:
        return 'N/A'
    return f'{v:.4f}'


def bool_icon(v):
    if v is True:
        return '✅'
    if v is False:
        return '❌'
    return '—'


def nivel_str(nivel):
    if nivel is None:
        return '—'
    labels = {0: 'null', 1: 'trend', 2: 'suggestive', 3: 'weak', 4: 'strong'}
    return f'{nivel} ({labels.get(nivel, "?")})'


def generate_readme(caso_dir, m):
    """Genera contenido del README.md a partir del metrics.json."""
    num = caso_dir.split('_')[0]
    nombre = NOMBRES.get(num, caso_dir.replace('_', ' '))
    
    synth = m.get('phases', {}).get('synthetic', {})
    real = m.get('phases', {}).get('real', {})
    generated = m.get('generated_at', 'N/A')
    
    # Fase principal (real si existe, sino sintética)
    ph = real if real else synth
    
    # EDI
    edi_obj = ph.get('edi', {})
    edi_val = edi_obj.get('value')
    edi_ci_lo = edi_obj.get('ci_lo')
    edi_ci_hi = edi_obj.get('ci_hi')
    edi_sig = edi_obj.get('permutation_significant', False)
    edi_pval = edi_obj.get('permutation_pvalue')
    
    # Correlaciones
    corrs = ph.get('correlations', {})
    corr_abm = corrs.get('abm_obs')
    corr_ode = corrs.get('ode_obs')
    
    # Errores
    errors = ph.get('errors', {})
    rmse_abm = errors.get('rmse_abm')
    rmse_reduced = errors.get('rmse_reduced')
    
    # Criterios
    criteria = ph.get('criteria', {})
    c1 = criteria.get('c1_convergence')
    c2 = criteria.get('c2_robustness')
    c3 = criteria.get('c3_replication')
    c4 = criteria.get('c4_validity')
    c5 = criteria.get('c5_uncertainty')
    symploke = criteria.get('symploke_pass')
    non_locality = criteria.get('non_locality_pass')
    persistence = criteria.get('persistence_pass')
    coupling = criteria.get('coupling_ok')
    overall = ph.get('overall_pass', False)
    
    # Taxonomía de emergencia
    tax = ph.get('emergence_taxonomy', {})
    category = tax.get('category', '?')
    nivel = tax.get('nivel')
    if nivel is None:
        nivel = NIVEL_MAP.get(category)
    interpretation = tax.get('interpretation', '')
    
    # Bias correction
    bc = ph.get('bias_correction', {})
    bc_mode = bc.get('mode', '?')
    
    # Noise sensitivity
    ns = ph.get('noise_sensitivity', {})
    ns_stable = ns.get('stable')
    ns_cv = ns.get('cv')
    
    # Symploké CR
    sym = ph.get('symploke', {})
    cr_val = sym.get('cr')
    
    # Data info
    data_info = ph.get('data', {})
    
    # Datos de fase sintética
    s_edi = synth.get('edi', {}).get('value') if synth else None
    s_overall = synth.get('overall_pass') if synth else None
    s_corrs = synth.get('correlations', {}) if synth else {}
    s_corr_abm = s_corrs.get('abm_obs')
    s_corr_ode = s_corrs.get('ode_obs')
    s_cr = synth.get('symploke', {}).get('cr') if synth else None
    
    # Estado general
    is_falsification = 'falsacion' in caso_dir
    if is_falsification:
        estado_icon = '🔬'
        estado_text = 'Control negativo (falsación)'
    elif overall:
        estado_icon = '✅'
        estado_text = 'Validado — cierre operativo confirmado'
    elif edi_sig and isinstance(edi_val, (int, float)) and edi_val > 0.01:
        estado_icon = '⚠️'
        estado_text = 'Parcial — señal significativa pero protocolo incompleto'
    else:
        estado_icon = '❌'
        estado_text = 'Sin señal — EDI insuficiente o no significativo'
    
    # Construir README
    lines = []
    lines.append(f'# Caso {nombre} (Modelo y Simulación)')
    lines.append('')
    lines.append(f'**Nivel de cierre operativo:** {nivel_str(nivel)}')
    lines.append(f'**Estado:** {estado_icon} {estado_text}')
    lines.append(f'**Generado:** {generated}')
    lines.append('')
    
    # Descripción breve
    if interpretation:
        lines.append(f'> {interpretation}')
        lines.append('')
    
    # Pipeline
    lines.append('## Ejecución')
    lines.append('')
    lines.append('```bash')
    lines.append(f'cd repos/Simulaciones/{caso_dir}/src && python3 validate.py')
    lines.append('```')
    lines.append('')
    
    # Estructura
    td_dir = os.path.join(TD_BASE, caso_dir)
    has_docs = os.path.isdir(os.path.join(td_dir, 'docs'))
    lines.append('## Estructura')
    lines.append('')
    if has_docs:
        lines.append('- `docs/arquitectura.md`: capas y supuestos del modelo híbrido.')
        lines.append('- `docs/protocolo_simulacion.md`: protocolo de simulación y criterio de paro.')
        lines.append('- `docs/indicadores_metricas.md`: indicadores, métricas y reglas de rechazo.')
        lines.append('- `docs/validacion_c1_c5.md`: validación operativa C1–C5.')
        lines.append('- `docs/reproducibilidad.md`: versionado, entorno y sensibilidad.')
    lines.append('- `metrics.json`: métricas de validación computadas.')
    lines.append('- `report.md`: reporte narrativo de resultados.')
    lines.append('')
    
    # Resultados
    lines.append('## Resultados')
    lines.append('')
    lines.append('| Métrica | Sintético | Real |')
    lines.append('|---------|-----------|------|')
    lines.append(f'| EDI     | {fmt_edi(s_edi)} | {fmt_edi(edi_val)} |')
    if edi_ci_lo is not None and edi_ci_hi is not None:
        s_ci_lo = synth.get('edi', {}).get('ci_lo') if synth else None
        s_ci_hi = synth.get('edi', {}).get('ci_hi') if synth else None
        s_ci = f'[{s_ci_lo:.3f}, {s_ci_hi:.3f}]' if s_ci_lo is not None else 'N/A'
        lines.append(f'| IC 95%  | {s_ci} | [{edi_ci_lo:.3f}, {edi_ci_hi:.3f}] |')
    lines.append(f'| Corr ABM | {fmt_corr(s_corr_abm)} | {fmt_corr(corr_abm)} |')
    lines.append(f'| Corr ODE | {fmt_corr(s_corr_ode)} | {fmt_corr(corr_ode)} |')
    if s_cr is not None or cr_val is not None:
        lines.append(f'| CR (Symploké) | {fmt_corr(s_cr)} | {fmt_corr(cr_val)} |')
    if rmse_abm is not None:
        s_rmse = synth.get('errors', {}).get('rmse_abm') if synth else None
        lines.append(f'| RMSE ABM | {fmt_edi(s_rmse)} | {fmt_edi(rmse_abm)} |')
    lines.append(f'| overall_pass | {bool_icon(s_overall)} | {bool_icon(overall)} |')
    lines.append('')
    
    # Protocolo C1-C5
    lines.append(f'**Protocolo C1-C5 (fase real):** C1={bool_icon(c1)} C2={bool_icon(c2)} C3={bool_icon(c3)} C4={bool_icon(c4)} C5={bool_icon(c5)}')
    lines.append('')
    lines.append(f'**Symploké:** {bool_icon(symploke)} | **No-localidad:** {bool_icon(non_locality)} | **Persistencia:** {bool_icon(persistence)} | **Acoplamiento:** {bool_icon(coupling)}')
    lines.append('')
    
    # Info adicional
    lines.append(f'**Significancia:** p={fmt_edi(edi_pval)}, significativo={bool_icon(edi_sig)}')
    lines.append(f'**Corrección de sesgo:** {bc_mode}')
    lines.append(f'**Sensibilidad al ruido:** estable={bool_icon(ns_stable)}{f", CV={ns_cv:.4f}" if ns_cv is not None else ""}')
    lines.append('')
    
    # Modelo híbrido
    lines.append('## Modelo Híbrido')
    lines.append('')
    lines.append('- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro')
    lines.append('- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos')
    lines.append('- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia')
    lines.append('')
    
    return '\n'.join(lines)


def main():
    cases = sorted([d for d in os.listdir(SIM_BASE)
                    if '_caso_' in d and os.path.isdir(os.path.join(SIM_BASE, d))])
    
    updated = 0
    errors = []
    
    for caso in cases:
        mpath = os.path.join(SIM_BASE, caso, 'outputs', 'metrics.json')
        if not os.path.exists(mpath):
            errors.append(f'{caso}: no metrics.json')
            continue
        
        with open(mpath) as f:
            m = json.load(f)
        
        readme_content = generate_readme(caso, m)
        
        td_dir = os.path.join(TD_BASE, caso)
        os.makedirs(td_dir, exist_ok=True)
        readme_path = os.path.join(td_dir, 'README.md')
        
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        num = caso.split('_')[0]
        ph = m.get('phases', {}).get('real', {})
        edi = ph.get('edi', {}).get('value')
        overall = ph.get('overall_pass', False)
        tax = ph.get('emergence_taxonomy', {})
        nivel = tax.get('nivel', NIVEL_MAP.get(tax.get('category', '?')))
        print(f'  {num} {caso[3:40]:37s} EDI={fmt_edi(edi):>7s}  nivel={str(nivel):>4s}  pass={bool_icon(overall)}')
        updated += 1
    
    print(f'\n✅ {updated} READMEs regenerados en TesisDesarrollo/02_Modelado_Simulacion/')
    if errors:
        print(f'❌ Errores: {errors}')


if __name__ == '__main__':
    main()

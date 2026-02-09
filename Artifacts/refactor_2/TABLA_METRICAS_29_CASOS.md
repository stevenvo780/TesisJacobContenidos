# Tabla Maestra de Métricas — 29 Casos

Actualizado: 2026-02-09 (datos de metrics.json post 7 correcciones técnicas — commit df1015b)

## Estado de Resolución de Defectos

| Defecto | Estado | Detalle |
|---------|--------|---------|
| D1: Data leakage en forcing | ✅ Resuelto | Persistence en validación, tendencia solo con train |
| D2: overall_pass vs EDI>0.90 | ✅ Resuelto | `edi_valid` incluido en conjunción `overall_pass` |
| D3: ODE genérica (28/29 iguales) | ✅ Resuelto | 11 modelos ODE domain-specific en `ode_library.py` |
| D4: ABM sin heterogeneidad | ✅ Resuelto | 3 capas: forcing_gradient + heterogeneity_strength + topología |
| D5: ABM y ODE no acoplados | ✅ Resuelto | Bidireccional 2-iter: ODE₁→ABM₁→ODE₂→ABM₂, ode_cs separado de mc, abm_feedback_gamma=0.05 |
| D6: Fases sintéticas compartidas | ⚠️ Parcial | 6/29 domain-specific, 23/29 aún genéricos (alpha=0.08, beta=0.03) |
| D7: EDI sin significancia estadística | ✅ Resuelto | Permutation test (200 perms), 7/29 significativos (p<0.05) |
| D8: mc > 0.5 (esclavización) | ✅ Resuelto | Grid [0.05, 0.45], refinement cap 0.50. 29/29 mc ≤ 0.50 |
| D9: EDI umbral mágico 0.30 | ✅ Resuelto | edi_min=0.325 (derivado de GPU null distribution 0.3248) |
| Datos sintéticos → reales | ⚠️ Parcial | 9/12 código real listo, 6 caen a fallback por APIs |
| Proxies inadecuados | ⚠️ Parcial | 2/3 corregidos (Kessler ✅, Starlink ✅, Salinización ⚠️) |
| Grid escalado | ✅ Resuelto | Run GPU 470x470 ejecutado |

## Métricas Actuales (de metrics.json — post 7 correcciones)

| # | Caso | EDI_syn | EDI_real | mc | ode_cs | perm_p | sig | CR | c1 | Pass |
|---|------|---------|----------|-----|--------|--------|-----|-----|-----|------|
| 01 | Clima Regional (CONUS) | -0.127 | -0.015 | 0.050 | 0.040 | 0.625 | no | 1.00 | F | F |
| 02 | Conciencia Colectiva | -0.038 | -0.038 | 0.072 | 0.058 | 0.910 | no | 0.94 | F | F |
| 03 | Contaminación PM2.5 | -0.000 | -0.000 | 0.050 | 0.040 | 0.460 | no | 2.78 | F | F |
| 04 | Energía (OPSD GB Grid) | 0.071 | -0.003 | 0.074 | 0.059 | 0.945 | no | 1.10 | F | F |
| 05 | Epidemiología (COVID-19 SEIR) | 0.446 | 0.000 | 0.050 | 0.040 | 1.000 | no | 0.00 | F | F |
| 06 | Falsación: Exogeneidad | — | -0.615 | 0.200 | 0.160 | 1.000 | no | 1.16 | F | F |
| 07 | Falsación: No-Estacionariedad | — | -7.837 | 0.200 | 0.160 | 1.000 | no | 1.18 | F | F |
| 08 | Falsación: Observabilidad | — | -3.771 | 0.200 | 0.160 | 1.000 | no | 1.20 | F | F |
| 09 | Finanzas (SPY) | -0.000 | 0.026 | 0.050 | 0.040 | 0.000 | **YES** | 0.00 | F | F |
| 10 | Justicia Algorítmica | -0.025 | 0.000 | 0.050 | 0.040 | 1.000 | no | 1.05 | F | F |
| 11 | Movilidad Urbana | 0.020 | 0.003 | 0.145 | 0.116 | 0.425 | no | 0.00 | F | F |
| 12 | Cambio de Paradigmas | 0.000 | 0.000 | 0.050 | 0.040 | 1.000 | no | 0.00 | F | F |
| 13 | Políticas Estratégicas | -0.003 | 0.000 | 0.050 | 0.040 | 1.000 | no | 1.62 | F | F |
| 14 | Postverdad | 0.000 | 0.002 | 0.050 | 0.040 | 0.005 | **YES** | 1.05 | F | F |
| 15 | Wikipedia Clima | 0.317 | 0.000 | 0.050 | 0.040 | 1.000 | no | 1.16 | F | F |
| 16 | Deforestación Global | -3.715 | -0.294 | 0.407 | 0.300 | 1.000 | no | 1.01 | F | F |
| 17 | Temperatura Oceánica | 0.110 | 0.067 | 0.050 | 0.040 | 0.000 | **YES** | 1.30 | F | F |
| 18 | Urbanización Global | 0.000 | -0.000 | 0.050 | 0.040 | 1.000 | no | 2.24 | F | F |
| 19 | Acidificación Oceánica | -0.141 | -0.002 | 0.172 | 0.138 | 0.000 | **YES** | 1.17 | F | F |
| 20 | Síndrome de Kessler | -3.419 | -3.419 | 0.050 | 0.040 | 1.000 | no | 1.17 | F | F |
| 21 | Salinización de Suelos | 0.505 | 0.088 | 0.416 | 0.300 | 1.000 | no | 1.05 | F | F |
| 22 | Ciclo del Fósforo | 0.386 | -3.670 | 0.500 | 0.300 | 1.000 | no | 1.01 | F | F |
| 23 | Erosión Dialéctica | 0.293 | -5.931 | 0.500 | 0.300 | 1.000 | no | 1.00 | F | F |
| 24 | Contam. Microplásticos | 0.679 | **0.439** | 0.500 | 0.300 | **0.000** | **YES** | 1.00 | F | F |
| 25 | Nivel Freático Acuíferos | 0.405 | -0.182 | 0.500 | 0.300 | 1.000 | no | 1.00 | F | F |
| 26 | Constelaciones (Starlink) | 0.564 | -545.736 | 0.107 | 0.086 | 1.000 | no | inf | F | F |
| 27 | Riesgo Biológico Global | 0.409 | 0.111 | 0.050 | 0.040 | 0.345 | no | 1.00 | F | F |
| 28 | Fuga de Cerebros Global | 0.491 | 0.182 | 0.500 | 0.300 | 0.000 | **YES** | 1.01 | T | F |
| 29 | Ecosistema IoT Global | 0.414 | 0.007 | 0.368 | 0.295 | 0.000 | **YES** | 1.06 | F | F |

## Conteos

| Métrica | Valor | Estado |
|---------|-------|--------|
| EDI_real en rango [0.325-0.90] | 1 (caso 24: 0.439) | 🚩 Solo microplásticos |
| EDI_real significativo (perm p<0.05) | 7 (casos 09, 14, 17, 19, 24, 28, 29) | ⚠️ Señal parcial |
| EDI_real válido AND significativo | 1 (caso 24) | 🚩 Insuficiente |
| EDI_syn en rango [0.325-0.90] | 6 | ⚠️ No transfiere a real |
| EDI > 0.90 (tautológico) | 0 | ✅ Eliminado |
| mc ≤ 0.50 | 29/29 | ✅ Cap aplicado |
| ode_coupling_strength presente | 29/29 | ✅ Separado de mc |
| Permutation test presente | 29/29 | ✅ 200 permutaciones |
| ABM feedback gamma > 0 | 29/29 | ✅ Bidireccional |
| overall_pass = true | 0 | ✅ Consistente con reglas |
| CR válido (>2.0) | 3 (casos 03, 18, 26) | 🚩 Baja cohesión |
| C1 convergence | 1 (caso 28) | 🚩 ABM rara vez supera ODE |
| Persistence pass | 24/29 | ✅ Mayoría pasa |
| EDI_real negativo | 14/26 genuinos | 🚩 Anti-emergencia dominante |
| Falsaciones correctas | 3/3 | ✅ Protocolo discriminante |

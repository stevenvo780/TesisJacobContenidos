# Tabla Maestra de Métricas — 29 Casos

Actualizado: 2026-02-09 (datos de metrics.json actuales)

## Estado de Resolución de Defectos

| Defecto | Estado | Detalle |
|---------|--------|---------|
| D1: Data leakage en forcing | ✅ Resuelto | Persistence en validación, tendencia solo con train |
| D2: overall_pass vs EDI>0.90 | ✅ Resuelto | `edi_valid` incluido en conjunción `overall_pass` |
| D3: ODE genérica (28/29 iguales) | ✅ Resuelto | 11 modelos ODE domain-specific en `ode_library.py` |
| D4: ABM sin heterogeneidad | ✅ Resuelto | 3 capas: forcing_gradient + heterogeneity_strength + topología |
| D5: ABM y ODE no acoplados | ⚠️ Parcial | ODE→ABM top-down ok, falta bidireccional simultáneo |
| D6: Fases sintéticas compartidas | ❌ No resuelto | 25/29 con alpha=0.08, beta=0.03 idénticos |
| Datos sintéticos → reales | ⚠️ Parcial | 9/12 código real listo, 6 caen a fallback por APIs |
| Proxies inadecuados | ⚠️ Parcial | 2/3 corregidos (Kessler ✅, Starlink ✅, Salinización ⚠️) |
| macro_coupling > 0.5 | ❌ No resuelto | 23/29 con mc>0.5, sin restricción en calibración |
| Grid escalado | ✅ Resuelto | Run GPU 470x470 ejecutado |

## Métricas Actuales (de metrics.json)

| # | Caso | EDI_syn | EDI_real | Pass_syn | Pass_real |
|---|------|---------|----------|----------|-----------|
| 01 | Clima Regional (CONUS) | -0.604 | -0.299 | false | false |
| 02 | Conciencia Colectiva | 0.112 | -0.063 | false | false |
| 03 | Contaminación PM2.5 | -0.000 | -0.000 | false | false |
| 04 | Energía (OPSD GB Grid) | 0.071 | -0.005 | false | false |
| 05 | Epidemiología (COVID-19 SEIR) | 0.446 | 0.000 | false | false |
| 06 | Falsación: Exogeneidad | — | -0.615 | — | false |
| 07 | Falsación: No-Estacionariedad | — | -7.837 | — | false |
| 08 | Falsación: Observabilidad | — | -3.771 | — | false |
| 09 | Finanzas (SPY) | -0.000 | 0.051 | false | false |
| 10 | Justicia Algorítmica | -0.025 | 0.000 | false | false |
| 11 | Movilidad Urbana | 0.020 | 0.003 | false | false |
| 12 | Cambio de Paradigmas | 0.000 | -0.000 | false | false |
| 13 | Políticas Estratégicas | -0.003 | -0.022 | false | false |
| 14 | Postverdad | 0.000 | 0.003 | false | false |
| 15 | Wikipedia Clima | 0.317 | 0.000 | false | false |
| 16 | Deforestación Global | -3.715 | -1.001 | false | false |
| 17 | Temperatura Oceánica | 0.110 | 0.119 | false | false |
| 18 | Urbanización Global | 0.000 | 0.000 | false | false |
| 19 | Acidificación Oceánica | -0.141 | -0.002 | false | false |
| 20 | Síndrome de Kessler | -3.419 | -3.419 | false | false |
| 21 | Salinización de Suelos | 0.505 | -1.378 | false | false |
| 22 | Ciclo del Fósforo | 0.386 | -4.269 | false | false |
| 23 | Erosión Dialéctica | 0.293 | -9.084 | false | false |
| 24 | Contam. Microplásticos | 0.679 | **0.586** | false | false |
| 25 | Nivel Freático Acuíferos | 0.405 | -0.272 | false | false |
| 26 | Constelaciones (Starlink) | 0.564 | -546.587 | false | false |
| 27 | Riesgo Biológico Global | 0.409 | **0.414** | false | false |
| 28 | Fuga de Cerebros Global | 0.491 | 0.213 | false | false |
| 29 | Ecosistema IoT Global | 0.414 | 0.014 | false | false |

## Conteos

| Métrica | Valor | Estado |
|---------|-------|--------|
| EDI_real en rango (0.30-0.90) | 2 (casos 24, 27) | ⚠️ Señal parcial |
| EDI_syn en rango (0.30-0.90) | 10 | ⚠️ No transfiere a real |
| EDI > 0.90 (tautológico) | 0 | ✅ Corregido |
| overall_pass = true | 0 | ✅ Consistente con reglas |
| EDI_real negativo | 18/26 genuinos | 🚩 Anti-emergencia dominante |
| Falsaciones correctas | 3/3 | ✅ Protocolo discriminante |

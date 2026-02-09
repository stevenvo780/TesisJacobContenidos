# Tabla Maestra de Métricas — 29 Casos

Actualizado: 2026-02-09 (datos de metrics.json post Bias Correction + Taxonomía Emergencia — commit 54234d6)

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
| D10: Bias ODE→ABM destruye acoplamiento | ✅ Resuelto | Bias Correction 3 modos (full/bias_only/none) con guardas de correlación y escala |
| D11: Evaluación binaria (pass/fail) | ✅ Resuelto | Taxonomía emergencia diferenciada: 6 categorías (strong/weak/suggestive/trend/null/falsification) |
| Datos sintéticos → reales | ⚠️ Parcial | 9/12 código real listo, 6 caen a fallback por APIs |
| Proxies inadecuados | ⚠️ Parcial | 2/3 corregidos (Kessler ✅, Starlink ✅, Salinización ⚠️) |
| Grid escalado | ✅ Resuelto | Run GPU 470x470 ejecutado |

## Bias Correction ODE→ABM (Nuevo en commit 54234d6)

La serie ODE, aunque bien correlacionada con observaciones, puede tener sesgo en nivel y escala que destruye el acoplamiento con el ABM. Se aplica corrección de sesgo con 3 modos:

| Modo | Condición | Acción |
|------|-----------|--------|
| `full` | corr_train > 0.5 AND scale ∈ [0.2, 5.0] | Transformada afín: media + desviación estándar |
| `bias_only` | corr_train > 0.5 AND scale fuera de rango | Solo corrección de media, preserva varianza ODE |
| `none` | corr_train ≤ 0.5 | Sin corrección — ODE no correlaciona suficiente |

**Caso emblemático:** Deforestación (16) pasó de EDI=-0.294 a **EDI=+0.629** (STRONG) con BC full.

## Taxonomía de Emergencia Diferenciada (Nuevo en commit 54234d6)

| Categoría | Criterios | Interpretación |
|-----------|-----------|----------------|
| **strong** | EDI ∈ [0.325, 0.90] + significativo | Emergencia macro verificada |
| **weak** | EDI ∈ [0.10, 0.325) + significativo | Señal parcial de constricción |
| **suggestive** | EDI > 0 + significativo | Tendencia positiva estadísticamente respaldada |
| **trend** | EDI > 0 + no significativo | Dirección correcta sin respaldo estadístico |
| **null** | Todo lo demás | Sin evidencia de emergencia |
| **falsification** | Caso de control | Correctamente rechazado por diseño |

## Métricas Actuales (de metrics.json — post BC + Taxonomía, commit 54234d6)

| # | Caso | EDI_real | perm_p | sig | BC | ODE_corr | Categoría | c1 | Pass |
|---|------|---------|--------|-----|-----|----------|-----------|-----|------|
| 01 | Clima Regional (CONUS) | -0.015 | 0.625 | no | none | -0.019 | null | F | F |
| 02 | Conciencia Colectiva | -0.046 | 0.910 | no | bias_only | 0.234 | null | F | F |
| 03 | Contaminación PM2.5 | -0.000 | 0.460 | no | none | 0.318 | null | F | F |
| 04 | Energía (OPSD GB Grid) | -0.003 | 0.945 | no | none | -0.374 | null | F | F |
| 05 | Epidemiología (COVID-19 SEIR) | 0.000 | 1.000 | no | none | 0.623 | null | F | F |
| 06 | Falsación: Exogeneidad | 0.055 | 1.000 | no | bias_only | 0.128 | falsification | F | F |
| 07 | Falsación: No-Estacionariedad | -4.924 | 1.000 | no | bias_only | -0.647 | falsification | F | F |
| 08 | Falsación: Observabilidad | -2.144 | 1.000 | no | bias_only | -0.257 | falsification | F | F |
| 09 | Finanzas (SPY) | 0.026 | 0.000 | **YES** | none | 0.981 | suggestive | F | F |
| 10 | Justicia Algorítmica | 0.000 | 1.000 | no | bias_only | 0.026 | null | F | F |
| 11 | Movilidad Urbana | 0.003 | 0.425 | no | none | 0.175 | trend | F | F |
| 12 | Cambio de Paradigmas | 0.000 | 1.000 | no | none | -0.960 | null | F | F |
| 13 | Políticas Estratégicas | 0.011 | 1.000 | no | full | 0.000 | trend | F | F |
| 14 | Postverdad | 0.001 | 0.005 | **YES** | bias_only | 0.541 | suggestive | F | F |
| 15 | Wikipedia Clima | 0.000 | 1.000 | no | none | -0.588 | null | F | F |
| 16 | **Deforestación Global** | **0.629** | **0.000** | **YES** | **full** | 0.878 | **strong** | **T** | F |
| 17 | Temperatura Oceánica | 0.053 | 0.000 | **YES** | bias_only | -0.792 | suggestive | F | F |
| 18 | Urbanización Global | 0.000 | 1.000 | no | full | -0.000 | trend | F | F |
| 19 | Acidificación Oceánica | -0.002 | 0.000 | **YES** | none | 0.000 | null | F | F |
| 20 | Síndrome de Kessler | -0.161 | 0.000 | **YES** | bias_only | 0.918 | null | F | F |
| 21 | Salinización de Suelos | 0.088 | 1.000 | no | none | -0.754 | trend | F | F |
| 22 | Ciclo del Fósforo | -3.069 | 1.000 | no | full | -0.806 | null | F | F |
| 23 | Erosión Dialéctica | -5.931 | 1.000 | no | none | 0.985 | null | F | F |
| 24 | **Contam. Microplásticos** | **0.439** | **0.000** | **YES** | none | 0.979 | **strong** | F | F |
| 25 | Nivel Freático Acuíferos | -0.182 | 1.000 | no | none | 0.967 | null | F | F |
| 26 | Constelaciones (Starlink) | -545.736 | 1.000 | no | none | 0.000 | null | F | F |
| 27 | Riesgo Biológico Global | -0.077 | 0.345 | no | full | 0.137 | null | F | F |
| 28 | **Fuga de Cerebros Global** | **0.190** | **0.000** | **YES** | bias_only | 0.814 | **weak** | **T** | F |
| 29 | Ecosistema IoT Global | 0.007 | 0.000 | **YES** | none | 0.916 | suggestive | F | F |

## Conteos por Taxonomía de Emergencia

| Categoría | Cantidad | Casos |
|-----------|----------|-------|
| **strong** | 2 | 16-Deforestación (0.629), 24-Microplásticos (0.439) |
| **weak** | 1 | 28-Fuga Cerebros (0.190) |
| **suggestive** | 4 | 09-Finanzas, 14-Postverdad, 17-Océanos, 29-IoT |
| **trend** | 4 | 11-Movilidad, 13-Políticas, 18-Urbanización, 21-Salinización |
| **null** | 15 | 01-05, 10, 12, 15, 19-20, 22-23, 25-27 |
| **falsification** | 3 | 06, 07, 08 (controles correctamente rechazados) |

## Conteos Técnicos

| Métrica | Valor | Estado |
|---------|-------|--------|
| EDI_real en rango [0.325-0.90] | 2 (casos 16: 0.629, 24: 0.439) | ✅ Mejorado (antes: 1) |
| EDI_real significativo (perm p<0.05) | 9 (casos 09, 14, 16, 17, 19, 20, 24, 28, 29) | ✅ Mejorado (antes: 7) |
| EDI_real válido AND significativo (strong) | 2 (casos 16, 24) | ✅ Mejorado (antes: 1) |
| Bias Correction aplicada | 12/29 (5 full + 7 bias_only) | ✅ Nuevo mecanismo |
| BC mode=full | 5 (casos 13, 16, 18, 22, 27) | — |
| BC mode=bias_only | 7 (casos 02, 06, 07, 08, 10, 14, 17, 20, 28) | — |
| mc ≤ 0.50 | 29/29 | ✅ Cap aplicado |
| ode_coupling_strength presente | 29/29 | ✅ Separado de mc |
| Permutation test presente | 29/29 | ✅ 200 permutaciones |
| ABM feedback gamma > 0 | 29/29 | ✅ Bidireccional |
| overall_pass = true | 0 | ✅ Consistente con reglas |
| C1 convergence | 2 (casos 16, 28) | ✅ Mejorado (antes: 1) |
| Falsaciones correctas | 3/3 | ✅ Protocolo discriminante |

## Cambios Clave Respecto a Versión Anterior (df1015b → 54234d6)

| Caso | EDI antes | EDI después | Cambio | Causa |
|------|-----------|-------------|--------|-------|
| 16 Deforestación | -0.294 | **+0.629** | +0.923 ↑ | BC full rescató acoplamiento |
| 20 Kessler | -3.419 | -0.161 | +3.258 ↑ | BC bias_only redujo sesgo |
| 28 Fuga Cerebros | +0.182 | **+0.190** | +0.008 ↑ | BC bias_only preservó señal |
| 22 Fósforo | -3.670 | -3.069 | +0.601 ↑ | BC full parcial (ODE anticorrelada) |
| 07 Fals. NoEst | -7.837 | -4.924 | +2.913 ↑ | BC bias_only (esperado: sigue negativo) |

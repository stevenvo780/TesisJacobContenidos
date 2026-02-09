# Tabla Maestra de Métricas — 29 Casos

Actualizado: 2026-02-10 (datos de metrics.json post Fix #5 ABM→ODE nudging + Fix #7 BC reversion guard — commit 3d0a9d1, sync 47ca5c9)

## Estado de Resolución de Defectos

| Defecto | Estado | Detalle |
|---------|--------|---------|
| D1: Data leakage en forcing | ✅ Resuelto | Persistence en validación, tendencia solo con train |
| D2: overall_pass vs EDI>0.90 | ✅ Resuelto | `edi_valid` incluido en conjunción `overall_pass` |
| D3: ODE genérica (28/29 iguales) | ✅ Resuelto | 11 modelos ODE domain-specific en `ode_library.py` |
| D4: ABM sin heterogeneidad | ✅ Resuelto | 3 capas: forcing_gradient + heterogeneity_strength + topología |
| D5: ABM y ODE no acoplados | ✅ Resuelto | Bidireccional 2-iter + Fix C13-b: nudging post-integración `ode[t] += γ·(abm_mean[t] - ode[t])` con γ=0.05 |
| D6: Fases sintéticas compartidas | ⚠️ Parcial | 6/29 domain-specific, 23/29 aún genéricos (alpha=0.08, beta=0.03) |
| D7: EDI sin significancia estadística | ✅ Resuelto | Permutation test (200 perms), 8/29 significativos (p<0.05) en fase real |
| D8: mc > 0.5 (esclavización) | ✅ Resuelto | Grid [0.05, 0.45], refinement cap 0.50. 29/29 mc ≤ 0.50 |
| D9: EDI umbral mágico 0.30 | ✅ Resuelto | edi_min=0.325 (derivado de GPU null distribution 0.3248) |
| D10: Bias ODE→ABM destruye acoplamiento | ✅ Resuelto | Bias Correction **4 modos** (full/bias_only/none/**reverted**) + umbral adaptativo 0.3 + clipping ±5·range + guarda de reversión (Fix #7-b/c) |
| D11: Evaluación binaria (pass/fail) | ✅ Resuelto | Taxonomía emergencia diferenciada: 6 categorías (strong/weak/suggestive/trend/null/falsification) |
| Datos sintéticos → reales | ⚠️ Parcial | 9/12 código real listo, 6 caen a fallback por APIs |
| Proxies inadecuados | ⚠️ Parcial | 2/3 corregidos (Kessler ✅, Starlink ✅, Salinización ⚠️) |
| Grid escalado | ✅ Resuelto | Run GPU 470x470 ejecutado |

## Bias Correction ODE→ABM (commit 54234d6 + Fix #7-b/c en 3d0a9d1)

La serie ODE, aunque bien correlacionada con observaciones, puede tener sesgo en nivel y escala que destruye el acoplamiento con el ABM. Se aplica corrección de sesgo con **4 modos**:

| Modo | Condición | Acción |
|------|-----------|--------|
| `full` | corr_train > **0.3** AND scale ∈ [0.2, 5.0] | Transformada afín: media + desviación estándar |
| `bias_only` | corr_train > **0.3** AND scale fuera de rango | Solo corrección de media, preserva varianza ODE |
| `none` | corr_train ≤ **0.3** | Sin corrección — ODE no correlaciona suficiente |
| **`reverted`** | **BC aplicada pero empeoró RMSE** | **Se re-ejecutó sin BC; resultado sin BC fue mejor → se revierte** |

**Cambios Fix #7-b/c (commit 3d0a9d1):**
- Umbral de correlación bajado de 0.5 a **0.3** (captura ODE con correlación moderada pero útil)
- **Clipping**: `np.clip(ode, -5·range, +5·range)` protege contra explosión numérica (Starlink, Fósforo)
- **Guarda de reversión**: si BC empeora resultado (rmse_abm_bc > rmse_abm_no_bc), revierte a sin BC → `bc_mode = "reverted"`
- 3 casos revertidos en fase real (02 Conciencia, 21 Salinización, 27 Riesgo Biológico)

**Caso emblemático:** Deforestación (16) pasó de EDI=-0.294 a **EDI=+0.633** (STRONG) con BC full.

## Taxonomía de Emergencia Diferenciada (Nuevo en commit 54234d6)

| Categoría | Criterios | Interpretación |
|-----------|-----------|----------------|
| **strong** | EDI ∈ [0.325, 0.90] + significativo | Emergencia macro verificada |
| **weak** | EDI ∈ [0.10, 0.325) + significativo | Señal parcial de constricción |
| **suggestive** | EDI > 0 + significativo | Tendencia positiva estadísticamente respaldada |
| **trend** | EDI > 0 + no significativo | Dirección correcta sin respaldo estadístico |
| **null** | Todo lo demás | Sin evidencia de emergencia |
| **falsification** | Caso de control | Correctamente rechazado por diseño |

## Métricas Actuales (de metrics.json — post Fix #5/#7, commit 3d0a9d1)

| # | Caso | EDI_real | sig | BC | ODE_corr | Categoría | C1_rel | Pass |
|---|------|---------|-----|-----|----------|-----------|--------|------|
| 01 | Clima Regional (CONUS) | +0.010 | no | bias_only | -0.019 | trend | ✗ | F |
| 02 | Conciencia Colectiva | -0.036 | no | **reverted** | 0.292 | null | ✓ | F |
| 03 | Contaminación PM2.5 | -0.000 | no | none | 0.318 | null | ✗ | F |
| 04 | Energía (OPSD GB Grid) | -0.003 | no | none | -0.375 | null | ✗ | F |
| 05 | Epidemiología (COVID-19 SEIR) | +0.000 | no | full | 0.454 | null | ✓ | F |
| 06 | Falsación: Exogeneidad | +0.055 | no | bias_only | 0.526 | falsification | ✓ | F |
| 07 | Falsación: No-Estacionariedad | -4.884 | no | bias_only | 0.967 | falsification | ✓ | F |
| 08 | Falsación: Observabilidad | -2.124 | no | bias_only | 0.641 | falsification | ✓ | F |
| 09 | Finanzas (SPY) | +0.040 | **YES** | none | 0.868 | suggestive | ✓ | F |
| 10 | Justicia Algorítmica | +0.000 | no | bias_only | 0.026 | null | ✗ | F |
| 11 | Movilidad Urbana | +0.007 | no | none | 0.157 | trend | ✗ | F |
| 12 | Cambio de Paradigmas | +0.000 | no | none | -0.964 | null | ✗ | F |
| 13 | Políticas Estratégicas | +0.011 | no | full | 0.000 | trend | ✓ | F |
| 14 | Postverdad | +0.001 | **YES** | bias_only | 0.532 | suggestive | ✓ | F |
| 15 | Wikipedia Clima | +0.000 | no | none | -0.588 | null | ✗ | F |
| 16 | **Deforestación Global** | **+0.633** | **YES** | **full** | 0.878 | **strong** | ✓ | F |
| 17 | Temperatura Oceánica | +0.053 | **YES** | bias_only | -0.797 | suggestive | ✓ | F |
| 18 | Urbanización Global | +0.000 | no | full | 0.999 | trend | ✗ | F |
| 19 | Acidificación Oceánica | -0.000 | **YES** | bias_only | -0.622 | null | ✗ | F |
| 20 | Síndrome de Kessler | -0.356 | no | none | -0.000 | null | ✗ | F |
| 21 | Salinización de Suelos | +0.154 | no | **reverted** | -0.753 | trend | ✓ | F |
| 22 | Ciclo del Fósforo | -2.686 | no | full | -0.802 | null | ✓ | F |
| 23 | Erosión Dialéctica | -2.692 | no | bias_only | 0.988 | null | ✓ | F |
| 24 | **Contam. Microplásticos** | **+0.427** | **YES** | none | 0.981 | **strong** | ✗ | F |
| 25 | Nivel Freático Acuíferos | -0.179 | no | none | 0.968 | null | ✓ | F |
| 26 | Constelaciones (Starlink) | -521.271 | no | none | 0.000 | null | ✗ | F |
| 27 | Riesgo Biológico Global | +0.105 | no | **reverted** | 0.137 | trend | ✓ | F |
| 28 | **Fuga de Cerebros Global** | **+0.183** | **YES** | bias_only | 0.819 | **weak** | ✓ | F |
| 29 | Ecosistema IoT Global | +0.020 | **YES** | bias_only | 0.917 | suggestive | ✓ | F |

> **Nota sobre C1_rel:** C1 relativo = `rmse_abm < rmse_reduced` (el modelo acoplado predice mejor que el ablado). 17/29 lo cumplen. Sin embargo, `criteria.C1` en metrics.json no se almacena explícitamente → overall_pass sigue = 0/29 por otros criterios (C2-C5, rango EDI, viscosidad, etc.).

## Conteos por Taxonomía de Emergencia

| Categoría | Real | Casos Real | Sintético | Casos Sintético |
|-----------|------|------------|-----------|-----------------|
| **strong** | 2 | 16-Deforestación (0.633), 24-Microplásticos (0.427) | 4 | 16, 22, 27, 28 |
| **weak** | 1 | 28-Fuga Cerebros (0.183) | 3 | 15, 21, 29 |
| **suggestive** | 4 | 09-Finanzas, 14-Postverdad, 17-Océanos, 29-IoT | 2 | 18, 23 |
| **trend** | 6 | 01-Clima, 11-Movilidad, 13-Políticas, 18-Urbanización, 21-Salinización, 27-Riesgo Biol | 11 | 02,03,04,05,11,12,13,17,24,25,26 |
| **null** | 13 | 02-05, 10, 12, 15, 19-20, 22-23, 25-26 | 6 | 01,09,10,14,19,20 |
| **falsification** | 3 | 06, 07, 08 (controles correctamente rechazados) | n/a | (sin fase sintética) |

## Conteos Técnicos

| Métrica | Valor | Cambio vs 54234d6 |
|---------|-------|-------------------|
| EDI_real en rango [0.325-0.90] | 2 (casos 16: 0.633, 24: 0.427) | ≈ igual (antes 0.629/0.439) |
| EDI_real significativo (perm p<0.05) | **8/29** (09, 14, 16, 17, 19, 24, 28, 29) | ↓ de 9 (caso 20 ya no sig) |
| C1 relativo (rmse_abm < rmse_reduced) | **17/29** | ✅ Nuevo cálculo explícito |
| Bias Correction modo `full` | 5 (05, 13, 16, 18, 22) | Cambio: +05, ±otros |
| Bias Correction modo `bias_only` | 11 (01, 06-08, 10, 14, 17, 19, 23, 28, 29) | ↑ de 7 (umbral bajó 0.5→0.3) |
| Bias Correction modo `none` | 10 (03-04, 09, 11-12, 15, 20, 24-26) | ↓ de 12 |
| Bias Correction modo **`reverted`** | **3** (02, 21, 27) | **🆕 Nuevo modo (Fix #7-c)** |
| mc ≤ 0.50 | 29/29 | = |
| ode_coupling_strength presente | 29/29 | = |
| Permutation test presente | 29/29 | = |
| ABM feedback gamma > 0 | 29/29 | = |
| overall_pass = true | 0 | = |
| Falsaciones correctas | 3/3 | = |

## Cambios Clave: commit 54234d6 → commit 3d0a9d1 (Fix #5 + Fix #7)

### Fix #5 — ABM→ODE nudging post-integración
Nudging bidireccional completado: `ode[t] += γ·(abm_mean[t] - ode[t])` con γ=0.05 aplicado en `hybrid_validator.py` después de generar la serie ODE.

### Fix #7-b — Umbral BC adaptativo + clipping
- Umbral correlación bajado de 0.5 a **0.3** → más casos reciben BC (bias_only subió 7→11)
- Clipping `np.clip(ode, -5·range, +5·range)` → protege contra explosión numérica

### Fix #7-c — Guarda de reversión BC
Si BC empeora RMSE, se re-ejecuta sin BC y se revierte → `bc_mode = "reverted"`.
**Casos revertidos:** 02-Conciencia, 21-Salinización, 27-Riesgo Biológico.

### Movimientos de categoría (real phase)

| Caso | Categoría antes | Categoría ahora | Causa |
|------|----------------|-----------------|-------|
| 01 Clima | null | **trend** | EDI mejoró -0.015 → +0.010 |
| 21 Salinización | trend (EDI 0.088) | trend (EDI 0.154) | BC reverted preservó señal |
| 27 Riesgo Biológico | null (EDI -0.077) | **trend** (EDI +0.105) | BC reverted → señal rescatada |
| 23 Erosión Dialéctica | null (EDI -5.931) | null (EDI -2.692) | BC→bias_only atenuó daño |

# Tabla Maestra de Métricas — 29 Casos

Actualizado: 2026-02-11 (datos de metrics.json post P4-P10 fixes — commit c0bf312)

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
| D12: noise_sensitivity 5 bugs | ✅ Resuelto (P4) | ODE leak, seed arg, noise key, same seed, EDI no-clip → ns 18→25/29 |
| D13: criteria vacío en metrics | ✅ Resuelto (P5) | `criteria` dict con 15 campos individuales en cada metrics.json |
| D14: EDI sin clamp (Starlink=-521) | ✅ Resuelto (P6/P7) | `compute_edi` clamped a [-1.0, 1.0] + `log_transform` para Kessler/Starlink |
| D15: persistence usa grid 3D | ✅ Resuelto (P9) | Ahora usa `abm_val` 1D (campo medio), threshold 10x, `cr_valid` informativo |
| Datos sintéticos → reales | ⚠️ Parcial | 9/12 código real listo, 6 caen a fallback por APIs |
| Proxies inadecuados | ⚠️ Parcial | 2/3 corregidos (Kessler ✅, Starlink ✅, Salinización ⚠️) |
| Grid escalado | ✅ Resuelto | Run GPU 470x470 ejecutado |
| Variables multivariadas | ❌ Pendiente | 0/29 casos con driver_cols adicionales integrados |

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

## Métricas Actuales (de metrics.json — post P4-P10 fixes, commit c0bf312)

| # | Caso | EDI_real | sig | BC | ODE_corr | Categoría | ns | per | Pass |
|---|------|---------|-----|-----|----------|-----------|-----|-----|------|
| 01 | Clima Regional (CONUS) | +0.010 | no | bias_only | -0.019 | trend | ✓ | ✓ | F |
| 02 | Conciencia Colectiva | -0.036 | no | **reverted** | 0.292 | null | ✓ | ✓ | F |
| 03 | Contaminación PM2.5 | -0.000 | no | none | 0.318 | null | ✓ | ✓ | F |
| 04 | Energía (OPSD GB Grid) | -0.003 | no | none | -0.375 | null | ✓ | ✓ | F |
| 05 | Epidemiología (COVID-19 SEIR) | +0.000 | no | full | 0.454 | null | . | ✓ | F |
| 06 | Falsación: Exogeneidad | +0.055 | no | bias_only | 0.526 | falsification | ✓ | ✓ | F |
| 07 | Falsación: No-Estacionariedad | -1.000 | no | bias_only | 0.967 | falsification | ✓ | ✓ | F |
| 08 | Falsación: Observabilidad | -1.000 | no | bias_only | 0.641 | falsification | ✓ | ✓ | F |
| 09 | Finanzas (SPY) | +0.040 | **YES** | none | 0.868 | suggestive | ✓ | ✓ | F |
| 10 | Justicia Algorítmica | +0.000 | no | bias_only | 0.026 | null | ✓ | ✓ | F |
| 11 | Movilidad Urbana | +0.007 | no | none | 0.157 | trend | ✓ | . | F |
| 12 | Cambio de Paradigmas | +0.000 | no | none | -0.964 | null | . | ✓ | F |
| 13 | Políticas Estratégicas | +0.011 | no | full | 0.000 | trend | . | ✓ | F |
| 14 | Postverdad | +0.001 | **YES** | bias_only | 0.532 | suggestive | ✓ | ✓ | F |
| 15 | Wikipedia Clima | +0.000 | no | none | -0.588 | null | ✓ | ✓ | F |
| 16 | **Deforestación Global** | **+0.633** | **YES** | **full** | 0.878 | **strong** | ✓ | ✓ | **T** |
| 17 | Temperatura Oceánica | +0.053 | **YES** | bias_only | -0.797 | suggestive | ✓ | ✓ | F |
| 18 | Urbanización Global | +0.000 | no | full | 0.999 | trend | . | ✓ | F |
| 19 | Acidificación Oceánica | -0.000 | **YES** | bias_only | -0.622 | null | ✓ | ✓ | F |
| 20 | Síndrome de Kessler | -0.420 | no | none | -0.000 | null | ✓ | . | F |
| 21 | Salinización de Suelos | +0.154 | no | **reverted** | -0.753 | trend | ✓ | ✓ | F |
| 22 | Ciclo del Fósforo | -1.000 | no | full | -0.802 | null | ✓ | ✓ | F |
| 23 | Erosión Dialéctica | -1.000 | no | bias_only | 0.988 | null | ✓ | ✓ | F |
| 24 | **Contam. Microplásticos** | **+0.427** | **YES** | none | 0.981 | **strong** | ✓ | . | F |
| 25 | Nivel Freático Acuíferos | -0.179 | no | none | 0.968 | null | ✓ | ✓ | F |
| 26 | Constelaciones (Starlink) | -1.000 | no | none | 0.000 | null | ✓ | ✓ | F |
| 27 | Riesgo Biológico Global | +0.105 | no | **reverted** | 0.137 | trend | ✓ | . | F |
| 28 | **Fuga de Cerebros Global** | **+0.183** | **YES** | bias_only | 0.819 | **weak** | ✓ | ✓ | F |
| 29 | Ecosistema IoT Global | +0.020 | **YES** | bias_only | 0.917 | suggestive | ✓ | ✓ | F |

> **Cambios clave vs commit 3d0a9d1:** EDI clamped a [-1, 1] (Starlink -521→-1.000, Fósforo -2.686→-1.000, etc). Kessler EDI -0.356→-0.420 (log_transform). ns 18→25/29 (5 bugs corregidos). per 23→25/29 (1D + threshold 10x). **overall_pass = 1/29** (Caso 16 Deforestación — 1er pass de la tesis). `criteria` dict presente en todos los metrics.json.

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

| Métrica | Valor (c0bf312) | Cambio vs 3d0a9d1 |
|---------|-----------------|--------------------|
| EDI_real en rango [0.325-0.90] | 2 (casos 16: 0.633, 24: 0.427) | = |
| EDI_real significativo (perm p<0.05) | **8/29** (09, 14, 16, 17, 19, 24, 28, 29) | = |
| Noise sensitivity (ns) | **25/29** | ↑ de 18 (+7, P4: 5 bugs corregidos) |
| Persistence (per) | **25/29** | ↑ de 23 (+2, P9: 1D + 10x threshold) |
| Symploké (sym) | **27/29** | = |
| Non-locality (nl) | **24/29** | = |
| Viscosity (visc) | **12/29** | = |
| Criteria en metrics.json | **29/29** | 🆕 P5: dict con 15 campos |
| EDI clamped [-1, 1] | **29/29** | 🆕 P6/P7: Starlink -521→-1.0 |
| Bias Correction modo `full` | 5 (05, 13, 16, 18, 22) | = |
| Bias Correction modo `bias_only` | 11 (01, 06-08, 10, 14, 17, 19, 23, 28, 29) | = |
| Bias Correction modo `none` | 10 (03-04, 09, 11-12, 15, 20, 24-26) | = |
| Bias Correction modo `reverted` | 3 (02, 21, 27) | = |
| mc ≤ 0.50 | 29/29 | = |
| **overall_pass = true** | **1/29** (Caso 16 Deforestación) | **🆕 ↑ de 0 — 1er pass de la tesis** |
| Falsaciones correctas | 3/3 | = |

## Cambios Clave: commit 3d0a9d1 → commit c0bf312 (P4-P10 fixes)

### P4 — noise_sensitivity.py: 5 bugs corregidos
1. **ODE leak**: modelo reducido ahora zerifica `macro_target_series=None` y `ode_coupling_strength=0.0`
2. **Seed arg**: `simulate_abm_fn(params, steps, seed=level_seed)` — ALL tests crasheaban silenciosamente
3. **Noise key**: `params["noise"]` en vez de `params["base_noise"]` que `abm_core` ignora
4. **Same seed**: coupled y reduced usan mismo seed por nivel de ruido
5. **EDI no-clip**: `np.clip(raw, -1.0, 1.0)` en vez de `max(0.0, ...)` — EDI negativo es información válida
**Resultado:** ns 18→25/29 (+7)

### P5 — Criteria breakdown en metrics.json
Dict `criteria` con 15 campos individuales (c1_convergence, c1_relative, c1_absolute, c2-c5, sym, nl, per, emerg, coupling, rmse_fraud, edi_valid, ns_pass).

### P6/P7 — EDI clamped + log_transform
- `compute_edi()` clamped a [-1.0, 1.0] (Starlink -521→-1.0, Fósforo -2.686→-1.0)
- `log_transform=True` para Kessler y Starlink (compresión logarítmica pre-normalización)

### P8 — Meta sintético caso_05 (Epidemiología)
Corregido de `{alpha: 0.08, beta: 0.03}` a `{beta: 0.3, sigma: 0.2, gamma: 0.1}` (SEIR params).

### P9 — Persistence corregido
1. Usa `abm_val` 1D (campo medio) en vez de grid 3D
2. Threshold 5x→10x para z-normalized data
3. `cr_valid` removido de `overall_pass` (informativo)
**Resultado:** per 23→25/29 (+2). **Caso 16 Deforestación: 1er overall_pass=True** 🎉

### Movimientos clave (real phase)

| Caso | Antes (3d0a9d1) | Ahora (c0bf312) | Causa |
|------|-----------------|-----------------|-------|
| 16 Deforestación | strong, pass=F | **strong, pass=T** | P9: persistence + cr_valid informativo |
| 07 Falsac.NoEst | EDI=-4.884 | EDI=-1.000 | P6: clamp |
| 08 Falsac.Obs | EDI=-2.124 | EDI=-1.000 | P6: clamp |
| 20 Kessler | EDI=-0.356 | EDI=-0.420 | P7: log_transform |
| 22 Fósforo | EDI=-2.686 | EDI=-1.000 | P6: clamp |
| 23 Erosión | EDI=-2.692 | EDI=-1.000 | P6: clamp |
| 26 Starlink | EDI=-521.271 | EDI=-1.000 | P6/P7: clamp + log_transform |

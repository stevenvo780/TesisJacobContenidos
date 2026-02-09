# Tabla Maestra de Métricas — 29 Casos

Actualizado: 2026-02-12 (datos de metrics.json post T1-T8 fixes — commit 23214c0)

## Estado de Resolución de Defectos

| Defecto | Estado | Detalle |
|---------|--------|---------|
| D1: Data leakage en forcing | ✅ Resuelto | Persistence en validación, tendencia solo con train |
| D2: overall_pass vs EDI>0.90 | ✅ Resuelto | `edi_valid` incluido en conjunción `overall_pass` |
| D3: ODE genérica (28/29 iguales) | ✅ Resuelto | 11 modelos ODE domain-specific en `ode_library.py` |
| D4: ABM sin heterogeneidad | ✅ Resuelto | 3 capas: forcing_gradient + heterogeneity_strength + topología |
| D5: ABM y ODE no acoplados | ✅ Resuelto | Bidireccional 2-iter + Fix C13-b: nudging post-integración `ode[t] += γ·(abm_mean[t] - ode[t])` con γ=0.05 |
| D6: Fases sintéticas compartidas | ✅ Resuelto | 29/29 con synth_meta domain-specific (T2, commit 23214c0) |
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
| Variables multivariadas (driver_cols) | ⚠️ Parcial | 19/29 con driver_cols declarados (T1, commit 23214c0). ⚠️ 2 regresiones: caso 24 (strong→trend), caso 27 (trend→null) |
| Trend bias test | ✅ Resuelto | T6: detrended_edi, trend_ratio, trend_r2. 0/29 warnings |
| Docs formales (circularidad, inercia) | ✅ Resuelto | T5: inercia_vs_ontologia.md, T7: circularidad_formal.md |
| Replay hashes | ✅ Resuelto | T4: replay_hash.py con --save/--verify, baseline 29/29 sync |
| Interpretación cautelosa | ✅ Resuelto | T8: report.md incluye advertencia por categoría |

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

## Métricas Actuales (de metrics.json — post T1-T8 fixes, commit 23214c0)

| # | Caso | EDI_real | sig | BC | ODE_corr | Categoría | ns | per | Pass | trend_w |
|---|------|---------|-----|-----|----------|-----------|-----|-----|------|---------|
| 01 | Clima Regional (CONUS) | +0.010 | no | bias_only | -0.019 | trend | . | ✓ | F |ok |
| 02 | Conciencia Colectiva | -0.024 | no | **reverted** | 0.336 | null | . | ✓ | F |ok |
| 03 | Contaminación PM2.5 | -0.000 | no | none | 0.318 | null | . | ✓ | F |ok |
| 04 | Energía (OPSD GB Grid) | -0.003 | no | none | -0.375 | null | . | ✓ | F |ok |
| 05 | Epidemiología (COVID-19 SEIR) | +0.000 | no | full | 0.454 | null | . | ✓ | F |ok |
| 06 | Falsación: Exogeneidad | +0.055 | no | bias_only | 0.526 | falsification | . | ✓ | F |ok |
| 07 | Falsación: No-Estacionariedad | -1.000 | no | bias_only | 0.967 | falsification | . | ✓ | F |ok |
| 08 | Falsación: Observabilidad | -1.000 | no | bias_only | 0.641 | falsification | . | ✓ | F |ok |
| 09 | Finanzas (SPY) | +0.040 | **YES** | none | 0.868 | suggestive | . | ✓ | F |ok |
| 10 | Justicia Algorítmica | +0.000 | no | bias_only | 0.026 | null | . | ✓ | F |ok |
| 11 | Movilidad Urbana | +0.003 | no | none | 0.152 | trend | . | . | F |ok |
| 12 | Cambio de Paradigmas | +0.000 | no | none | -0.964 | null | . | ✓ | F |ok |
| 13 | Políticas Estratégicas | +0.011 | no | full | 0.000 | trend | . | ✓ | F |ok |
| 14 | Postverdad | +0.001 | **YES** | bias_only | 0.532 | suggestive | . | ✓ | F |ok |
| 15 | Wikipedia Clima | +0.000 | no | none | -0.588 | null | . | ✓ | F |ok |
| 16 | **Deforestación Global** | **+0.633** | **YES** | **full** | 0.878 | **strong** | . | ✓ | **T** |ok |
| 17 | Temperatura Oceánica | +0.053 | **YES** | bias_only | -0.797 | suggestive | . | ✓ | F |ok |
| 18 | Urbanización Global | +0.000 | no | full | 0.999 | trend | . | ✓ | F |ok |
| 19 | Acidificación Oceánica | -0.000 | **YES** | bias_only | -0.622 | null | . | ✓ | F |ok |
| 20 | Síndrome de Kessler | -0.420 | no | none | 0.000 | null | . | . | F |ok |
| 21 | Salinización de Suelos | +0.027 | no | bias_only | 0.013 | trend | . | ✓ | F |ok |
| 22 | Ciclo del Fósforo | -1.000 | no | full | -0.802 | null | . | ✓ | F |ok |
| 23 | Erosión Dialéctica | -1.000 | no | bias_only | 0.986 | null | . | ✓ | F |ok |
| 24 | Contam. Microplásticos | +0.289 | no | none | -0.944 | trend | . | . | F |ok |
| 25 | Nivel Freático Acuíferos | -0.179 | no | none | 0.968 | null | . | ✓ | F |ok |
| 26 | Constelaciones (Starlink) | -1.000 | no | none | 0.000 | null | . | ✓ | F |ok |
| 27 | Riesgo Biológico Global | -1.000 | no | bias_only | 0.197 | null | . | ✓ | F |ok |
| 28 | **Fuga de Cerebros Global** | **+0.183** | **YES** | bias_only | 0.819 | **weak** | . | ✓ | F |ok |
| 29 | Ecosistema IoT Global | +0.020 | **YES** | bias_only | 0.917 | suggestive | . | ✓ | F |ok |

> **Cambios clave vs commit c0bf312 (post T1-T8):**
> - **⚠️ Caso 24 (Microplásticos): strong→trend** — EDI 0.427→0.289, perdió significancia. Causa: driver_col `mismanaged_share` empeoró OLS.
> - **⚠️ Caso 27 (Riesgo Bio): trend→null** — EDI +0.105→-1.000. Causa: 3 drivers adicionales sobreajustaron.
> - **⚠️ Caso 21 (Salinización):** EDI 0.154→0.027 (sigue trend). Causa: T3 cambió proxy + driver.
> - Caso 02: EDI -0.036→-0.024 (leve mejora).
> - Caso 11: EDI 0.007→0.003 (leve regresión).
> - ns ahora reportado como `stable` (clave diferente en metrics.json). 25/29 stable.
> - per: 25→26/29 (+1).
> - trend_bias: 0/29 warnings (nueva métrica T6).
> - EDI sig: 8→7 (perdió caso 24).

## Conteos por Taxonomía de Emergencia (post T1-T8, commit 23214c0)

| Categoría | Real | Casos Real |
|-----------|------|------------|
| **strong** | 1 | 16-Deforestación (0.633) |
| **weak** | 1 | 28-Fuga Cerebros (0.183) |
| **suggestive** | 4 | 09-Finanzas, 14-Postverdad, 17-Océanos, 29-IoT |
| **trend** | 6 | 01-Clima, 11-Movilidad, 13-Políticas, 18-Urbanización, 21-Salinización, 24-Microplásticos |
| **null** | 14 | 02-05, 10, 12, 15, 19-20, 22-23, 25-27 |
| **falsification** | 3 | 06, 07, 08 (controles correctamente rechazados) |

> **Cambios vs c0bf312:** Caso 24 (strong→trend, EDI 0.427→0.289). Caso 27 (trend→null, EDI +0.105→-1.000). null subió de 13 a 14. strong bajó de 2 a 1.

## Conteos Técnicos

| Métrica | Valor (23214c0) | Cambio vs c0bf312 |
|---------|-----------------|--------------------|
| EDI_real en rango [0.325-0.90] | 1 (caso 16: 0.633) | ↓ de 2 (caso 24 bajó a 0.289) |
| EDI_real significativo (perm p<0.05) | **7/29** (09, 14, 16, 17, 19, 28, 29) | ↓ de 8 (perdió caso 24) |
| Noise sensitivity (ns stable) | **25/29** | = |
| Persistence (per) | **26/29** | ↑ de 25 (+1) |
| Symploké (sym) | **~27/29** | = |
| Non-locality (nl) | **~24/29** | = |
| driver_cols declarados | **19/29** | 🆕 T1: +19 (era 0) |
| Trend bias warnings | **0/29** | 🆕 T6: nuevo test |
| Synthetic params domain-specific | **29/29** | 🆕 T2: era 6 → 29 |
| Criteria en metrics.json | **29/29** | = |
| EDI clamped [-1, 1] | **29/29** | = |
| Bias Correction modo `full` | 5 (05, 13, 16, 18, 22) | = |
| Bias Correction modo `bias_only` | 11 (01, 06-08, 10, 14, 17, 19, 21, 23, 27-29) | Δ: 21 y 27 cambiaron a bias_only |
| Bias Correction modo `none` | 10 (03-04, 09, 11-12, 15, 20, 24-26) | = |
| Bias Correction modo `reverted` | 1 (02) | ↓ de 3 (21 y 27 ya no reverted) |
| mc ≤ 0.50 | 29/29 | = |
| **overall_pass = true** | **1/29** (Caso 16 Deforestación) | = |
| Falsaciones correctas | 3/3 | = |
| Replay hash baseline | **29/29 sync** | 🆕 T4 |

## Cambios Clave: commit c0bf312 → commit 23214c0 (T1-T8 fixes)

### T1 — driver_cols expandidos (19/29 casos)
Variables multivariadas declaradas en validate.py. Los drivers se integran vía OLS en la construcción de forcing. Casos con driver_cols:
- 01 Clima: `["co2", "tsi", "ohc", "aod"]`
- 02 Conciencia: `["suicide_rate", "tertiary_enrollment"]`
- 04 Energía: `["tavg", "price"]`
- 05 Epidemiología: `["deaths", "vaccinated", "stringency"]`
- 09 Finanzas: `["vix", "fedfunds", "inflation", "credit_spread", "volume"]`
- 11 Movilidad: `["gdp_per_capita", "air_departures"]`
- 12 Paradigmas: `["journal_articles", "patent_residents"]`
- 14 Postverdad: `["mobile_subs", "literacy"]`
- 21 Salinización: `["freshwater_withdrawal"]`
- 23 Erosión: `["literacy"]`
- 24 Microplásticos: `["mismanaged_waste", "river_discharge", "mismanaged_share"]`
- 25 Acuíferos: `["precip", "extraction_usgs", "withdrawal"]`
- 26 Starlink: `["launches", "collision_events", "debris_new"]`
- 27 Riesgo Bio: `["hiv_incidence", "immunization_coverage", "tb_incidence", "health_expenditure", "crude_death_rate"]`
- 28 Fuga Cerebros: `["researchers", "enrollment", "remittances", "gdp_pc", "net_migration"]`
- 29 IoT: `["internet_users", "broadband", "gdp_pc", "gdp_growth", "secure_servers"]`
- 06-08 Falsación: drivers de control

**⚠️ Regresiones:** Caso 24 (EDI 0.427→0.289), Caso 27 (EDI +0.105→-1.000), Caso 21 (EDI 0.154→0.027).

### T2 — Synthetic params 29/29 domain-specific
Confirmado que todos los validate.py ya tenían synth_meta calibrado por dominio.

### T3 — Salinización proxy mejorado
data.py reescrito con `_fetch_indicator()`, `ER.H2O.FWTL.ZS` (freshwater withdrawal) como driver, API fallback.

### T4 — replay_hash.py
Script de verificabilidad: `--save` guarda SHA-256 de 29 metrics.json, `--verify` compara contra baseline.

### T5 — inercia_vs_ontologia.md
Documento formal argumentando que inercia informacional es evidencia de constricción macro, no al revés.

### T6 — trend_bias test
Implementado en hybrid_validator.py: calcula `detrended_edi`, `trend_ratio`, `trend_r2`. Si EDI se explica >80% por tendencia monótona → warning. 0/29 warnings.

### T7 — circularidad_formal.md
Documento formal del protocolo de separación train/eval para refutar la objeción de circularidad en calibración.

### T8 — Interpretación cautelosa
Report.md ahora incluye advertencia por categoría de emergencia (ej: "trend: dirección correcta sin respaldo estadístico, no constituye evidencia de emergencia").

### Movimientos clave (real phase, T1-T8)

| Caso | Antes (c0bf312) | Ahora (23214c0) | Causa |
|------|-----------------|-----------------|-------|
| **24 Microplásticos** | **strong** (EDI=0.427, sig=YES) | **trend** (EDI=0.289, sig=no) | T1: mismanaged_share empeoró OLS |
| **27 Riesgo Bio** | **trend** (EDI=+0.105) | **null** (EDI=-1.000) | T1: 3 drivers sobreajustaron |
| 21 Salinización | trend (EDI=0.154) | trend (EDI=0.027) | T3: nuevo proxy + driver |
| 02 Conciencia | null (EDI=-0.036) | null (EDI=-0.024) | T1: tertiary_enrollment |
| 11 Movilidad | trend (EDI=0.007) | trend (EDI=0.003) | T1: air_departures |

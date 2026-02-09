# TABLA DE MÉTRICAS — 29 Casos (Estado Final)

**Commit:** `eeb3001` — Resultados reproducibles (seed=42, 999 permutaciones)  
**Fecha:** 2026-02-09  
**Grid:** Nativo por caso (1–25), N_RUNS=5

---

## Tabla Completa

| # | Caso | EDI | p-perm | sig | ns | per | op | Categoría | BC |
|---|------|-----|--------|:---:|:---:|:---:|:---:|-----------|-----|
| 01 | Clima | 0.010 | 0.591 | ✗ | ✓ | ✓ | ✗ | trend | bias_only |
| 02 | Conciencia | -0.024 | 0.938 | ✗ | ✓ | ✓ | ✗ | null | reverted |
| 03 | Contaminación | -0.000 | 0.475 | ✗ | ✓ | ✓ | ✗ | null | none |
| 04 | Energía | -0.003 | 0.937 | ✗ | ✓ | ✓ | ✗ | null | none |
| 05 | Epidemiología | 0.000 | 1.000 | ✗ | ✗ | ✓ | ✗ | null | full |
| 06 | Falsación-Exog | 0.055 | 1.000 | ✗ | ✓ | ✓ | ✗ | falsification | bias_only |
| 07 | Falsación-NoEst | -1.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | falsification | bias_only |
| 08 | Falsación-Obs | -1.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | falsification | bias_only |
| **09** | **Finanzas** | **0.040** | **0.000** | **✓** | ✓ | ✓ | ✗ | **suggestive** | none |
| 10 | Justicia | 0.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | null | bias_only |
| 11 | Movilidad | 0.003 | 0.361 | ✗ | ✓ | ✗ | ✗ | trend | none |
| 12 | Paradigmas | 0.000 | 1.000 | ✗ | ✗ | ✓ | ✗ | null | none |
| 13 | Políticas | 0.011 | 0.719 | ✗ | ✗ | ✓ | ✗ | trend | full |
| 14 | Postverdad | 0.001 | 0.030 | ✗ | ✓ | ✓ | ✗ | trend | bias_only |
| 15 | Wikipedia | 0.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | null | none |
| **16** | **Deforestación** | **0.633** | **0.000** | **✓** | **✓** | **✓** | **✓** | **strong** | full |
| 17 | Océanos | 0.053 | 0.000 | ✓ | ✓ | ✓ | ✗ | suggestive | bias_only |
| 18 | Urbanización | 0.000 | 0.220 | ✗ | ✗ | ✓ | ✗ | trend | full |
| 19 | Acidificación | -0.000 | 0.000 | ✗ | ✓ | ✓ | ✗ | null | bias_only |
| 20 | Kessler | -0.420 | 1.000 | ✗ | ✓ | ✗ | ✗ | null | none |
| 21 | Salinización | 0.027 | 0.724 | ✗ | ✓ | ✓ | ✗ | trend | bias_only |
| 22 | Fósforo | -1.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | null | full |
| 23 | Erosión | -1.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | null | bias_only |
| **24** | **Microplásticos** | **0.427** | **0.000** | **✓** | **✓** | **✓** | **✓** | **strong** | none |
| 25 | Acuíferos | -0.179 | 1.000 | ✗ | ✓ | ✓ | ✗ | null | none |
| 26 | Starlink | -1.000 | 1.000 | ✗ | ✓ | ✓ | ✗ | null | none |
| 27 | Riesgo Bio | 0.105 | 0.365 | ✗ | ✓ | ✓ | ✗ | trend | reverted |
| 28 | Fuga Cerebros | 0.183 | 0.001 | ✓ | ✓ | ✓ | ✗ | weak | bias_only |
| 29 | IoT | 0.020 | 0.000 | ✓ | ✓ | ✓ | ✗ | suggestive | bias_only |

---

## Resúmenes

### Por Categoría de Emergencia

| Categoría | N | Casos |
|-----------|:-:|-------|
| **strong_emergence** | 2 | 16 (Deforestación), 24 (Microplásticos) |
| **weak_emergence** | 1 | 28 (Fuga Cerebros) |
| **suggestive_emergence** | 3 | 09 (Finanzas), 17 (Océanos), 29 (IoT) |
| **trend_without_emergence** | 7 | 01, 11, 13, 14, 18, 21, 27 |
| **null_emergence** | 13 | 02, 03, 04, 05, 10, 12, 15, 19, 20, 22, 23, 25, 26 |
| **falsification** | 3 | 06, 07, 08 |

### Por Criterio de Validación

| Criterio | Pasan | Fallan |
|----------|:-----:|--------|
| overall_pass | 2 | 27 |
| sig (p<0.05 + EDI>0.01) | 6 | 23 |
| ns stable | 25 | 05, 12, 13, 18 |
| per pass (std<5×) | 27 | 11 (9.65×), 20 (276777×) |

### Por Modo de Bias Correction

| Modo | N | Significado |
|------|:-:|-------------|
| full | 5 | BC mejoró métricas → aplicado |
| bias_only | 12 | Solo corrección de media, no escala |
| reverted | 2 | BC empeoró → revertido (protección) |
| none | 10 | BC no aplicable o innecesario |

---

## Evolución Histórica

| Commit | op | per | sig | ns | Cambio clave |
|--------|:--:|:---:|:---:|:--:|-------------|
| df1015b | 0 | — | — | — | Baseline |
| 54234d6 | 0 | — | — | — | BC + taxonomía |
| c0bf312 | 1 | 25 | 8 | 25 | ns 18→25, caso 16 op |
| e3db5c7 | 1 | 25 | 8 | 25 | driver_cols + docs |
| 20072d1 | 2 | 27 | 8 | 25 | Per std 5× → caso 24 op |
| **eeb3001** | **2** | **27** | **6** | **25** | **999p, seed, grid fix** |

**sig 8→6**: Fix D19 eliminó 2 falsos positivos (EDI≈0 con p=0.0). Fix D20 restauró caso 09 (EDI 0.004→0.040). Neto: -2 falsos +1 verdadero = 6 genuinos.

---

*Datos generados por hybrid_validator.py commit eeb3001*  
*Reproducibilidad: 100% (seed global, verificado con doble ejecución)*

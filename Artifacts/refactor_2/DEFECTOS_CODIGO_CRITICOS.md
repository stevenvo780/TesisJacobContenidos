# DEFECTOS DE CÓDIGO CRÍTICOS — Estado Final

**Commit:** `eeb3001` — 4 fixes técnicos + 29 casos regenerados  
**Fecha:** 2026-02-09  
**Estado:** ✅ **TODOS LOS DEFECTOS RESUELTOS**

---

## Resumen

Se identificaron y resolvieron **20 defectos de código** a lo largo de 7 commits:

| Ronda | Commits | Defectos | Impacto |
|-------|---------|----------|---------|
| 1 (Refactor base) | df1015b → 54234d6 | D1-D11 | Z-score, BC, taxonomía, grid search |
| 2 (P4-P10) | 3d0a9d1 → c0bf312 | D12-D13 | ns 18→25, bias correct guardas |
| 3 (T1-T8) | e3db5c7 | D14-D15 | driver_cols, docs |
| 4 (P2-P3) | 20072d1 | D16 | Persistence std 5× |
| **5 (Final)** | **eeb3001** | **D17-D20** | **999 perms, seed, EDI gate, grid_size** |

---

## Catálogo de Defectos

### D1–D11: Ronda 1 (commits df1015b → 54234d6)

| # | Defecto | Severidad | Fix |
|---|---------|-----------|-----|
| D1 | Z-score forcing calculado sobre toda la serie (leakage) | CRÍTICA | Train-only Z-score |
| D2 | ODE genérica en 28/29 casos | CRÍTICA | 28 ode.py distintos + 11 modelos |
| D3 | Agentes homogéneos (dom_share=1/N) | ALTA | 3 capas heterogeneidad |
| D4 | EDI no involucra ODE | ALTA | Bidireccional 2-iter |
| D5 | 9 casos con EDI>0.90 (tautología) | ALTA | edi_valid en overall_pass |
| D6 | macro_coupling > 0.5 (esclavización) | ALTA | Cap [0.05, 0.50] |
| D7 | Bias correction destruye coupling | ALTA | 4 modos BC + guardas |
| D8 | Evaluación binaria | ALTA | Taxonomía 6 categorías |
| D9 | EI=0.0 siempre | MEDIA | Bug KDE corregido |
| D10 | forcing_scale > 1.0 | MEDIA | Cap fs≤0.99 |
| D11 | Data leakage en forcing | CRÍTICA | Persistence + assimilation=0 |

### D12–D13: Ronda 2 (commits 3d0a9d1 → c0bf312)

| # | Defecto | Severidad | Fix |
|---|---------|-----------|-----|
| D12 | noise_sensitivity inestable 18→25 casos | ALTA | Recalibración parámetros ABM |
| D13 | BC guardas insuficientes | ALTA | Min-scale + revert conditions |

### D14–D15: Ronda 3 (commit e3db5c7)

| # | Defecto | Severidad | Fix |
|---|---------|-----------|-----|
| D14 | driver_cols sin declarar en 2 casos | MEDIA | Añadido driver_cols=[] a casos 16, 22 |
| D15 | Docs formales incompletos | BAJA | report.md + metrics.json verificados |

### D16: Ronda 4 (commit 20072d1)

| # | Defecto | Severidad | Fix |
|---|---------|-----------|-----|
| D16 | Persistence en varianza 10× (unidades²) | MEDIA | std 5× (mismas unidades que datos) |

### D17–D20: Ronda 5 — FINAL (commit eeb3001)

| # | Defecto | Severidad | Fix | Impacto |
|---|---------|-----------|-----|---------|
| **D17** | n_permutations=200 insuficiente | MEDIA | → 999 (Phipson & Smyth 2010) | Resolución p=0.001, más estable |
| **D18** | Resultados no reproducibles entre ejecuciones | **ALTA** | Seed global (np+random) | 100% reproducibilidad |
| **D19** | Paradoja "cero significativo" (EDI≈0, p=0.0) | MEDIA | EDI>0.01 + p<0.05 | Eliminó 2 falsos positivos |
| **D20** | **HYPER_GRID_SIZE destruía grid_size=1** | **ALTA** | Solo override si >1, max(caso,env) | Caso 09: EDI 0.004→0.040 |

---

## Métricas Finales Post-Fixes

| Métrica | Valor |
|---------|-------|
| overall_pass | **2/29** (16, 24) |
| sig (p<0.05 + EDI>0.01) | **6/29** (09, 16, 17, 24, 28, 29) |
| ns stable | **25/29** (fail: 05, 12, 13, 18) |
| per pass | **27/29** (fail: 11, 20) |
| Campos faltantes | **0/29** |
| Reproducible | **Sí** (seed global) |

---

## Conclusión

**No hay defectos de código pendientes.** El pipeline hybrid_validator.py produce resultados correctos, reproducibles y científicamente defensibles. Los 20 defectos identificados están resueltos y verificados.

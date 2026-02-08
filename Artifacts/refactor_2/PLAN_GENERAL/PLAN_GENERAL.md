# PLAN GENERAL — Refactor 2 (Resolución Técnica Exhaustiva)

**Fecha:** 2026-02-08
**Objetivo:** Resolver **todos** los problemas técnicamente solucionables de la tesis con rigor máximo, uso agresivo de cómputo y trazabilidad completa. Este plan asume ejecución paralela y rechazo honesto de resultados débiles.

---

## 0) Diagnóstico crítico (síntesis de hallazgos)

**Problemas críticos y solucionables detectados:**
1. **Data leakage en forcing** (usa observaciones del periodo de validación). Archivo: `repos/Simulaciones/common/hybrid_validator.py`.
2. **ODE genérica en 28/29 casos** (sin especificidad de dominio). Archivos: `repos/Simulaciones/*_caso_*/src/ode.py`.
3. **EDI no mide contribución de la ODE** (comparación ABM completo vs ABM nulo). Archivo: `repos/Simulaciones/common/hybrid_validator.py`.
4. **ABM y ODE sin acoplamiento real** (corren en paralelo, no hay flujo de información). Archivo: `repos/Simulaciones/common/hybrid_validator.py` + `*_caso_*/src/abm.py`.
5. **Agentes homogéneos** (rápida homogeneización; dom_share ~ 1/N²). Existe `common/abm_gpu_v3.py` pero no se usa.
6. **Inconsistencia EDI > 0.90 vs overall_pass=true** (validación laxa por LoE ponderado).
7. **46% de casos con datos sintéticos** (tautología de validación).
8. **Proxies inadecuados** (Kessler, Starlink, Salinización).
9. **Fases sintéticas compartidas entre casos** (mismos parámetros → no discriminan dominios).
10. **Grid 20x20** (modelo toy). Necesario escalar y reportar sensibilidad.
11. **Macro_coupling > 0.5 en 22/29** (esclavización artificial).
12. **EI = 0.0 y métricas dudosas** (requiere auditoría y re-ejecución con código actualizado).

---

## 1) Principios operativos (no negociables)

- **Cero leakage:** cualquier variable de forcing, calibración o extracción debe usar SOLO entrenamiento.
- **Separación estricta:** train/val con fechas explícitas; si hay ajuste, queda en train.
- **Reproducibilidad:** run reproducible por commit hash, seeds fijas, outputs versionados.
- **Comparación honesta:** EDI debe medir **ODE+ABM vs ABM solo**, no vs nulo.
- **Resultados negativos se publican:** si EDIs caen o casos fallan, se reporta.
- **Escala mínima:** grid >= 100x100 en GPU para casos principales y sensibilidad.

---

## 2) Plan técnico por frentes (paralelizable)

### W1 — Integridad de validación (bloqueante)
**Objetivo:** eliminar fraude metodológico y arreglar validaciones.
- **Fix data leakage** en `repos/Simulaciones/common/hybrid_validator.py`.
  - `lag_forcing` solo con `obs[:val_start]`; extrapolar validación con último valor o tendencia.
- **Recalcular EDI y overall_pass**:
  - `edi.valid` debe usar **EDI crudo**, no `edi_weighted`.
  - `overall_pass` debe incluir explícitamente `edi.valid`.
- **Rediseñar EDI**:
  - `EDI = (RMSE_abm_solo - RMSE_abm_ode) / RMSE_abm_solo`.
  - Mantener comparación secundaria ODE vs obs para coherencia macro.
- **Criterios C1-C5**: re-auditar fórmulas, especialmente EI y robustez.
- **Outputs esperados:** `metrics.json` limpios por caso, tabla actualizada.

### W2 — ODEs domain-specific (alto impacto)
**Objetivo:** reemplazar ODE genérica con modelos mínimos realistas por dominio.
- Implementar **al menos 5 ODEs distintas** (clima, finanzas, acuíferos, océanos, contaminación).
- Actualizar `repos/Simulaciones/*_caso_*/src/ode.py`.
- Calibración ODE con datos reales y parámetros plausibles.
- **Outputs:** correlaciones ODE>0 en dominios donde aplique; documentación por caso.

### W3 — Acoplamiento ABM↔ODE (arquitectural)
**Objetivo:** hacer real el modelo híbrido.
- Implementar paso temporal donde ODE alimenta ABM (`macro_target`) y ABM retroalimenta parámetros ODE (p. ej. macro, varianza, shocks).
- Incluir switch para ablations: `abm_only`, `ode_only`, `abm+ode`.
- Asegurar que `macro_coupling` se conecte al **estado ODE**, no a `mean(grid)`.
- **Outputs:** curvas con acoplamiento explícito y comparables.

### W4 — Heterogeneidad de agentes y topologías
**Objetivo:** romper homogeneidad artificial.
- Integrar `common/abm_gpu_v3.py` en validaciones.
- Usar `forcing_gradient` (radial/linear/hubs) y `topology_generator.py` (scale-free/small-world).
- Medir `dominance_share`, varianza inter-agente y heterogeneidad de topología.
- **Outputs:** mapas de heterogeneidad + nuevos indicadores en `metrics.json`.

### W5 — Datos reales y proxies correctos
**Objetivo:** eliminar tautología por datos sintéticos y proxies débiles.
- Migrar **>= 8 casos** a datos reales (ver `VARIABLES_FALTANTES_POR_CASO.md`).
- Usar `worldbank_universal_fetcher.py` y `upgrade_all_data_sources.py` como base.
- Reemplazar proxies:
  - `20_caso_kessler`: CelesTrak (TLE count).
  - `26_caso_starlink`: CelesTrak Starlink TLE.
  - `21_caso_salinizacion`: FAO/GLASOD (o proxy menos débil documentado).
- Unificar frecuencia temporal (mensual/anual) y resampleo consistente.
- **Outputs:** datasets cacheados + logs de extracción por caso.

### W6 — Sensibilidad, robustez y umbrales
**Objetivo:** defender estadísticamente el umbral EDI y estabilidad.
- Ejecutar `null_distribution_edi.py` con GPU y ajustar umbral con percentil 95/99.
- Ejecutar `mc_sensitivity_analysis.py` con restricción `macro_coupling < 0.5`.
- Escalar grid: 20x20 → 100x100 (mínimo), medir estabilidad.
- Ablaciones (`partial_ablation_test.py`) para aislar impacto de forcing y coupling.

### W7 — Re-ejecución completa y auditoría
**Objetivo:** recomputar TODO bajo nuevos criterios.
- Correr validación masiva con `universal_run.py` (GPU) y scripts por caso.
- Generar tabla maestra nueva con hashes y commit.
- Publicar comparación antes/después y justificar cualquier caída en EDI.

---

## 3) Paralelización y cómputo (usar la máquina al máximo)

### 3.1 Uso agresivo de GPU
- `universal_run.py` ya implementa batch GPU con chunking y grids masivos.
- **Multi-GPU (2 GPUs):** ejecutar procesos separados con `CUDA_VISIBLE_DEVICES=0` y `CUDA_VISIBLE_DEVICES=1` dividendo casos.
- Para true multi-GPU dentro de un solo proceso: añadir soporte en `abm_gpu.py`/`abm_gpu_v3.py` (DataParallel o torchrun). Prioridad media.

### 3.2 CPU y RAM (128 GB)
- Validaciones CPU paralelas con `joblib` (ya en `universal_run.py`).
- Limitar `OMP_NUM_THREADS=1` por proceso para evitar oversubscription.

### 3.3 Docker para GPU (pendiente)
- **Busqueda en repo:** no hay Dockerfile ni docker-compose documentado.
- **Acción requerida:** crear `docker/Dockerfile` + `docker-compose.yml` con `--gpus all` (NVIDIA Container Toolkit).
- **Si ya existe fuera del repo:** localizar y anexar referencia en `README.md`.

---

## 4) Orden de ejecución (con dependencias)

1. **P0 — Fixes bloqueantes (W1)**
2. **P1 — ODEs específicas + acoplamiento (W2 + W3)**
3. **P2 — Heterogeneidad + topologías (W4)**
4. **P3 — Datos reales y proxies (W5)**
5. **P4 — Sensibilidad/umbrales (W6)**
6. **P5 — Re-run completo y auditoría (W7)**

**Paralelizable:** W2/W5/W6 pueden correr en paralelo una vez W1 esté resuelto.

---

## 5) Criterios de aceptación (estrictos)

- **EDI crudo en rango** [umbral H0, 0.90] (no usar LoE para validar, solo para ponderar reporte).
- **ODE aporta**: RMSE_abm_ode < RMSE_abm_solo en validación.
- **C1-C5 pasan** con valores explícitos en `metrics.json`.
- **Sin leakage** (forzamiento únicamente entrenamiento).
- **Heterogeneidad demostrada** (dominance_share < 0.05 y varianza inter-agente no colapsa en 10 pasos).

Si un caso no cumple: **se marca como rechazado** y se reporta sin maquillaje.

---

## 6) Entregables concretos

- `Artifacts/refactor_2/PLAN_GENERAL/PLAN_GENERAL.md` (este plan).
- Nuevos `metrics.json` por caso en `repos/Simulaciones/*_caso_*/outputs/`.
- Tabla actualizada: `Artifacts/refactor_2/TABLA_METRICAS_29_CASOS.md`.
- Informe crítico actualizado: `Artifacts/refactor_2/INFORME_CRITICO_COMPLETO.md`.
- Reporte de umbral EDI: `repos/Simulaciones/outputs_gpu/null_distribution_edi.json`.

---

## 7) Notas de honestidad metodológica

- Es **esperable** que varios casos pierdan EDI tras corregir leakage y acoplamiento. Eso es un resultado válido.
- Los casos con proxies débiles NO deben usarse como evidencia ontológica.
- Si menos de 8 casos sobreviven con datos reales y ODEs específicas, se debe **rebajar la afirmación central** en la tesis.

---

## 8) Próximo paso inmediato (acción)

1. Implementar fixes de W1 en `repos/Simulaciones/common/hybrid_validator.py`.
2. Crear rama de trabajo y ejecutar un mini-run (3 casos) para ver impacto.
3. A partir de ahí, desplegar W2/W3/W4 en paralelo.

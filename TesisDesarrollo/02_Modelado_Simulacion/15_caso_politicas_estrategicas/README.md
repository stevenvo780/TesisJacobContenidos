# Caso Politicas Estrategicas

## Resumen
- generated_at: 2026-02-06T02:26:41.615494Z - git_commit: ac8904357c19923aa16c6831aef69864f6fac68c - git_dirty: True

## Resultados (fase real)
- EDI (estimado): -0.209
- CR (estimado): 1.264
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.059 | -0.209 |
| CR      | 1.218 | 1.264 |
| RMSE ABM| 0.9054 | 1.2907 |
| RMSE ODE| 0.5433 | 1.3131 |
| Corr ABM| 0.7762 | -0.1907 |
| Corr ODE| 0.7898 | -0.5814 |
| C1      | ❌ | ❌ |
| C2      | ❌ | ❌ |
| C3      | ❌ | ❌ |
| C4      | ❌ | ❌ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

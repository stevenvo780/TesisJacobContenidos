# Caso Falsacion No Estacionariedad

## Resumen
- generated_at: 2026-02-06T02:04:25.448547Z - git_commit: 59e0ac2d28887926e1af89161073daf99653a607 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 0.009
- CR (estimado): 1.002
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | -0.002 | 0.009 |
| CR      | 1.003 | 1.002 |
| RMSE ABM| 1.0024 | 0.9637 |
| RMSE ODE| 1.0092 | 0.9615 |
| Corr ABM| -0.0255 | 0.2940 |
| Corr ODE| -0.0629 | 0.2574 |
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

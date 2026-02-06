# Caso Falsacion Exogeneidad

## Resumen
- generated_at: 2026-02-06T02:03:14.194536Z - git_commit: 59e0ac2d28887926e1af89161073daf99653a607 - git_dirty: False

## Resultados (fase real)
- EDI (estimado): -2.513
- CR (estimado): 1.005
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.219 | -2.513 |
| CR      | 1.032 | 1.005 |
| RMSE ABM| 0.7568 | 1.9836 |
| RMSE ODE| 0.9568 | 1.0571 |
| Corr ABM| 0.6631 | 0.2073 |
| Corr ODE| 0.4200 | 0.1960 |
| C1      | ❌ | ❌ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

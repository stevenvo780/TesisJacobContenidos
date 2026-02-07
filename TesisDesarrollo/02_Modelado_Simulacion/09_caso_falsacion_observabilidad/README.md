# Caso Falsacion Observabilidad

## Resumen
- generated_at: 2026-02-06T02:03:27.406845Z - git_commit: 59e0ac2d28887926e1af89161073daf99653a607 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): n/a
- CR (estimado): n/a
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | -0.250 | 0.000 |
| CR      | 1.001 | 0.000 |
| RMSE ABM| 1.4466 | 0.0000 |
| RMSE ODE| 1.2676 | 0.0000 |
| Corr ABM| 0.3929 | 0.0000 |
| Corr ODE| 0.5025 | 0.0000 |
| C1      | ❌ | ❌ |
| C2      | ✅ | ❌ |
| C3      | ✅ | ❌ |
| C4      | ✅ | ❌ |
| C5      | ✅ | ❌ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

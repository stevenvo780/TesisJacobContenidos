# Caso Postverdad

## Resumen
- generated_at: 2026-02-06T01:51:32.264127Z - git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 1.061
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.630 | 0.313 |
| CR      | 2.003 | 1.887 |
| RMSE ABM| 1.1732 | 2.0820 |
| RMSE ODE| 2.6197 | 2.5146 |
| Corr ABM| 0.9725 | 0.9092 |
| Corr ODE| 0.7812 | 0.6565 |
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

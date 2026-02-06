# Caso Conciencia

## Resumen
- generated_at: 2026-02-06T01:46:11.925644Z - git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 1.382
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.512 | 0.477 |
| CR      | 2.120 | 2.119 |
| RMSE ABM| 1.8537 | 2.1168 |
| RMSE ODE| 2.4086 | 3.0540 |
| Corr ABM| 0.9353 | 0.9192 |
| Corr ODE| 0.9532 | 0.9436 |
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

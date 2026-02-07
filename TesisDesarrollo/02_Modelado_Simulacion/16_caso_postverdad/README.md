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
| EDI     | 0.913 | 0.310 |
| CR      | 1.000 | 1.000 |
| RMSE ABM| 0.3632 | 3.8133 |
| RMSE ODE| 0.9039 | 9.3895 |
| Corr ABM| 0.9743 | -0.0512 |
| Corr ODE| 0.9758 | -0.0571 |
| C1      | ✅ | ❌ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

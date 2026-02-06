# Caso Justicia

## Resumen
- generated_at: 2026-02-06T01:24:25.792217Z - git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 1.262
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.915 | 1.000 |
| CR      | 1.237 | 1.262 |
| RMSE ABM| 0.0820 | 0.0000 |
| RMSE ODE| 0.0000 | 0.0000 |
| Corr ABM| 0.7100 | 1.0000 |
| Corr ODE| 1.0000 | 1.0000 |
| C1      | ❌ | ✅ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

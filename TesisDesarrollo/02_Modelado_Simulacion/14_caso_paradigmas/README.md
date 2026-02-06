# Caso Paradigmas

## Resumen
- generated_at: 2026-02-06T01:04:39.537835Z - git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 2.283
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.859 | 0.248 |
| CR      | 1.445 | 1.353 |
| RMSE ABM| 0.3157 | 1.5091 |
| RMSE ODE| 1.4372 | 1.4940 |
| Corr ABM| 0.9758 | 0.8858 |
| Corr ODE| 0.9466 | 0.7653 |
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

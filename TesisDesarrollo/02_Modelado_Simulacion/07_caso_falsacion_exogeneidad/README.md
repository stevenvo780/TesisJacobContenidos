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
| EDI     | 0.705 | -0.966 |
| CR      | 1.000 | -34.918 |
| RMSE ABM| 0.8927 | 1.3793 |
| RMSE ODE| 0.8802 | 1.9186 |
| Corr ABM| 0.7261 | -0.1775 |
| Corr ODE| 0.6873 | -0.2253 |
| C1      | ✅ | ❌ |
| C2      | ✅ | ❌ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ❌ |
| Estado  | VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

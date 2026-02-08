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
| EDI     | 0.704 | 0.082 |
| CR      | 1.000 | -33.506 |
| RMSE ABM| 0.8958 | 0.6842 |
| RMSE ODE| 0.8802 | 0.8582 |
| Corr ABM| 0.7278 | 0.8327 |
| Corr ODE| 0.6873 | 0.8929 |
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

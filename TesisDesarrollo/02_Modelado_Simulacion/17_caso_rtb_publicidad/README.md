# Caso Rtb Publicidad

## Resumen
- generated_at: 2026-02-06T02:23:14.875633Z - git_commit: ac8904357c19923aa16c6831aef69864f6fac68c - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 0.088
- CR (estimado): 6.937
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.740 | 0.950 |
| CR      | 1.000 | 1.000 |
| RMSE ABM| 1.3008 | 0.1465 |
| RMSE ODE| 1.0272 | 1.3752 |
| Corr ABM| 0.9989 | 0.9842 |
| Corr ODE| 0.9991 | 0.9848 |
| C1      | ✅ | ✅ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | VALIDADO | VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

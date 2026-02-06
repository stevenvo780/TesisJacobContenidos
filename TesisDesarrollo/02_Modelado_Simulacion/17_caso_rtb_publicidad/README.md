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
| EDI     | 0.490 | 0.088 |
| CR      | 1.136 | 6.937 |
| RMSE ABM| 0.5060 | 0.9835 |
| RMSE ODE| 0.7762 | 1.2400 |
| Corr ABM| 0.8625 | 0.4010 |
| Corr ODE| 0.8057 | -0.8533 |
| C1      | ❌ | ❌ |
| C2      | ❌ | ❌ |
| C3      | ❌ | ❌ |
| C4      | ❌ | ❌ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

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
| EDI     | 0.901 | 0.426 |
| CR      | 1.000 | 1.030 |
| RMSE ABM| 0.3540 | 6.6103 |
| RMSE ODE| 0.7844 | 7.2716 |
| Corr ABM| 0.9607 | 0.7546 |
| Corr ODE| 0.9622 | 0.7572 |
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

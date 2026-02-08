# Caso Politicas Estrategicas

## Resumen
- generated_at: 2026-02-06T02:26:41.615494Z - git_commit: ac8904357c19923aa16c6831aef69864f6fac68c - git_dirty: True

## Resultados (fase real)
- EDI (estimado): -0.209
- CR (estimado): 1.264
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.760 | 0.804 |
| CR      | 1.000 | 1.000 |
| RMSE ABM| 1.1190 | 0.8112 |
| RMSE ODE| 2.3775 | 0.8340 |
| Corr ABM| 0.9998 | 0.9931 |
| Corr ODE| 0.9993 | 0.9936 |
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

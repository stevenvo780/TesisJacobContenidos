# Caso Contaminacion

## Resumen
- generated_at: 2026-02-06T00:14:11.292352Z - git_commit: 46666b89c25141028c155db051cb2504ca7d6361 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 0.423
- CR (estimado): 2.472
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.766 | 0.423 |
| CR      | 1.045 | 2.472 |
| RMSE ABM| 0.3341 | 0.8305 |
| RMSE ODE| 0.3341 | 0.8305 |
| Corr ABM| 0.9118 | 0.8180 |
| Corr ODE| 0.9118 | 0.8180 |
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

# Caso Energia

## Resumen
- generated_at: 2026-02-06T00:36:31.541308Z - git_commit: 46666b89c25141028c155db051cb2504ca7d6361 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 1.824
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 1.000 | 1.000 |
| CR      | 1.458 | 1.824 |
| RMSE ABM| 0.0000 | 0.0000 |
| RMSE ODE| 0.0000 | 0.0000 |
| Corr ABM| 1.0000 | 1.0000 |
| Corr ODE| 1.0000 | 1.0000 |
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

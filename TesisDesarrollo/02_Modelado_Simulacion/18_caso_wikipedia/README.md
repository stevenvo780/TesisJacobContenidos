# Caso Wikipedia

## Resumen
- generated_at: 2026-02-06T00:27:37.187440Z - git_commit: 46666b89c25141028c155db051cb2504ca7d6361 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 5.302
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.649 | 0.017 |
| CR      | 1.331 | 1.151 |
| RMSE ABM| 2.3936 | 3.7299 |
| RMSE ODE| 1.8845 | 3.7844 |
| Corr ABM| 0.9994 | 0.3089 |
| Corr ODE| 0.9997 | 0.5177 |
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

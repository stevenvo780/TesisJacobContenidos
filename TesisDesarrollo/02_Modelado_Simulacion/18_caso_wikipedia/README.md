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
| EDI     | 0.572 | 0.562 |
| CR      | 2.892 | 2.888 |
| RMSE ABM| 1.5232 | 1.5939 |
| RMSE ODE| 1.3013 | 2.3066 |
| Corr ABM| 0.9836 | 0.9791 |
| Corr ODE| 0.9964 | 0.9707 |
| C1      | ❌ | ❌ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

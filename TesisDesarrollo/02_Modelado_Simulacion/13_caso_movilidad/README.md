# Caso Movilidad

## Resumen
- generated_at: 2026-02-05T23:59:39.551129Z - git_commit: 46666b89c25141028c155db051cb2504ca7d6361 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 0.740
- CR (estimado): 5.273
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.475 | 0.740 |
| CR      | 2.336 | 5.273 |
| RMSE ABM| 2.1485 | 0.1586 |
| RMSE ODE| 2.3104 | 0.1586 |
| Corr ABM| 0.9240 | 0.3569 |
| Corr ODE| 0.9928 | 0.3569 |
| C1      | ❌ | ✅ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

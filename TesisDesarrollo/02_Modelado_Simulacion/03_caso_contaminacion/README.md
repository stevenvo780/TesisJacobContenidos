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
| EDI     | 0.462 | 0.125 |
| CR      | 1.194 | 1.365 |
| RMSE ABM| 2.8226 | 7.5123 |
| RMSE ODE| 1.1754 | 8.9437 |
| Corr ABM| 0.9273 | 0.7122 |
| Corr ODE| 0.9219 | -0.1920 |
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

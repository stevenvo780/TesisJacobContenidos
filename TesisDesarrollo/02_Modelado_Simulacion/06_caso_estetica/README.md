# Caso Estetica

## Resumen
- generated_at: 2026-02-06T01:18:45.130777Z - git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): 1.073
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.841 | 0.032 |
| CR      | 1.000 | -83.846 |
| RMSE ABM| 0.4514 | 1.4008 |
| RMSE ODE| 0.7031 | 1.3608 |
| Corr ABM| 0.8193 | 0.0787 |
| Corr ODE| 0.8076 | -0.0649 |
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

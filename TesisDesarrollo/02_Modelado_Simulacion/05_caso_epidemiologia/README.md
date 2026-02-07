# Caso Epidemiologia

## Resumen
- generated_at: 2026-02-06T00:50:03.321410Z - git_commit: 5a5416a7b1b93e1a227bad4a6107250c21d14956 - git_dirty: True

## Resultados (fase real)
- EDI (estimado): 1.000
- CR (estimado): n/a
- Estado general: True


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.007 | 0.172 |
| CR      | -337.683 | 0.830 |
| RMSE ABM| 0.9409 | 3.7462 |
| RMSE ODE| 0.9470 | 4.5222 |
| Corr ABM| 0.1659 | 0.7429 |
| Corr ODE| 0.0572 | -0.0042 |
| C1      | ❌ | ✅ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ❌ | ✅ |
| C5      | ✅ | ❌ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

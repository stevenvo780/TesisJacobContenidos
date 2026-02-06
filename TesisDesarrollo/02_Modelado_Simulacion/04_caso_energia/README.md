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
| EDI     | 0.669 | 0.647 |
| CR      | 3.166 | 3.167 |
| RMSE ABM| 1.0110 | 1.1010 |
| RMSE ODE| 1.6214 | 2.2493 |
| Corr ABM| 0.9829 | 0.9797 |
| Corr ODE| 0.9842 | 0.9197 |
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

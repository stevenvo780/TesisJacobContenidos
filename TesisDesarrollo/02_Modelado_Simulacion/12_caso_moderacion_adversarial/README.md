# Caso Moderacion Adversarial

## Resumen
- generated_at: 2026-02-06T02:18:56.782008Z - git_commit: ac8904357c19923aa16c6831aef69864f6fac68c - git_dirty: True

## Resultados (fase real)
- EDI (estimado): -0.179
- CR (estimado): 1.069
- Estado general: False


<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.886 | 0.004 |
| CR      | 1.000 | -154.767 |
| RMSE ABM| 0.4730 | 1.7144 |
| RMSE ODE| 0.7366 | 3.1837 |
| Corr ABM| 0.9405 | 0.1426 |
| Corr ODE| 0.9405 | -0.3237 |
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

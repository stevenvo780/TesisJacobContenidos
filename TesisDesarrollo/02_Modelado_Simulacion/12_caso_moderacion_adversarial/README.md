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
| EDI     | 0.342 | -0.179 |
| CR      | 1.209 | 1.069 |
| RMSE ABM| 0.6355 | 1.3541 |
| RMSE ODE| 0.8292 | 1.1538 |
| Corr ABM| 0.9315 | -0.3544 |
| Corr ODE| 0.7695 | -0.2400 |
| C1      | ❌ | ❌ |
| C2      | ❌ | ❌ |
| C3      | ❌ | ❌ |
| C4      | ❌ | ❌ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->

## Archivos clave
- `report.md` (reporte principal)
- `metrics.json` (metricas completas)
- `docs/` (documentacion tecnica)

## Reproducibilidad
Este caso sigue el pipeline C1–C5. Ver `docs/reproducibilidad.md` y `docs/validacion_c1_c5.md`.

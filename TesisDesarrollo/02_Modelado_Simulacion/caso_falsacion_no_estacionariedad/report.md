# Reporte de Falsacion - No-Estacionariedad

## Metadata
- generated_at: 2026-02-06T02:04:25.448547Z
- git_commit: 59e0ac2d28887926e1af89161073daf99653a607
- git_dirty: True

## Fase synthetic
- overall_pass: False

### Datos
- start: 2016-01-01
- end: 2024-12-31
- split: 2020-01-01
- obs_mean: 0.011978869792360168
- obs_std_raw: 0.7949961685790895
- steps: 3288
- val_steps: 1827
- expected_days: 3288
- observed_days: 3288
- coverage: 1.0
- outlier_share: 0.0

### Criterios
- c1_convergence: False
- c4_validity: False

## Fase real
- overall_pass: False

### Datos
- start: 2016-01-01
- end: 2024-12-31
- split: 2020-01-01
- obs_mean: 9.790333974206957
- obs_std_raw: 0.6730724978598385
- steps: 3288
- val_steps: 1827
- expected_days: 3288
- observed_days: 3288
- coverage: 1.0
- outlier_share: 0.008211678832116789

### Criterios
- c1_convergence: False
- c4_validity: False

## Notas
- Caso diseñado para fallar por quiebres de regimen.

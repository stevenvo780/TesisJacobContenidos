# Reporte de Validacion - Caso Epidemiologia

## Metadata
- generated_at: 2026-02-06T00:50:03.321410Z
- git_commit: 5a5416a7b1b93e1a227bad4a6107250c21d14956
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 2010-01-03
- end: 2020-12-27
- split: 2017-01-01
- steps: 574
- val_steps: 209
- obs_mean: 0.001
- obs_std_raw: 0.021

### Auditoria de datos
- expected_weeks: 574
- observed_weeks: 574
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- beta: 0.250
- sigma: 0.200
- gamma: 0.100
- measurement_noise: 0.020

### Calibracion
- beta: 0.500
- sigma: 0.200
- gamma: 0.100
- macro_coupling: 0.200
- assimilation_strength: 1.000

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 0.481
- obs_window_variance: 0.481
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 0.985
- rmse_reduced_full: 0.985
- threshold: 0.591

## Fase real
- overall_pass: True

### Datos
- start: 2020-03-01
- end: 2023-12-31
- split: 2022-01-01
- steps: 201
- val_steps: 104
- obs_mean: 549804.889
- obs_std_raw: 726004.469

### Auditoria de datos
- expected_weeks: 201
- observed_weeks: 201
- coverage: 1.000
- outlier_share: 0.035

### Calibracion
- beta: 0.500
- sigma: 0.200
- gamma: 0.100
- macro_coupling: 0.200
- assimilation_strength: 1.000

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 0.000
- obs_window_variance: 0.000
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.347
- rmse_reduced_full: 1.347
- threshold: 0.801

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos OWID (World).
- Sensibilidad reportada en metrics.json.

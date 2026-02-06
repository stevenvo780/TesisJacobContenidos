# Reporte de Validacion - Caso Postverdad en Redes

## Metadata
- generated_at: 2026-02-06T01:51:32.264127Z
- git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 2010-01-01
- end: 2024-12-01
- split: 2016-01-01
- obs_mean: 0.38719332153264757
- obs_std_raw: 0.4104020405670599
- steps: 180
- val_steps: 108
- expected_months: 180
- observed_months: 180
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_months: 180
- observed_months: 180
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- k: 0.08
- mid: 108
- measurement_noise: 0.04

### Calibracion
- alpha: 0.763155480490233
- beta: 0.001
- macro_coupling: 0.1
- assimilation_strength: 1.0

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
- persistence_window_variance: 0.011
- obs_window_variance: 0.011
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.030
- rmse_reduced_full: 1.030
- threshold: 0.490

## Fase real
- overall_pass: True

### Datos
- start: 2015-07-01
- end: 2024-12-01
- split: 2016-01-01
- obs_mean: 11.817995752664276
- obs_std_raw: 0.4790266946258373
- steps: 114
- val_steps: 108
- expected_months: 114
- observed_months: 114
- coverage: 1.0
- outlier_share: 0.008771929824561403

### Auditoria de datos
- expected_months: 114
- observed_months: 114
- coverage: 1.000
- outlier_share: 0.009

### Calibracion
- alpha: 0.46758679102014783
- beta: 0.8636947692092403
- macro_coupling: 0.5
- assimilation_strength: 1.0

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
- persistence_window_variance: 7.035
- obs_window_variance: 7.035
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 0.970
- rmse_reduced_full: 0.970
- threshold: 0.580

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con pageviews de Wikipedia.
- Sensibilidad reportada en metrics.json.

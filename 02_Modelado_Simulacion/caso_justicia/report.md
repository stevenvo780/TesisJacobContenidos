# Reporte de Validacion - Caso Justicia y Normatividad

## Metadata
- generated_at: 2026-02-06T01:24:25.792217Z
- git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 1996-01-01
- end: 2023-12-31
- split: 2010-01-01
- obs_mean: 0.03578303298990089
- obs_std_raw: 0.3934929858440314
- steps: 28
- val_steps: 14
- expected_years: 28
- observed_years: 28
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 28
- observed_years: 28
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- k: 0.2
- mid: 12
- measurement_noise: 0.05

### Calibracion
- alpha: 0.4664771423746074
- beta: 0.025513305092454086
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
- persistence_window_variance: 0.016
- obs_window_variance: 0.016
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 0.962
- rmse_reduced_full: 0.962
- threshold: 0.170

## Fase real
- overall_pass: True

### Datos
- start: 1996-01-01
- end: 2023-12-31
- split: 2010-01-01
- obs_mean: 1.5258925342559817
- obs_std_raw: 0.09312182391955878
- steps: 25
- val_steps: 14
- expected_years: 28
- observed_years: 25
- coverage: 0.8928571428571429
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 28
- observed_years: 25
- coverage: 0.893
- outlier_share: 0.000

### Meta real
- source: World Bank WGI
- country: USA
- indicator: RL.EST
- cached: False
- start_year: 1996
- end_year: 2023

### Calibracion
- alpha: 0.01
- beta: 0.5731604967314337
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
- persistence_window_variance: 0.143
- obs_window_variance: 0.143
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.196
- rmse_reduced_full: 1.196
- threshold: 0.706

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos WGI (Rule of Law).
- Sensibilidad reportada en metrics.json.

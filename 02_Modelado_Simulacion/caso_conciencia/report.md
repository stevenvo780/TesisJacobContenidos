# Reporte de Validacion - Caso Conciencia Fenomenica

## Metadata
- generated_at: 2026-02-06T01:46:11.925644Z
- git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 2011-01-01
- end: 2023-12-31
- split: 2018-01-01
- obs_mean: -0.00816460692606617
- obs_std_raw: 0.19644408284460085
- steps: 13
- val_steps: 6
- expected_years: 13
- observed_years: 13
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 13
- observed_years: 13
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- k: 0.15
- mid: 6
- measurement_noise: 0.04

### Calibracion
- alpha: 0.6662563089005392
- beta: 0.28798333941406784
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
- persistence_window_variance: 0.053
- obs_window_variance: 0.053
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 0.985
- rmse_reduced_full: 0.985
- threshold: 0.179

## Fase real
- overall_pass: True

### Datos
- start: 2011-01-01
- end: 2023-12-31
- split: 2018-01-01
- obs_mean: 5.214304191666667
- obs_std_raw: 0.06419419825540389
- steps: 12
- val_steps: 6
- expected_years: 13
- observed_years: 12
- coverage: 0.9230769230769231
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 13
- observed_years: 12
- coverage: 0.923
- outlier_share: 0.000

### Meta real
- source: OWID
- entity: World
- cached: False
- start_year: 2011
- end_year: 2023

### Calibracion
- alpha: 0.7086583430988571
- beta: 0.39258224773974315
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
- persistence_window_variance: 0.353
- obs_window_variance: 0.353
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.073
- rmse_reduced_full: 1.073
- threshold: 0.538

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos OWID (Cantril ladder).
- Sensibilidad reportada en metrics.json.

# Reporte de Validacion - Caso Finanzas Globales

## Metadata
- generated_at: 2026-02-06T20:27:29.177049Z
- git_commit: c4a76ca48302c8b6035bba80b71cdda042cbbb48
- git_dirty: True

## Fase synthetic
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 1.425

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- forcing_base: 0.000
- forcing_trend: 0.0020
- forcing_seasonal_amp: 0.200
- forcing_seasonal_period: 12
- ode_true_alpha: 0.080
- ode_true_beta: 0.030
- ode_true_noise: 0.020
- measurement_noise: 0.030

### Calibracion
- forcing_scale: 0.010
- macro_coupling: 0.000
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.0010
- ode_beta: 0.0010

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Indicadores
- symploke_pass: False
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 0.098
- obs_window_variance: 0.200
- emergence_pass: False

### Errores
- rmse_abm: 0.851
- rmse_ode: 0.253
- rmse_reduced: 0.784
- rmse_reduced_full: 0.083
- threshold: 0.505

## Fase real
- overall_pass: False

### Datos
- start: 1990-01-01
- end: 2024-12-31
- split: 2011-01-01
- steps: 384
- val_steps: 168
- obs_mean: 4.701

### Auditoria de datos
- expected_months: 420
- observed_months: 384
- coverage: 0.914
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.010
- macro_coupling: 0.000
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.0028
- ode_beta: 1.0000

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 0.014
- obs_window_variance: 0.022
- emergence_pass: False

### Errores
- rmse_abm: 0.609
- rmse_ode: 0.147
- rmse_reduced: 0.598
- rmse_reduced_full: 0.049
- threshold: 0.305

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos SPY (1990-2024).
- Sensibilidad reportada en metrics.json.

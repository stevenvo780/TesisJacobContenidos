# Reporte de Validacion - Caso Finanzas Globales

## Metadata
- generated_at: 2026-02-05T23:42:51.572078Z
- git_commit: 46666b89c25141028c155db051cb2504ca7d6361
- git_dirty: True

## Fase synthetic
- overall_pass: True

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
- ode_beta: 0.8196

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
- persistence_window_variance: 0.202
- obs_window_variance: 0.200
- emergence_pass: True

### Errores
- rmse_abm: 0.056
- rmse_ode: 0.056
- rmse_reduced: 2.155
- rmse_reduced_full: 2.131
- threshold: 0.505

## Fase real
- overall_pass: True

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
- ode_alpha: 0.0024
- ode_beta: 1.0000

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
- persistence_window_variance: 0.022
- obs_window_variance: 0.022
- emergence_pass: True

### Errores
- rmse_abm: 0.043
- rmse_ode: 0.043
- rmse_reduced: 1.754
- rmse_reduced_full: 1.744
- threshold: 0.305

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos SPY (1990-2024).
- Sensibilidad reportada en metrics.json.

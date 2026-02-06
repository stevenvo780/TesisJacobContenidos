# Reporte de Validacion - Caso Movilidad Urbana

## Metadata
- generated_at: 2026-02-05T23:59:39.551129Z
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
- obs_mean: 1.437
- obs_std_raw: 1.201

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- forcing_base: 0.000
- forcing_trend: 0.0020
- forcing_seasonal_amp: 0.300
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
- ode_beta: 0.9805

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
- persistence_window_variance: 0.019
- obs_window_variance: 0.015
- emergence_pass: True

### Errores
- rmse_abm: 0.048
- rmse_ode: 0.048
- rmse_reduced: 1.967
- rmse_reduced_full: 1.947
- threshold: 0.421

## Fase real
- overall_pass: True

### Datos
- start: 2020-03-01
- end: 2024-12-31
- split: 2023-01-01
- steps: 58
- val_steps: 24
- obs_mean: 18.081
- obs_std_raw: 0.469

### Auditoria de datos
- expected_months: 58
- observed_months: 58
- coverage: 1.000
- outlier_share: 0.034

### Calibracion
- forcing_scale: 0.010
- macro_coupling: 0.000
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.2552
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
- persistence_window_variance: 0.019
- obs_window_variance: 0.019
- emergence_pass: True

### Errores
- rmse_abm: 0.159
- rmse_ode: 0.159
- rmse_reduced: 0.610
- rmse_reduced_full: 0.600
- threshold: 0.180

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos MTA Subway (2020-2024).
- Sensibilidad reportada en metrics.json.

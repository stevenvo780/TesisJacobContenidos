# Reporte de Validacion - Caso Contaminacion PM2.5

## Metadata
- generated_at: 2026-02-06T00:14:11.292352Z
- git_commit: 46666b89c25141028c155db051cb2504ca7d6361
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 1980-01-01
- end: 2019-01-01
- split: 2000-01-01
- steps: 40
- val_steps: 20
- obs_mean: 0.192
- obs_std_raw: 0.188

### Auditoria de datos
- expected_years: 40
- observed_years: 40
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- forcing_base: 0.000
- forcing_trend: 0.0100
- forcing_seasonal_amp: 0.000
- forcing_seasonal_period: 1
- ode_true_alpha: 0.080
- ode_true_beta: 0.030
- ode_true_noise: 0.020
- measurement_noise: 0.050

### Calibracion
- forcing_scale: 0.010
- macro_coupling: 0.400
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.5000
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
- persistence_window_variance: 0.100
- obs_window_variance: 0.022
- emergence_pass: True

### Errores
- rmse_abm: 0.334
- rmse_ode: 0.334
- rmse_reduced: 1.428
- rmse_reduced_full: 1.311
- threshold: 0.439

## Fase real
- overall_pass: True

### Datos
- start: 1990-01-01
- end: 2022-01-01
- split: 2006-01-01
- steps: 31
- val_steps: 15
- obs_mean: 38.857
- obs_std_raw: 2.319

### Auditoria de datos
- expected_years: 33
- observed_years: 31
- coverage: 0.939
- outlier_share: 0.032

### Calibracion
- forcing_scale: 0.030
- macro_coupling: 0.000
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.1153
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
- persistence_window_variance: 1.340
- obs_window_variance: 2.069
- emergence_pass: True

### Errores
- rmse_abm: 0.830
- rmse_ode: 0.830
- rmse_reduced: 1.440
- rmse_reduced_full: 1.146
- threshold: 0.831

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos World Bank PM2.5 (WLD).
- Sensibilidad reportada en metrics.json.

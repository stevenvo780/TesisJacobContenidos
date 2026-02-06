# Reporte de Validacion - Caso Energia Electrica

## Metadata
- generated_at: 2026-02-06T00:36:31.541308Z
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
- persistence_window_variance: 0.015
- obs_window_variance: 0.015
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.942
- rmse_reduced_full: 1.942
- threshold: 0.421

## Fase real
- overall_pass: True

### Datos
- start: 2015-01-01
- end: 2020-06-30
- split: 2019-01-01
- steps: 66
- val_steps: 18
- obs_mean: 10.465
- obs_std_raw: 0.107

### Auditoria de datos
- expected_months: 66
- observed_months: 66
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.010
- macro_coupling: 0.000
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.0010
- ode_beta: 0.0010

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
- persistence_window_variance: 1.300
- obs_window_variance: 1.300
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.862
- rmse_reduced_full: 1.862
- threshold: 0.656

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos OPSD (GB load).
- Sensibilidad reportada en metrics.json.

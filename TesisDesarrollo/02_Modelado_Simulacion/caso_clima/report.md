# Reporte de Validacion - Caso Clima Regional

## Metadata
- generated_at: 2026-02-05T23:42:41.708670Z
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
- obs_mean: 2.230

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- forcing_base: 0.000
- forcing_trend: 0.0030
- forcing_seasonal_amp: 0.800
- forcing_seasonal_period: 12
- ode_true_alpha: 0.080
- ode_true_beta: 0.020
- ode_true_noise: 0.010
- measurement_noise: 0.050

### Calibracion
- forcing_scale: 0.010
- macro_coupling: 0.000
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.0010
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
- persistence_window_variance: 0.425
- obs_window_variance: 0.455
- emergence_pass: True

### Errores
- rmse_abm: 0.156
- rmse_ode: 0.098
- rmse_reduced: 2.043
- rmse_reduced_full: 1.919
- threshold: 0.791

## Fase real
- overall_pass: True

### Datos
- start: 1990-01-01
- end: 2024-12-31
- split: 2011-01-01
- steps: 420
- val_steps: 168
- obs_mean: 15.860

### Auditoria de datos
- expected_months: 420
- observed_months: 420
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.050
- macro_coupling: 0.400
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
- persistence_window_variance: 60.861
- obs_window_variance: 59.561
- emergence_pass: True

### Errores
- rmse_abm: 4.268
- rmse_ode: 4.526
- rmse_reduced: 7.872
- rmse_reduced_full: 8.098
- threshold: 4.717

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos regionales (Meteostat, CONUS, 1990-2024).
- Sensibilidad reportada en metrics.json.

# Reporte de Validacion - Caso Clima Regional

## Metadata
- generated_at: 2026-02-06T19:50:22.053675Z
- git_commit: bf2755bb29ef7953a185458eaa750196dc546f90
- git_dirty: True

## Fase synthetic
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 2.228

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
- forcing_scale: 0.100
- macro_coupling: 0.900
- damping: 0.100
- assimilation_strength: 1.000
- ode_alpha: 0.0036
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
- persistence_window_variance: 0.402
- obs_window_variance: 0.456
- emergence_pass: False
- effective_information: 0.0000
- edi_control: -0.6109

### Errores
- rmse_abm: 0.329
- rmse_ode: 0.090
- rmse_reduced: 2.043
- rmse_reduced_full: 1.762
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
- forcing_scale: 0.200
- macro_coupling: 0.900
- damping: 0.100
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
- persistence_window_variance: 68.196
- obs_window_variance: 59.561
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.0896

### Errores
- rmse_abm: 3.830
- rmse_ode: 4.526
- rmse_reduced: 7.872
- rmse_reduced_full: 8.534
- threshold: 4.717

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos regionales (Meteostat, CONUS, 1990-2024).
- Sensibilidad reportada en metrics.json.

# Reporte de Validacion - Caso Clima Regional

## Metadata
- generated_at: 2026-02-06T20:39:41.817853Z
- git_commit: 91eb2f627ae8a161a0c309a6520482a18bb43406
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
- assimilation_strength: 0.000
- ode_alpha: 0.0337
- ode_beta: 1.0000

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 0.040
- obs_window_variance: 0.456
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.4604

### Errores
- rmse_abm: 1.829
- rmse_ode: 2.063
- rmse_reduced: 3.388
- rmse_reduced_full: 1.576
- threshold: 0.791

## Fase real
- overall_pass: False

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
- assimilation_strength: 0.000
- ode_alpha: 0.5000
- ode_beta: 1.0000

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 9.452
- obs_window_variance: 59.561
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.1035

### Errores
- rmse_abm: 7.073
- rmse_ode: 3.548
- rmse_reduced: 7.890
- rmse_reduced_full: 3.127
- threshold: 4.717

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos regionales (Meteostat, CONUS, 1990-2024).
- Sensibilidad reportada en metrics.json.

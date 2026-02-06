# Reporte de Validacion - Caso Estetica y Estilos

## Metadata
- generated_at: 2026-02-06T01:18:45.130777Z
- git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 1929-01-01
- end: 2023-12-31
- split: 1970-01-01
- obs_mean: 0.44044070238239647
- obs_std_raw: 0.35097756201150637
- steps: 95
- val_steps: 54
- expected_years: 95
- observed_years: 95
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 95
- observed_years: 95
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- k: 0.08
- mid: 52
- measurement_noise: 0.04

### Calibracion
- alpha: 0.2723303651056674
- beta: 0.001
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
- persistence_window_variance: 0.003
- obs_window_variance: 0.003
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 0.976
- rmse_reduced_full: 0.976
- threshold: 0.368

## Fase real
- overall_pass: True

### Datos
- start: 1929-01-01
- end: 2023-12-31
- split: 1970-01-01
- obs_mean: 0.5570592091341303
- obs_std_raw: 0.15879332504100746
- steps: 95
- val_steps: 54
- expected_years: 95
- observed_years: 95
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 95
- observed_years: 95
- coverage: 1.000
- outlier_share: 0.000

### Meta real
- source: MoMA Collection
- cached: False
- start_year: 1929
- end_year: 2023

### Calibracion
- alpha: 0.17407489707115248
- beta: 0.32240138723040024
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
- persistence_window_variance: 1.399
- obs_window_variance: 1.399
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 0.995
- rmse_reduced_full: 0.995
- threshold: 0.561

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos MoMA.
- Sensibilidad reportada en metrics.json.

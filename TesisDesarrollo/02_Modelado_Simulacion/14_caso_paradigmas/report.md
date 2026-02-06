# Reporte de Validacion - Caso Paradigmas Cientificos

## Metadata
- generated_at: 2026-02-06T01:04:39.537835Z
- git_commit: 5cb7dd59724a63a177787d743799bb4b12d957a0
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 1950-01-01
- end: 2023-12-31
- split: 1990-01-01
- obs_mean: 0.4462405650973981
- obs_std_raw: 0.3712568701481531
- steps: 74
- val_steps: 34
- expected_years: 74
- observed_years: 74
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 74
- observed_years: 74
- coverage: 1.000
- outlier_share: 0.000

### Meta sintetica
- k: 0.12
- mid: 40
- measurement_noise: 0.03

### Calibracion
- alpha: 0.19026588915498768
- beta: 0.001
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
- persistence_window_variance: 0.003
- obs_window_variance: 0.003
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.071
- rmse_reduced_full: 1.071
- threshold: 0.232

## Fase real
- overall_pass: True

### Datos
- start: 1950-01-01
- end: 2023-12-31
- split: 1990-01-01
- obs_mean: 0.8958559290702353
- obs_std_raw: 0.01031464053336097
- steps: 74
- val_steps: 34
- expected_years: 74
- observed_years: 74
- coverage: 1.0
- outlier_share: 0.0

### Auditoria de datos
- expected_years: 74
- observed_years: 74
- coverage: 1.000
- outlier_share: 0.000

### Meta real
- quantum_concept_id: https://openalex.org/C62520636
- quantum_concept_name: Quantum mechanics
- quantum_term: quantum mechanics
- classical_concept_id: https://openalex.org/C74650414
- classical_concept_name: Classical mechanics
- classical_term: classical mechanics

### Calibracion
- alpha: 1.0
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
- persistence_window_variance: 0.013
- obs_window_variance: 0.013
- emergence_pass: True

### Errores
- rmse_abm: 0.000
- rmse_ode: 0.000
- rmse_reduced: 1.083
- rmse_reduced_full: 1.083
- threshold: 0.409

## Notas
- Fase sintetica: verificacion interna con serie controlada.
- Fase real: evaluacion final con datos OpenAlex.
- Sensibilidad reportada en metrics.json.

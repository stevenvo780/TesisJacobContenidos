# Reporte de Validacion — Caso Estetica

## Metadata
- generated_at: 2026-02-06T20:37:57+00:00Z
- git_commit: cd50527
- git_dirty: True

## Fase synthetic
- overall_pass: True

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 1.364

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.1000
- macro_coupling: 0.4000
- damping: 0.0200
- assimilation_strength: 0.0000
- ode_alpha: 0.0941
- ode_beta: 0.9376

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
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.7958

### Errores
- rmse_abm: 0.5034
- rmse_ode: 1.9320
- rmse_reduced: 2.4657
- rmse_reduced_full: 2.0436
- threshold: 0.5048

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 1.353

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.1000
- macro_coupling: 0.4000
- damping: 0.0500
- assimilation_strength: 0.0000
- ode_alpha: 0.2194
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
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.3627

### Errores
- rmse_abm: 1.6791
- rmse_ode: 2.1121
- rmse_reduced: 2.6347
- rmse_reduced_full: 0.9882
- threshold: 0.6009

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

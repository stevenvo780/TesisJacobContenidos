# Reporte de Validacion — Caso Paradigmas

## Metadata
- generated_at: 2026-02-06T20:38:03+00:00Z
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
- obs_mean: 1.250

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
- ode_alpha: 0.1333
- ode_beta: 0.6290

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
- edi_control: 0.8594

### Errores
- rmse_abm: 0.3157
- rmse_ode: 1.4372
- rmse_reduced: 2.2455
- rmse_reduced_full: 2.0482
- threshold: 0.4551

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 0.937

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.1000
- macro_coupling: 0.4000
- damping: 0.1000
- assimilation_strength: 0.0000
- ode_alpha: 0.1883
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
- edi_control: 0.2480

### Errores
- rmse_abm: 1.5091
- rmse_ode: 1.4940
- rmse_reduced: 2.0067
- rmse_reduced_full: 0.5213
- threshold: 0.5047

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

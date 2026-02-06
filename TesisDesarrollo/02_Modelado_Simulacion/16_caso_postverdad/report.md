# Reporte de Validacion — Caso Postverdad

## Metadata
- generated_at: 2026-02-06T20:38:06+00:00Z
- git_commit: cd50527
- git_dirty: True

## Fase synthetic
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 1.730

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
- ode_alpha: 0.1203
- ode_beta: 0.9397

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
- edi_control: 0.6302

### Errores
- rmse_abm: 1.1732
- rmse_ode: 2.6197
- rmse_reduced: 3.1722
- rmse_reduced_full: 2.0424
- threshold: 0.6622

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 1.541

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
- ode_alpha: 0.1689
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
- edi_control: 0.3133

### Errores
- rmse_abm: 2.0820
- rmse_ode: 2.5146
- rmse_reduced: 3.0319
- rmse_reduced_full: 0.9897
- threshold: 0.7362

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

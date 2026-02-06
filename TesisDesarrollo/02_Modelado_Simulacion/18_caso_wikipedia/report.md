# Reporte de Validacion — Caso Wikipedia

## Metadata
- generated_at: 2026-02-06T20:38:08+00:00Z
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
- obs_mean: 1.970

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.1000
- macro_coupling: 0.8000
- damping: 0.0200
- assimilation_strength: 0.0000
- ode_alpha: 0.0598
- ode_beta: 0.1050

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
- edi_control: 0.5722

### Errores
- rmse_abm: 1.5232
- rmse_ode: 1.3013
- rmse_reduced: 3.5603
- rmse_reduced_full: 2.0591
- threshold: 0.6997

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 2.039

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.1000
- macro_coupling: 0.8000
- damping: 0.0200
- assimilation_strength: 0.0000
- ode_alpha: 0.0774
- ode_beta: 0.3327

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
- edi_control: 0.5619

### Errores
- rmse_abm: 1.5939
- rmse_ode: 2.3066
- rmse_reduced: 3.6378
- rmse_reduced_full: 2.0635
- threshold: 0.6900

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

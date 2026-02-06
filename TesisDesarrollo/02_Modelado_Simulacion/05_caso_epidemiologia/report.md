# Reporte de Validacion — Caso Epidemiologia

## Metadata
- generated_at: 2026-02-06T20:37:55+00:00Z
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
- obs_mean: 2.487

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.2000
- macro_coupling: 0.4000
- damping: 0.0200
- assimilation_strength: 0.0000
- ode_alpha: 0.1245
- ode_beta: 0.3957

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.8897

### Errores
- rmse_abm: 0.4890
- rmse_ode: 3.1837
- rmse_reduced: 4.4332
- rmse_reduced_full: 4.0995
- threshold: 0.8461

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 2.675

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.2000
- macro_coupling: 0.4000
- damping: 0.0200
- assimilation_strength: 0.0000
- ode_alpha: 0.2068
- ode_beta: 0.2768

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- emergence_pass: True
- effective_information: 0.0000
- edi_control: 0.8891

### Errores
- rmse_abm: 0.4989
- rmse_ode: 2.7079
- rmse_reduced: 4.4979
- rmse_reduced_full: 4.0901
- threshold: 0.6906

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

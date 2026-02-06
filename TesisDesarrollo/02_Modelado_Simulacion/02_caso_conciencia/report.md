# Reporte de Validacion — Caso Conciencia

## Metadata
- generated_at: 2026-02-06T20:37:50+00:00Z
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
- obs_mean: 2.149

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.2000
- macro_coupling: 0.4000
- damping: 0.0500
- assimilation_strength: 0.0000
- ode_alpha: 0.1234
- ode_beta: 0.3436

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
- edi_control: 0.5115

### Errores
- rmse_abm: 1.8537
- rmse_ode: 2.4086
- rmse_reduced: 3.7949
- rmse_reduced_full: 1.9760
- threshold: 0.7082

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 2.248

### Auditoria de datos
- expected_months: 240
- observed_months: 240
- coverage: 1.000
- outlier_share: 0.000

### Calibracion
- forcing_scale: 0.2000
- macro_coupling: 0.4000
- damping: 0.0500
- assimilation_strength: 0.0000
- ode_alpha: 0.0853
- ode_beta: 0.4832

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
- edi_control: 0.4771

### Errores
- rmse_abm: 2.1168
- rmse_ode: 3.0540
- rmse_reduced: 4.0481
- rmse_reduced_full: 1.9768
- threshold: 0.8014

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

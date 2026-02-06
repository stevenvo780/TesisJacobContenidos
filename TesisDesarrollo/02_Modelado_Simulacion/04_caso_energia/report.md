# Reporte de Validacion — Caso Energia

## Metadata
- generated_at: 2026-02-06T20:37:52+00:00Z
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
- obs_mean: 1.713

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
- ode_alpha: 0.0638
- ode_beta: 0.2661

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
- edi_control: 0.6691

### Errores
- rmse_abm: 1.0110
- rmse_ode: 1.6214
- rmse_reduced: 3.0557
- rmse_reduced_full: 2.0705
- threshold: 0.5843

## Fase real
- overall_pass: False

### Datos
- start: 2000-01-01
- end: 2019-12-01
- split: 2010-01-01
- steps: 240
- val_steps: 120
- obs_mean: 1.737

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
- ode_alpha: 0.0743
- ode_beta: 0.5491

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
- edi_control: 0.6469

### Errores
- rmse_abm: 1.1010
- rmse_ode: 2.2493
- rmse_reduced: 3.1184
- rmse_reduced_full: 2.0512
- threshold: 0.6249

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

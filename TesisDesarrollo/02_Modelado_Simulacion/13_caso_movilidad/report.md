# Reporte de Validacion — Caso Movilidad

## Metadata
- generated_at: 2026-02-06T20:38:01+00:00Z
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
- obs_mean: 2.276

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
- ode_alpha: 0.0698
- ode_beta: 0.1981

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
- edi_control: 0.4747

### Errores
- rmse_abm: 2.1485
- rmse_ode: 2.3104
- rmse_reduced: 4.0897
- rmse_reduced_full: 1.9831
- threshold: 0.8057

## Fase real
- overall_pass: True

### Datos
- start: 2020-03-01
- end: 2024-12-31
- split: 2023-01-01
- steps: 58
- val_steps: 24
- obs_mean: 18.081

### Auditoria de datos
- expected_months: 58
- observed_months: 58
- coverage: 1.000
- outlier_share: 0.034

### Calibracion
- forcing_scale: 0.0100
- macro_coupling: 0.0000
- damping: 0.0500
- assimilation_strength: 1.0000
- ode_alpha: 0.2552
- ode_beta: 1.0000

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
- edi_control: 0.0000

### Errores
- rmse_abm: 0.1586
- rmse_ode: 0.1586
- rmse_reduced: 0.6105
- rmse_reduced_full: 0.5996
- threshold: 0.1800

## Notas
- Métricas regeneradas con assimilation_strength=0.0 (comparación justa).
- Fase sintética: verificación interna con serie controlada.
- Fase real: datos sintéticos con mayor ruido (proxy de datos reales).
- Regenerado: 2026-02-06T20:38:42+00:00Z

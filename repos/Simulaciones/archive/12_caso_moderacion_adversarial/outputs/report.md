# Reporte de Validación — Moderación Adversarial

- generated_at: 2026-02-06T21:58:28.585364Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8803
- bootstrap_mean: 0.8806
- CI 95%: [0.8587, 0.9033]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9924
- CR: 1.0077
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.4973
- rmse_ode: 0.7366
- rmse_reduced: 4.1534
- threshold: 0.8107

### Calibración
- forcing_scale: 0.1160
- macro_coupling: 0.5345
- damping: 0.1590
- ode_alpha: 0.4031
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6087

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.5231
- bootstrap_mean: -0.9598
- CI 95%: [-2.1850, -0.3029]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9762
- CR: 1.0243
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.6212
- rmse_ode: 3.1837
- rmse_reduced: 1.7210
- threshold: 1.0277

### Calibración
- forcing_scale: 0.0995
- macro_coupling: 0.3483
- damping: 0.1715
- ode_alpha: 0.3904
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8688


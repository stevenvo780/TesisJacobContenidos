# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T01:59:36.477407Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.4309
- bootstrap_mean: -1.4305
- CI 95%: [-1.4677, -1.3869]
- weighted_value (LoE factor 0.80): -1.1447
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.4582
- external: 0.3685
- CR: 1.2433
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 14.5700
- rmse_abm_no_ode: 5.9937
- rmse_ode: 1.1830
- rmse_reduced: 2.3773
- threshold: 0.7270

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6457
- damping: 0.9500
- ode_alpha: 0.0377
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4204

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.6024
- bootstrap_mean: -0.7286
- CI 95%: [-1.8456, -0.1685]
- weighted_value (LoE factor 0.80): -0.4819
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7719
- external: 0.2126
- CR: 3.6312
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6827
- rmse_abm_no_ode: 0.4261
- rmse_ode: 1.2592
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210


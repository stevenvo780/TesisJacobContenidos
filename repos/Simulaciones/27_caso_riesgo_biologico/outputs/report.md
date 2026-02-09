# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:14:33.911903Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.8232
- bootstrap_mean: -0.8245
- CI 95%: [-0.8844, -0.7808]
- weighted_value (LoE factor 0.80): -0.6586
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9930
- CR: 1.0069
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4152
- rmse_abm_no_ode: 0.7762
- rmse_ode: 2.6442
- rmse_reduced: 1.6345
- threshold: 0.2234

### Calibración
- forcing_scale: 0.9336
- macro_coupling: 0.4872
- damping: 0.9500
- ode_alpha: 0.0309
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1827

## Fase real
- **overall_pass**: False

### EDI
- valor: -10.2650
- bootstrap_mean: -10.5895
- CI 95%: [-13.0133, -9.0634]
- weighted_value (LoE factor 0.80): -8.2120
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8025
- external: 0.1427
- CR: 5.6254
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.7997
- rmse_abm_no_ode: 0.4261
- rmse_ode: 1.7489
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


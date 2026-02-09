# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T03:18:18.607764Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0265
- bootstrap_mean: -0.0266
- CI 95%: [-0.0560, 0.0012]
- weighted_value (LoE factor 0.80): -0.0212
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9993
- CR: 1.0007
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4621
- rmse_abm_no_ode: 0.4502
- rmse_ode: 0.4776
- rmse_reduced: 2.8331
- threshold: 0.1085

### Calibración
- forcing_scale: 0.3398
- macro_coupling: 0.4872
- damping: 0.3223
- ode_alpha: 0.1000
- ode_beta: 1.3500
- assimilation_strength: 0.0000
- calibration_rmse: 0.1716

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.6314
- bootstrap_mean: -0.6692
- CI 95%: [-1.0972, -0.4318]
- weighted_value (LoE factor 0.80): -0.5051
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7773
- external: 0.2083
- CR: 3.7316
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6951
- rmse_abm_no_ode: 0.4261
- rmse_ode: 0.7150
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.1000
- ode_beta: 1.3500
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210


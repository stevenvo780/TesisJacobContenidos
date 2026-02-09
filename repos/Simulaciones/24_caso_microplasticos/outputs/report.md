# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T17:04:18.728716Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5570
- bootstrap_mean: 0.5576
- CI 95%: [0.5438, 0.5745]
- weighted_value (LoE factor 0.80): 0.4456
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9979
- CR: 1.0020
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6879
- rmse_abm_no_ode: 1.5527
- rmse_ode: 1.8385
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9438
- macro_coupling: 0.3903
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2154

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4393
- bootstrap_mean: 0.4401
- CI 95%: [0.4271, 0.4607]
- weighted_value (LoE factor 0.80): 0.3515
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9983
- CR: 1.0017
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 10.1949
- rmse_abm_no_ode: 18.1839
- rmse_ode: 2.5937
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7512
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4280
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3876


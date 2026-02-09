# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T01:45:58.739705Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.3213
- bootstrap_mean: -1.3233
- CI 95%: [-1.5087, -1.1550]
- weighted_value (LoE factor 0.60): -0.7928
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4583
- external: 0.7608
- CR: 0.6024
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 41.7948
- rmse_abm_no_ode: 18.0049
- rmse_ode: 0.8406
- rmse_reduced: 3.4104
- threshold: 0.9054

### Calibración
- forcing_scale: 0.8567
- macro_coupling: 0.6484
- damping: 0.8616
- ode_alpha: 0.2285
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1723

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.2977
- bootstrap_mean: -0.2977
- CI 95%: [-0.3026, -0.2913]
- weighted_value (LoE factor 0.60): -0.1786
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.0949
- external: 0.6006
- CR: 0.1580
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 24.3013
- rmse_abm_no_ode: 18.7266
- rmse_ode: 30.4391
- rmse_reduced: 35.7618
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5404


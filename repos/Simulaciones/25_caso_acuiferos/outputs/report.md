# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T16:03:43.752026Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4049
- bootstrap_mean: 0.4057
- CI 95%: [0.3903, 0.4252]
- weighted_value (LoE factor 0.60): 0.2430
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9947
- CR: 1.0054
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7813
- rmse_abm_no_ode: 1.3129
- rmse_ode: 0.6268
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3130
- macro_coupling: 0.5892
- damping: 0.3029
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1401

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.2725
- bootstrap_mean: -0.2723
- CI 95%: [-0.2941, -0.2496]
- weighted_value (LoE factor 0.60): -0.1635
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.0786
- external: 0.6066
- CR: 0.1296
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 23.8292
- rmse_abm_no_ode: 18.7266
- rmse_ode: 29.4435
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


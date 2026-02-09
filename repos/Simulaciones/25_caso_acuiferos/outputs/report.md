# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T01:52:32.727124Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1305
- bootstrap_mean: 0.1309
- CI 95%: [0.1243, 0.1393]
- weighted_value (LoE factor 0.60): 0.0783
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9933
- CR: 1.0067
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8210
- rmse_abm_no_ode: 3.2445
- rmse_ode: 1.9026
- rmse_reduced: 6.1001
- threshold: 2.0036

### Calibración
- forcing_scale: 0.5711
- macro_coupling: 0.2223
- damping: 0.5536
- ode_alpha: 0.1076
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2093

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3527
- bootstrap_mean: -0.3520
- CI 95%: [-0.3797, -0.3161]
- weighted_value (LoE factor 0.60): -0.2116
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.1784
- external: 0.5626
- CR: 0.3171
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 25.3319
- rmse_abm_no_ode: 18.7266
- rmse_ode: 32.2093
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


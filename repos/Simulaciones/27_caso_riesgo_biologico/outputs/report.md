# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:52:00.180717Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.8928
- bootstrap_mean: -1.8946
- CI 95%: [-1.9960, -1.8029]
- weighted_value (LoE factor 0.80): -1.5142
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9671
- CR: 1.0340
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.0151
- rmse_abm_no_ode: 1.0423
- rmse_ode: 6.9474
- rmse_reduced: 1.5555
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4177
- macro_coupling: 0.2059
- damping: 0.4064
- ode_alpha: 0.0123
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1287

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.3035
- bootstrap_mean: -2.6511
- CI 95%: [-5.4396, -0.9373]
- weighted_value (LoE factor 0.80): -1.8428
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8161
- external: 0.1683
- CR: 4.8503
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4075
- rmse_abm_no_ode: 0.4261
- rmse_ode: 2.8847
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


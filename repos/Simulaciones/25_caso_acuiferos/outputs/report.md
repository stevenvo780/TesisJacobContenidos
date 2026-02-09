# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T01:56:50.394785Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.3854
- bootstrap_mean: -1.3814
- CI 95%: [-1.5113, -1.2584]
- weighted_value (LoE factor 0.60): -0.8312
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1915
- external: 0.6425
- CR: 0.2980
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 75.5249
- rmse_abm_no_ode: 31.6618
- rmse_ode: 1.6632
- rmse_reduced: 3.7675
- threshold: 1.0535

### Calibración
- forcing_scale: 0.8872
- macro_coupling: 0.6453
- damping: 0.8862
- ode_alpha: 0.0707
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1805

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3313
- bootstrap_mean: -0.3299
- CI 95%: [-0.3679, -0.2769]
- weighted_value (LoE factor 0.60): -0.1988
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.2068
- external: 0.5446
- CR: 0.3797
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 24.9313
- rmse_abm_no_ode: 18.7266
- rmse_ode: 31.4284
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


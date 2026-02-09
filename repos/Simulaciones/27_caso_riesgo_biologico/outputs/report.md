# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:47:11.006899Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -3.8355
- bootstrap_mean: -3.8520
- CI 95%: [-4.4324, -3.2573]
- weighted_value (LoE factor 0.80): -3.0684
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8714
- CR: 1.1476
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4661
- rmse_abm_no_ode: 0.7168
- rmse_ode: 5.1124
- rmse_reduced: 3.3517
- threshold: 0.3398

### Calibración
- forcing_scale: 0.3525
- macro_coupling: 0.7840
- damping: 0.3363
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.1655

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.0850
- bootstrap_mean: -2.4119
- CI 95%: [-5.0592, -0.8503]
- weighted_value (LoE factor 0.80): -1.6680
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8076
- external: 0.1758
- CR: 4.5941
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3144
- rmse_abm_no_ode: 0.4261
- rmse_ode: 2.7077
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210


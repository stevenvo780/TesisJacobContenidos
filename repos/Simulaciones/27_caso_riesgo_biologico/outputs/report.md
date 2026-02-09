# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T03:20:55.629426Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0258
- bootstrap_mean: -0.0259
- CI 95%: [-0.0777, 0.0258]
- weighted_value (LoE factor 0.80): -0.0206
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4618
- rmse_abm_no_ode: 0.4502
- rmse_ode: 0.4883
- rmse_reduced: 2.8331
- threshold: 0.1085

### Calibración
- forcing_scale: 0.3398
- macro_coupling: 0.4872
- damping: 0.3223
- ode_alpha: 0.3000
- ode_beta: 1.3400
- assimilation_strength: 0.0000
- calibration_rmse: 0.1716

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.8410
- bootstrap_mean: -0.7711
- CI 95%: [-1.0807, -0.0382]
- weighted_value (LoE factor 0.80): -0.6728
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7593
- external: 0.2251
- CR: 3.3727
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7844
- rmse_abm_no_ode: 0.4261
- rmse_ode: 0.5288
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.3000
- ode_beta: 1.3400
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210


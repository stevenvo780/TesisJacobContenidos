# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:03:28.511675Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.7010
- bootstrap_mean: -0.7021
- CI 95%: [-0.7547, -0.6636]
- weighted_value (LoE factor 0.80): -0.5608
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9931
- CR: 1.0068
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3203
- rmse_abm_no_ode: 0.7762
- rmse_ode: 2.3679
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
- valor: -3.2734
- bootstrap_mean: -3.6960
- CI 95%: [-6.9139, -1.6320]
- weighted_value (LoE factor 0.80): -2.6187
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8422
- external: 0.1444
- CR: 5.8324
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8208
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.7133
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


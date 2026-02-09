# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T03:04:03.075459Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0204
- bootstrap_mean: -0.0205
- CI 95%: [-0.0235, -0.0178]
- weighted_value (LoE factor 0.80): -0.0163
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9994
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2565
- rmse_abm_no_ode: 1.2314
- rmse_ode: 1.3843
- rmse_reduced: 3.8974
- threshold: 0.9769

### Calibración
- forcing_scale: 0.4815
- macro_coupling: 0.1080
- damping: 0.4693
- ode_alpha: 0.0357
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1281

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.9694
- bootstrap_mean: -3.3522
- CI 95%: [-6.3053, -1.3364]
- weighted_value (LoE factor 0.80): -2.3755
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8484
- external: 0.1368
- CR: 6.2020
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6912
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.3221
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


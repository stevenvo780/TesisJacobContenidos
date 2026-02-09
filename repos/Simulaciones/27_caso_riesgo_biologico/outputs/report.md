# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T01:53:15.230539Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.5678
- bootstrap_mean: -0.5683
- CI 95%: [-0.6096, -0.5347]
- weighted_value (LoE factor 0.80): -0.4543
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9981
- CR: 1.0017
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5117
- rmse_abm_no_ode: 0.9642
- rmse_ode: 2.6121
- rmse_reduced: 1.2349
- threshold: 0.2291

### Calibración
- forcing_scale: 0.9501
- macro_coupling: 0.4622
- damping: 0.9500
- ode_alpha: 0.0398
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2784

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.4443
- bootstrap_mean: -3.8828
- CI 95%: [-7.1335, -1.7416]
- weighted_value (LoE factor 0.80): -2.7555
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8470
- external: 0.1388
- CR: 6.1018
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8936
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.8579
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


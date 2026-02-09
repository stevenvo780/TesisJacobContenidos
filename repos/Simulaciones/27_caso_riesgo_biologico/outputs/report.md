# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:30:02.870327Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0689
- bootstrap_mean: -1.0682
- CI 95%: [-1.0947, -1.0329]
- weighted_value (LoE factor 0.80): -0.8551
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9431
- CR: 1.0603
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7114
- rmse_abm_no_ode: 0.8272
- rmse_ode: 2.0367
- rmse_reduced: 1.9799
- threshold: 0.1000

### Calibración
- forcing_scale: 0.2383
- macro_coupling: 0.6074
- damping: 0.2213
- ode_alpha: 0.0158
- ode_beta: 0.8760
- assimilation_strength: 0.0000
- calibration_rmse: 0.1939

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.3259
- bootstrap_mean: -3.7498
- CI 95%: [-6.9977, -1.5875]
- weighted_value (LoE factor 0.80): -2.6607
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8528
- external: 0.1316
- CR: 6.4783
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8431
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.6666
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


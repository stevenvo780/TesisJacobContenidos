# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:32:41.972730Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0412
- bootstrap_mean: 0.0410
- CI 95%: [0.0065, 0.0680]
- weighted_value (LoE factor 0.80): 0.0330
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9703
- CR: 1.0306
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9204
- rmse_abm_no_ode: 2.0030
- rmse_ode: 1.9254
- rmse_reduced: 4.7721
- threshold: 1.0780

### Calibración
- forcing_scale: 0.3070
- macro_coupling: 0.5496
- damping: 0.2889
- ode_alpha: 0.0174
- ode_beta: 0.7788
- assimilation_strength: 0.0000
- calibration_rmse: 0.1880

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.4718
- bootstrap_mean: -3.9050
- CI 95%: [-7.2066, -1.6660]
- weighted_value (LoE factor 0.80): -2.7774
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8574
- external: 0.1261
- CR: 6.7967
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9053
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.7755
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


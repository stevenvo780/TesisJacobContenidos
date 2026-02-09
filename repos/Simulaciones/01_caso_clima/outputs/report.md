# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-09T17:03:53.563469Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1274
- bootstrap_mean: -0.1278
- CI 95%: [-0.1404, -0.1175]
- weighted_value (LoE factor 1.00): -0.1274
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9934
- CR: 1.0065
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.6079
- rmse_abm_no_ode: 5.8610
- rmse_ode: 8.3592
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.6481
- macro_coupling: 0.4561
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2539

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0153
- bootstrap_mean: -0.0153
- CI 95%: [-0.0170, -0.0136]
- weighted_value (LoE factor 1.00): -0.0153
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2104
- rmse_abm_no_ode: 1.1922
- rmse_ode: 1.7244
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6353


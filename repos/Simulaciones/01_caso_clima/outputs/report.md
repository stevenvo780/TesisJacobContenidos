# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-08T20:46:48.090246Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: 0.0001
- CR: 17497.3222
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.4985
- rmse_abm_no_ode: 1.4985
- rmse_ode: 4963.6661
- rmse_reduced: 1.6123
- threshold: 0.1695

### Calibración
- forcing_scale: 0.6191
- macro_coupling: 0.7509
- damping: 0.9184
- ode_alpha: 0.0441
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1385

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9997
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1751
- rmse_abm_no_ode: 1.1751
- rmse_ode: 1.7206
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6353


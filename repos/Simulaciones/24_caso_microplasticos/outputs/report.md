# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T01:52:08.098735Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -17.9436
- bootstrap_mean: -17.9731
- CI 95%: [-18.7496, -17.3261]
- weighted_value (LoE factor 0.80): -14.3549
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9260
- CR: 1.0800
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 23.0813
- rmse_abm_no_ode: 1.2184
- rmse_ode: 42.1173
- rmse_reduced: 1.5745
- threshold: 0.1000

### Calibración
- forcing_scale: 0.2374
- macro_coupling: 0.2660
- damping: 0.2292
- ode_alpha: 0.0078
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1510

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1589
- bootstrap_mean: 0.1624
- CI 95%: [0.1186, 0.2216]
- weighted_value (LoE factor 0.80): 0.1271
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9888
- CR: 1.0113
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 15.1540
- rmse_abm_no_ode: 18.0173
- rmse_ode: 12.2479
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7461
- macro_coupling: 1.0000
- damping: 0.4276
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3875


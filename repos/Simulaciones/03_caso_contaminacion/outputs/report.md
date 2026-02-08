# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-08T17:43:07.301179Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4616
- bootstrap_mean: 0.4632
- CI 95%: [0.4435, 0.4871]
- weighted_value (LoE factor 0.20): 0.0923
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8376
- CR: 1.1939
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8225
- rmse_ode: 1.1754
- rmse_reduced: 5.2423
- threshold: 2.1312

### Calibración
- forcing_scale: 0.3226
- macro_coupling: 0.1119
- damping: 0.6076
- ode_alpha: 0.3767
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7712

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1247
- bootstrap_mean: 0.1263
- CI 95%: [0.0013, 0.2494]
- weighted_value (LoE factor 0.20): 0.0249
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.7327
- CR: 1.3647
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 7.5126
- rmse_ode: 8.9437
- rmse_reduced: 8.5832
- threshold: 8.1069

### Calibración
- forcing_scale: 0.7579
- macro_coupling: 1.0000
- damping: 0.8285
- ode_alpha: 0.0716
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5179


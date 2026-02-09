# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T02:13:22.974695Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.5858
- bootstrap_mean: -1.6243
- CI 95%: [-2.2304, -1.1452]
- weighted_value (LoE factor 0.60): -0.9515
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9480
- CR: 1.0547
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0268
- rmse_abm_no_ode: 0.7838
- rmse_ode: 10.1577
- rmse_reduced: 2.7961
- threshold: 0.7146

### Calibración
- forcing_scale: 0.9351
- macro_coupling: 0.3008
- damping: 0.9500
- ode_alpha: 0.3090
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2793

## Fase real
- **overall_pass**: False

### EDI
- valor: -9.1397
- bootstrap_mean: -9.2519
- CI 95%: [-12.1888, -7.1539]
- weighted_value (LoE factor 0.60): -5.4838
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9185
- CR: 1.0876
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3171
- rmse_abm_no_ode: 0.3271
- rmse_ode: 8.2638
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9398
- macro_coupling: 0.6239
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782


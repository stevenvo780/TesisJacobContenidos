# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T15:57:51.949204Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6788
- bootstrap_mean: 0.6793
- CI 95%: [0.6643, 0.6943]
- weighted_value (LoE factor 0.80): 0.5431
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.6289
- external: 0.8588
- CR: 0.7323
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5006
- rmse_abm_no_ode: 1.5587
- rmse_ode: 1.8385
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9469
- macro_coupling: 0.6115
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2154

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5861
- bootstrap_mean: 0.5871
- CI 95%: [0.5689, 0.6161]
- weighted_value (LoE factor 0.80): 0.4689
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9968
- CR: 1.0032
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 7.4579
- rmse_abm_no_ode: 18.0173
- rmse_ode: 2.5937
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


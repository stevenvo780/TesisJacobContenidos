# Reporte de Validación — Cambio de Paradigmas Científicos

- generated_at: 2026-02-08T20:49:56.949837Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -2.6235
- bootstrap_mean: -2.6315
- CI 95%: [-2.8188, -2.4701]
- weighted_value (LoE factor 0.20): -0.5247
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9929
- CR: 1.0071
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0653
- rmse_abm_no_ode: 0.2940
- rmse_ode: 1.4690
- rmse_reduced: 1.8187
- threshold: 0.3135

### Calibración
- forcing_scale: 0.1198
- macro_coupling: 0.4231
- damping: 0.1257
- ode_alpha: 0.0534
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2324

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.0079
- bootstrap_mean: -2.0388
- CI 95%: [-2.5680, -1.6786]
- weighted_value (LoE factor 0.20): -0.4016
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.4278
- CR: 2.3378
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3578
- rmse_abm_no_ode: 1.1163
- rmse_ode: nan
- rmse_reduced: 3.3578
- threshold: 1.0107

### Calibración
- forcing_scale: 0.8166
- macro_coupling: 0.1901
- damping: 0.8047
- ode_alpha: 0.4875
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4656


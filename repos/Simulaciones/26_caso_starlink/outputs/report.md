# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T02:03:19.847227Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -10.5292
- bootstrap_mean: -10.5345
- CI 95%: [-10.9778, -10.1706]
- weighted_value (LoE factor 0.80): -8.4233
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9800
- CR: 1.0203
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3572
- rmse_abm_no_ode: 0.2912
- rmse_ode: 9.7554
- rmse_reduced: 2.0599
- threshold: 0.3123

### Calibración
- forcing_scale: 0.8820
- macro_coupling: 0.4186
- damping: 0.8903
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0909

## Fase real
- **overall_pass**: False

### EDI
- valor: -192.7871
- bootstrap_mean: -193.1000
- CI 95%: [-226.0881, -161.6833]
- weighted_value (LoE factor 0.80): -154.2297
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8706
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0245
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.2330
- rmse_reduced: 0.0001
- threshold: 0.1000

### Calibración
- forcing_scale: 0.1239
- macro_coupling: 0.1073
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0002


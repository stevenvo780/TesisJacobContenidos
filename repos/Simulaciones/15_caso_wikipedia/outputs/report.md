# Reporte de Validación — Wikipedia Clima

- generated_at: 2026-02-08T20:39:27.309670Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0109
- bootstrap_mean: 0.0109
- CI 95%: [0.0107, 0.0112]
- weighted_value (LoE factor 0.20): 0.0022
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0064
- rmse_abm_no_ode: 1.0175
- rmse_ode: 1.2830
- rmse_reduced: 1.6904
- threshold: 0.3047

### Calibración
- forcing_scale: 0.6240
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.0632
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2459

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0031
- bootstrap_mean: 0.0032
- CI 95%: [0.0024, 0.0040]
- weighted_value (LoE factor 0.20): 0.0006
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9953
- external: 0.0003
- CR: 3821.1740
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 4.4270
- rmse_abm_no_ode: 4.4410
- rmse_ode: 3.9441
- rmse_reduced: 3.8377
- threshold: 2.5160

### Calibración
- forcing_scale: 0.4922
- macro_coupling: 0.7723
- damping: 0.9500
- ode_alpha: 0.0358
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9281


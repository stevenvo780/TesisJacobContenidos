# Reporte de Validación — Salinización de Suelos

- generated_at: 2026-02-08T20:40:40.529183Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2483
- bootstrap_mean: -0.2504
- CI 95%: [-0.2827, -0.2259]
- weighted_value (LoE factor 0.20): -0.0497
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.9989
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4599
- rmse_abm_no_ode: 1.1695
- rmse_ode: 2.1759
- rmse_reduced: 3.3810
- threshold: 0.8882

### Calibración
- forcing_scale: 0.9803
- macro_coupling: 0.4280
- damping: 0.9500
- ode_alpha: 0.3626
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3353

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.9302
- bootstrap_mean: -1.9486
- CI 95%: [-3.6252, -0.9313]
- weighted_value (LoE factor 0.20): -0.3860
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9610
- external: 0.0024
- CR: 401.7657
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 3.8418
- rmse_abm_no_ode: 1.3111
- rmse_ode: 2.7269
- rmse_reduced: 1.0780
- threshold: 0.1357

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.8607
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2726


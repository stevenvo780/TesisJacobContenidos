# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-09T17:03:45.697191Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9980
- external: 0.9264
- CR: 1.0774
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9582
- rmse_abm_no_ode: 0.9582
- rmse_ode: 1.5238
- rmse_reduced: 0.9582
- threshold: 0.2854

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7782

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9728
- external: 0.9246
- CR: 1.0521
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8889
- rmse_abm_no_ode: 1.8889
- rmse_ode: 1.5789
- rmse_reduced: 1.8889
- threshold: 0.3262

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8940


# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-09T17:03:59.000786Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.8411
- bootstrap_mean: -1.8420
- CI 95%: [-1.9092, -1.7858]
- weighted_value (LoE factor 0.60): -1.1047
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9540
- CR: 1.0482
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5961
- rmse_abm_no_ode: 1.2657
- rmse_ode: 7.0374
- rmse_reduced: 3.7882
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3467
- macro_coupling: 0.4770
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3368
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1170

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.2936
- bootstrap_mean: -0.2939
- CI 95%: [-0.3553, -0.2322]
- weighted_value (LoE factor 0.60): -0.1761
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9992
- external: 0.9916
- CR: 1.0077
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5056
- rmse_abm_no_ode: 1.1639
- rmse_ode: 2.5179
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.8999
- macro_coupling: 0.4073
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1431


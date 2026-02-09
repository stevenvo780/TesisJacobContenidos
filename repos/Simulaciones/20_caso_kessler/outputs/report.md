# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-09T18:26:41.883836Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -3.4194
- bootstrap_mean: -3.4154
- CI 95%: [-3.5367, -3.2629]
- weighted_value (LoE factor 0.20): -0.6839
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8221
- external: 0.7165
- CR: 1.1475
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2691399.5511
- rmse_abm_no_ode: 608992.9187
- rmse_ode: 7660452158067588.0000
- rmse_reduced: 627263.5667
- threshold: 8.9265

### Calibración
- forcing_scale: 0.0227
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0099
- ode_alpha: 0.1532
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 142138.1939
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1612
- bootstrap_mean: -0.1568
- CI 95%: [-0.2500, -0.0355]
- weighted_value (LoE factor 0.20): -0.0322
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7883
- external: 0.5222
- CR: 1.5095
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 665319.2883
- rmse_abm_no_ode: 572967.3112
- rmse_ode: 2073629760066926.7500
- rmse_reduced: 627284.2745
- threshold: 2.3530

### Calibración
- forcing_scale: 0.0033
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0316
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 131424.5550
- ode_rolling: None


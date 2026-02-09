# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-09T18:53:41.731663Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4485
- bootstrap_mean: -0.4488
- CI 95%: [-0.4588, -0.4414]
- weighted_value (LoE factor 0.20): -0.0897
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7976
- external: 0.6861
- CR: 1.1625
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 882106.9302
- rmse_abm_no_ode: 608992.9187
- rmse_ode: 10.6201
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
- valor: -0.3559
- bootstrap_mean: -0.3560
- CI 95%: [-0.3617, -0.3515]
- weighted_value (LoE factor 0.20): -0.0712
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7914
- external: 0.6605
- CR: 1.1982
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 776863.0414
- rmse_abm_no_ode: 572967.3112
- rmse_ode: 11.6175
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


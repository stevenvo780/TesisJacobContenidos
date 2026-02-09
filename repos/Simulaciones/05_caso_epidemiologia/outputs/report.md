# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-09T20:24:03.228606Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5276
- bootstrap_mean: 0.5233
- CI 95%: [0.4465, 0.5945]
- weighted_value (LoE factor 0.20): 0.1055
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.3969
- external: 0.2630
- CR: 1.5094
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0133
- rmse_abm_no_ode: 4.2623
- rmse_ode: 0.5436
- rmse_reduced: 15.2230
- threshold: 0.1000

### Calibración
- forcing_scale: 1.0000
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0068
- ode_beta: 0.8095
- assimilation_strength: 0.0000
- calibration_rmse: 20.1559
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: -0.0004
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.5221
- rmse_abm_no_ode: 4.5221
- rmse_ode: 16.4401
- rmse_reduced: 13.8782
- threshold: 4.3680

### Calibración
- forcing_scale: 0.1000
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000
- ode_rolling: None


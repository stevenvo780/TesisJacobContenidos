# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T18:26:46.064353Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.5337
- bootstrap_mean: -0.5334
- CI 95%: [-0.5402, -0.5264]
- weighted_value (LoE factor 0.60): -0.3202
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9932
- CR: 1.0069
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0154
- rmse_abm_no_ode: 1.3141
- rmse_ode: 0.6268
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3130
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3029
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1401
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1817
- bootstrap_mean: -0.1815
- CI 95%: [-0.1956, -0.1672]
- weighted_value (LoE factor 0.60): -0.1090
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9987
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 22.1132
- rmse_abm_no_ode: 18.7135
- rmse_ode: 29.4435
- rmse_reduced: 35.7618
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5410
- ode_rolling: None


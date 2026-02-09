# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T20:23:56.754836Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2847
- bootstrap_mean: 0.2851
- CI 95%: [0.2783, 0.2940]
- weighted_value (LoE factor 0.80): 0.2278
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9980
- CR: 1.0019
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1106
- rmse_abm_no_ode: 1.5527
- rmse_ode: 1.7280
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9438
- macro_coupling: 0.3903
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2154
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4265
- bootstrap_mean: 0.4272
- CI 95%: [0.4144, 0.4465]
- weighted_value (LoE factor 0.80): 0.3412
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9984
- CR: 1.0016
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 10.4284
- rmse_abm_no_ode: 18.1839
- rmse_ode: 2.7865
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7512
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4280
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3876
- ode_rolling: None


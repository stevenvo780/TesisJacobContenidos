# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-11T04:40:51.392715Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0337
- bootstrap_mean: 0.0337
- CI 95%: [0.0286, 0.0387]
- weighted_value (LoE factor 0.20): 0.0067
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9275
- external: 0.9204
- CR: 1.0077
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4009
- rmse_abm_no_ode: 0.4085
- rmse_ode: 0.4414
- rmse_reduced: 0.4149
- threshold: 0.3269

### Calibración
- forcing_scale: 0.0018
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0149
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0049
- bootstrap_mean: -0.0049
- CI 95%: [-0.0061, -0.0041]
- weighted_value (LoE factor 0.20): -0.0010
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6974
- external: -0.6344
- CR: 1.0993
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6024
- rmse_abm_no_ode: 1.5992
- rmse_ode: 2.0440
- rmse_reduced: 1.5946
- threshold: 1.2251

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0301
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


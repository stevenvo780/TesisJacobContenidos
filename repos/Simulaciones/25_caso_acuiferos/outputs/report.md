# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-10T05:36:45.828039Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3107
- bootstrap_mean: 0.3114
- CI 95%: [0.2978, 0.3282]
- weighted_value (LoE factor 0.60): 0.1864
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9973
- CR: 1.0027
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8954
- rmse_abm_no_ode: 1.2991
- rmse_ode: 0.6323
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4452
- macro_coupling: 0.4345
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4483
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1404
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0270
- bootstrap_mean: -0.0269
- CI 95%: [-0.0294, -0.0242]
- weighted_value (LoE factor 0.60): -0.0162
- válido (0.30-0.90): False
- detrended_edi: -0.0270
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 19.3884
- rmse_abm_no_ode: 18.8796
- rmse_ode: 29.2432
- rmse_reduced: 35.7621
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5755
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


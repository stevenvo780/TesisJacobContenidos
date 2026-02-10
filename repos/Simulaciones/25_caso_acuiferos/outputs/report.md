# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-10T04:22:20.014684Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1525
- bootstrap_mean: 0.1526
- CI 95%: [0.1458, 0.1603]
- weighted_value (LoE factor 0.60): 0.0915
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9994
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1088
- rmse_abm_no_ode: 1.3082
- rmse_ode: 0.6357
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4015
- macro_coupling: 0.1211
- ode_coupling_strength: 0.0969
- abm_feedback_gamma: 0.0500
- damping: 0.4014
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1401
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1583
- bootstrap_mean: -0.1578
- CI 95%: [-0.1711, -0.1438]
- weighted_value (LoE factor 0.60): -0.0950
- válido (0.30-0.90): False
- detrended_edi: -0.1583
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 0.9999
- external: 0.9988
- CR: 1.0011
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 22.7590
- rmse_abm_no_ode: 19.6484
- rmse_ode: 29.3106
- rmse_reduced: 35.7620
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4777
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9448
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5267
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


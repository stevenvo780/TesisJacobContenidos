# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-12T04:08:26.213943Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0608
- bootstrap_mean: -0.0642
- CI 95%: [-0.1004, -0.0467]
- weighted_value (LoE factor 0.60): -0.0365
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9452
- external: 0.8680
- CR: 1.0889
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3743
- rmse_abm_no_ode: 1.2954
- rmse_ode: 1.5150
- rmse_reduced: 0.9439
- threshold: 0.8250

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8258
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0205
- bootstrap_mean: -0.0204
- CI 95%: [-0.0236, -0.0169]
- weighted_value (LoE factor 0.60): -0.0123
- válido (0.30-0.90): False
- detrended_edi: -0.0205
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 19.8898
- rmse_abm_no_ode: 19.4907
- rmse_ode: 28.3461
- rmse_reduced: 35.7619
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5762
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


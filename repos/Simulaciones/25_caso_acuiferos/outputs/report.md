# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-12T01:19:54.447878Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0247
- bootstrap_mean: -0.0264
- CI 95%: [-0.0450, -0.0175]
- weighted_value (LoE factor 0.60): -0.0148
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9814
- external: 0.9604
- CR: 1.0219
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3277
- rmse_abm_no_ode: 1.2957
- rmse_ode: 1.4229
- rmse_reduced: 0.9439
- threshold: 0.8250

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2726
- ode_coupling_strength: 0.2181
- abm_feedback_gamma: 0.0500
- damping: 0.9187
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8287
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1257
- bootstrap_mean: -0.1252
- CI 95%: [-0.1417, -0.1070]
- weighted_value (LoE factor 0.60): -0.0754
- válido (0.30-0.90): False
- detrended_edi: -0.1257
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 0.9999
- external: 0.9976
- CR: 1.0023
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 23.4481
- rmse_abm_no_ode: 20.8300
- rmse_ode: 28.7159
- rmse_reduced: 35.7621
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
- calibration_rmse: 0.5503
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


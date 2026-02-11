# Reporte de Validación — Acidificación Oceánica (CO2SYS + Revelle Factor)

- generated_at: 2026-02-11T04:44:43.397291Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2242
- bootstrap_mean: 0.2239
- CI 95%: [0.1993, 0.2467]
- weighted_value (LoE factor 0.20): 0.0448
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9973
- external: 0.4448
- CR: 2.2421
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.5691
- rmse_abm_no_ode: 1.4135
- rmse_ode: 7.9632
- rmse_reduced: 2.0224
- threshold: 1.0107

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1040
- ode_coupling_strength: 0.0832
- abm_feedback_gamma: 0.0500
- damping: 0.0695
- ode_alpha: 0.0170
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3061
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0211
- bootstrap_mean: -0.0247
- CI 95%: [-0.0446, -0.0147]
- weighted_value (LoE factor 0.20): -0.0042
- válido (0.30-0.90): False
- detrended_edi: -0.0211
- trend_ratio: 1.000
- trend_r2: 0.861

### Symploké y CR
- internal: 0.9992
- external: 0.8250
- CR: 1.2111
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3432
- rmse_abm_no_ode: 3.3431
- rmse_ode: 8.8952
- rmse_reduced: 3.2742
- threshold: 2.3256

### Calibración
- forcing_scale: 0.8574
- macro_coupling: 0.2886
- ode_coupling_strength: 0.2309
- abm_feedback_gamma: 0.0500
- damping: 0.0113
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9496
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


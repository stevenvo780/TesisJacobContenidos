# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-11T04:47:00.234525Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4296
- bootstrap_mean: 0.4309
- CI 95%: [0.3929, 0.4760]
- weighted_value (LoE factor 0.60): 0.2578
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9957
- CR: 1.0043
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8194
- rmse_abm_no_ode: 1.3093
- rmse_ode: 0.6311
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3207
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3191
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1401
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3900
- bootstrap_mean: 0.3896
- CI 95%: [0.3720, 0.4011]
- weighted_value (LoE factor 0.60): 0.2340
- válido (0.30-0.90): True
- detrended_edi: 0.3900
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 0.9999
- external: 0.9987
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 21.8141
- rmse_abm_no_ode: 18.3309
- rmse_ode: 29.2807
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
- calibration_rmse: 0.5463
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-11T02:08:59.238066Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1544
- bootstrap_mean: 0.1520
- CI 95%: [0.0983, 0.2000]
- weighted_value (LoE factor 0.60): 0.0926
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2149
- rmse_abm_no_ode: 1.3049
- rmse_ode: 0.6374
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4382
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.4281
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1403
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.4182
- bootstrap_mean: 0.4163
- CI 95%: [0.3905, 0.4320]
- weighted_value (LoE factor 0.60): 0.2509
- válido (0.30-0.90): True
- detrended_edi: 0.4182
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 20.8066
- rmse_abm_no_ode: 19.4673
- rmse_ode: 29.2711
- rmse_reduced: 35.7621
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1551
- ode_coupling_strength: 0.1241
- abm_feedback_gamma: 0.0500
- damping: 0.8974
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5599
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


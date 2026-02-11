# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-11T05:02:52.003433Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3809
- bootstrap_mean: 0.3821
- CI 95%: [0.3422, 0.4301]
- weighted_value (LoE factor 0.60): 0.2285
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9970
- CR: 1.0030
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8895
- rmse_abm_no_ode: 1.3130
- rmse_ode: 0.6323
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3176
- macro_coupling: 0.3288
- ode_coupling_strength: 0.2630
- abm_feedback_gamma: 0.0500
- damping: 0.3079
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
- valor: 0.3832
- bootstrap_mean: 0.3827
- CI 95%: [0.3654, 0.3941]
- weighted_value (LoE factor 0.60): 0.2299
- válido (0.30-0.90): True
- detrended_edi: 0.3832
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
- rmse_abm: 22.0587
- rmse_abm_no_ode: 18.7135
- rmse_ode: 29.2853
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

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


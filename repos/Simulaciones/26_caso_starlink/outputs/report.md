# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-11T04:47:26.986739Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9244
- bootstrap_mean: 0.9246
- CI 95%: [0.9170, 0.9330]
- weighted_value (LoE factor 0.80): 0.7395
- válido (0.30-0.90): False
- detrended_edi: 0.9244
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 0.9995
- external: 0.9986
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2435
- rmse_abm_no_ode: 0.4299
- rmse_ode: 0.2035
- rmse_reduced: 3.2218
- threshold: 0.6792

### Calibración
- forcing_scale: 0.9098
- macro_coupling: 0.4988
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1384
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1568
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7483
- bootstrap_mean: 0.7483
- CI 95%: [0.7483, 0.7483]
- weighted_value (LoE factor 0.80): 0.5986
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.7687
- CR: 1.3006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0171
- rmse_abm_no_ode: 0.4150
- rmse_ode: 3.3975
- rmse_reduced: 4.0409
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4525
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.1502
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4044
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


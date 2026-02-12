# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-12T04:09:25.419252Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0070
- bootstrap_mean: 0.0031
- CI 95%: [-0.0945, 0.1389]
- weighted_value (LoE factor 0.60): -0.0042
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9921
- external: 0.9621
- CR: 1.0312
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1374
- rmse_abm_no_ode: 1.1295
- rmse_ode: 1.2407
- rmse_reduced: 1.4318
- threshold: 1.1459

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8006
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0252
- bootstrap_mean: 0.0267
- CI 95%: [-0.1433, 0.1856]
- weighted_value (LoE factor 0.60): 0.0151
- válido (0.30-0.90): False
- detrended_edi: 0.0252
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9992
- external: 0.9923
- CR: 1.0069
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.2067
- rmse_abm_no_ode: 4.3153
- rmse_ode: 4.2985
- rmse_reduced: 6.7009
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6566
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4601
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


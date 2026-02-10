# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-10T04:22:02.540674Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.7774
- bootstrap_mean: 0.7787
- CI 95%: [0.7131, 0.8344]
- weighted_value (LoE factor 0.20): 0.1555
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.0229
- external: 0.0186
- CR: 1.2335
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9074
- rmse_abm_no_ode: 4.0761
- rmse_ode: 0.6492
- rmse_reduced: 15.2230
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9351
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5585
- ode_alpha: 0.0068
- ode_beta: 0.8095
- assimilation_strength: 0.0000
- calibration_rmse: 0.4880
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: -0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 4.5221
- rmse_abm_no_ode: 4.5221
- rmse_ode: 15.0864
- rmse_reduced: 13.8782
- threshold: 4.3680

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3704
- ode_coupling_strength: 0.2964
- abm_feedback_gamma: 0.0500
- damping: 0.9121
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4383
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


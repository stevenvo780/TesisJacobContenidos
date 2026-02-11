# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-11T04:41:08.854368Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.6417
- bootstrap_mean: -0.6391
- CI 95%: [-0.6968, -0.5756]
- weighted_value (LoE factor 0.20): -0.1283
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9021
- CR: 1.1085
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7839
- rmse_abm_no_ode: 1.2007
- rmse_ode: 0.4169
- rmse_reduced: 0.4775
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9449
- macro_coupling: 0.1974
- ode_coupling_strength: 0.1579
- abm_feedback_gamma: 0.0500
- damping: 0.5673
- ode_alpha: 0.0068
- ode_beta: 0.8095
- assimilation_strength: 0.0000
- calibration_rmse: 0.4880
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0586
- bootstrap_mean: 0.0387
- CI 95%: [-0.2537, 0.1734]
- weighted_value (LoE factor 0.20): 0.0117
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9995
- external: 0.4423
- CR: 2.2596
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.2570
- rmse_abm_no_ode: 5.1102
- rmse_ode: 15.1313
- rmse_reduced: 4.5220
- threshold: 4.3680

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4383
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


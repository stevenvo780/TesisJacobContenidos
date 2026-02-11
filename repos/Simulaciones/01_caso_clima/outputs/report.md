# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-11T00:39:20.913587Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0250
- bootstrap_mean: -0.0251
- CI 95%: [-0.0271, -0.0234]
- weighted_value (LoE factor 1.00): -0.0250
- válido (0.30-0.90): False
- detrended_edi: -0.0250
- trend_ratio: 1.000
- trend_r2: 0.996

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
- rmse_abm: 4.5685
- rmse_abm_no_ode: 4.4570
- rmse_ode: 8.1428
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.7533
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7560
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2547
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0376
- bootstrap_mean: 0.0376
- CI 95%: [0.0324, 0.0425]
- weighted_value (LoE factor 1.00): 0.0376
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9989
- CR: 1.0009
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1473
- rmse_abm_no_ode: 1.1922
- rmse_ode: 1.6993
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2028
- ode_coupling_strength: 0.1623
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7347
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-12T03:56:48.271841Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2275
- bootstrap_mean: 0.2288
- CI 95%: [0.1993, 0.2586]
- weighted_value (LoE factor 0.60): 0.1365
- válido (0.30-0.90): False
- detrended_edi: 0.2275
- trend_ratio: 1.000
- trend_r2: 0.805

### Symploké y CR
- internal: 0.9998
- external: 0.9948
- CR: 1.0050
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1768
- rmse_abm_no_ode: 2.8178
- rmse_ode: 5.5902
- rmse_reduced: 5.3314
- threshold: 1.4385

### Calibración
- forcing_scale: 0.9184
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.3509
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0038
- bootstrap_mean: -0.0040
- CI 95%: [-0.0209, 0.0116]
- weighted_value (LoE factor 0.60): -0.0023
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9966
- external: 0.9968
- CR: 0.9999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9508
- rmse_abm_no_ode: 2.9396
- rmse_ode: 3.2334
- rmse_reduced: 3.2946
- threshold: 3.2834

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.7927
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


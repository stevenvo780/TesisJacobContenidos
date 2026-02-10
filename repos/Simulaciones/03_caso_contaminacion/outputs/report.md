# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-10T05:32:14.720063Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [-0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1574
- external: 0.1246
- CR: 1.2631
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8190
- rmse_abm_no_ode: 0.8190
- rmse_ode: 9.7647
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.8836
- macro_coupling: 0.4192
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7353
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5782
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, 0.0000]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1574
- external: 0.1211
- CR: 1.3003
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 3.2945
- rmse_abm_no_ode: 3.2945
- rmse_ode: 8.0601
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 1.0000
- macro_coupling: 0.4500
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8000
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6625
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


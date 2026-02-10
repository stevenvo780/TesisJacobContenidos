# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-10T04:20:32.968036Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [-0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1689
- external: 0.1352
- CR: 1.2498
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
- rmse_ode: 8.9390
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.8061
- macro_coupling: 0.4741
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6742
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5738
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
- internal: 0.1690
- external: 0.1322
- CR: 1.2782
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
- calibration_rmse: 0.6634
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


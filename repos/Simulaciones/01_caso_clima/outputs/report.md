# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-11T17:24:26.782974Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0036
- bootstrap_mean: 0.0036
- CI 95%: [0.0035, 0.0038]
- weighted_value (LoE factor 1.00): 0.0036
- válido (0.30-0.90): False
- detrended_edi: 0.0036
- trend_ratio: 1.000
- trend_r2: 0.996

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.8422
- rmse_abm_no_ode: 5.8633
- rmse_ode: 4.6558
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.6476
- macro_coupling: 0.1260
- ode_coupling_strength: 0.1008
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1847
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2539
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0096
- bootstrap_mean: 0.0099
- CI 95%: [-0.0085, 0.0289]
- weighted_value (LoE factor 1.00): 0.0096
- válido (0.30-0.90): False
- detrended_edi: 0.0096
- trend_ratio: 1.000
- trend_r2: 0.525

### Symploké y CR
- internal: 1.0000
- external: 0.9944
- CR: 1.0056
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8603
- rmse_abm_no_ode: 0.8686
- rmse_ode: 0.8647
- rmse_reduced: 2.4945
- threshold: 1.1902

### Calibración
- forcing_scale: 0.1112
- macro_coupling: 0.2004
- ode_coupling_strength: 0.1604
- abm_feedback_gamma: 0.0500
- damping: 0.1007
- ode_alpha: 0.4014
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7386
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


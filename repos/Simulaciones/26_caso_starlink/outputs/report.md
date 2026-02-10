# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-10T04:22:27.714628Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3746
- bootstrap_mean: 0.3748
- CI 95%: [0.3658, 0.3851]
- weighted_value (LoE factor 0.80): 0.2997
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9978
- CR: 1.0022
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7716
- rmse_abm_no_ode: 1.2339
- rmse_ode: 0.7355
- rmse_reduced: 0.6953
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3930
- macro_coupling: 0.1342
- ode_coupling_strength: 0.1074
- abm_feedback_gamma: 0.0500
- damping: 0.3817
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3374
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1895.0367
- CI 95%: [-2172.1947, -1659.2700]
- weighted_value (LoE factor 0.80): -0.8000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 1.000

### Symploké y CR
- internal: 0.9917
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0587
- rmse_abm_no_ode: 0.0000
- rmse_ode: 0.6286
- rmse_reduced: 0.0000
- threshold: 0.1000

### Calibración
- forcing_scale: 0.0492
- macro_coupling: 0.0787
- ode_coupling_strength: 0.0629
- abm_feedback_gamma: 0.0500
- damping: 0.7711
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-10T02:52:05.319173Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0009
- bootstrap_mean: 0.0009
- CI 95%: [0.0008, 0.0010]
- weighted_value (LoE factor 0.20): 0.0002
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9351
- external: 0.8562
- CR: 1.0921
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3998
- rmse_abm_no_ode: 1.4011
- rmse_ode: 0.5471
- rmse_reduced: 1.3994
- threshold: 0.3900

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7388
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0022
- bootstrap_mean: 0.0022
- CI 95%: [0.0018, 0.0025]
- weighted_value (LoE factor 0.20): 0.0004
- válido (0.30-0.90): False
- detrended_edi: 0.0022
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.4679
- external: -0.3254
- CR: 1.4379
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8332
- rmse_abm_no_ode: 1.8372
- rmse_ode: 1.0036
- rmse_reduced: 1.8293
- threshold: 0.1452

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3605
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-12T03:58:34.660305Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0452
- bootstrap_mean: 0.0460
- CI 95%: [0.0402, 0.0553]
- weighted_value (LoE factor 1.00): 0.0452
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9983
- external: 0.9985
- CR: 0.9998
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7509
- rmse_abm_no_ode: 1.8338
- rmse_ode: 1.0240
- rmse_reduced: 0.7984
- threshold: 0.7086

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8863
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2274
- bootstrap_mean: 0.2320
- CI 95%: [0.1712, 0.3296]
- weighted_value (LoE factor 1.00): 0.2274
- válido (0.30-0.90): False
- detrended_edi: 0.2274
- trend_ratio: 1.000
- trend_r2: 0.610

### Symploké y CR
- internal: 0.9999
- external: 0.9635
- CR: 1.0377
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8854
- rmse_abm_no_ode: 3.7348
- rmse_ode: 2.1000
- rmse_reduced: 1.2725
- threshold: 1.2735

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1621
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6560
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


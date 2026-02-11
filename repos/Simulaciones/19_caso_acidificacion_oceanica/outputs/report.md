# Reporte de Validación — Acidificación Oceánica (CO2SYS + Revelle Factor)

- generated_at: 2026-02-11T02:09:29.762876Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1055
- bootstrap_mean: 0.1040
- CI 95%: [0.0884, 0.1233]
- weighted_value (LoE factor 0.20): 0.0211
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9980
- external: 0.3487
- CR: 2.8620
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8091
- rmse_abm_no_ode: 1.4135
- rmse_ode: 7.9792
- rmse_reduced: 2.0224
- threshold: 1.0107

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3584
- ode_coupling_strength: 0.2867
- abm_feedback_gamma: 0.0500
- damping: 0.8903
- ode_alpha: 0.0170
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7798
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0211
- bootstrap_mean: -0.0261
- CI 95%: [-0.0421, -0.0158]
- weighted_value (LoE factor 0.20): -0.0042
- válido (0.30-0.90): False
- detrended_edi: -0.0211
- trend_ratio: 1.000
- trend_r2: 0.861

### Symploké y CR
- internal: 0.9992
- external: 0.8124
- CR: 1.2299
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3432
- rmse_abm_no_ode: 3.3431
- rmse_ode: 8.8954
- rmse_reduced: 3.2742
- threshold: 2.3256

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4394
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5591
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5566
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


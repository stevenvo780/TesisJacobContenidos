# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-10T05:35:31.952406Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: -0.0133
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8853
- rmse_abm_no_ode: 2.8853
- rmse_ode: 1.9815
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.5478
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.5418
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2385
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0064
- bootstrap_mean: 0.0063
- CI 95%: [0.0038, 0.0093]
- weighted_value (LoE factor 0.20): 0.0013
- válido (0.30-0.90): False
- detrended_edi: 0.0064
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.8156
- external: 0.7704
- CR: 1.0587
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9469
- rmse_abm_no_ode: 2.9658
- rmse_ode: 2.9113
- rmse_reduced: 2.9720
- threshold: 1.1553

### Calibración
- forcing_scale: 0.8798
- macro_coupling: 0.2745
- ode_coupling_strength: 0.2196
- abm_feedback_gamma: 0.0500
- damping: 0.8877
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1490
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


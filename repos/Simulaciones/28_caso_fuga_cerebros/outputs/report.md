# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-12T00:19:02.752050Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0013
- bootstrap_mean: 0.0093
- CI 95%: [-0.0731, 0.1190]
- weighted_value (LoE factor 0.60): 0.0008
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9936
- external: 0.9674
- CR: 1.0271
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1321
- rmse_abm_no_ode: 1.1336
- rmse_ode: 1.2263
- rmse_reduced: 1.4319
- threshold: 1.1459

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4621
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7887
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0587
- bootstrap_mean: 0.0587
- CI 95%: [-0.1034, 0.2069]
- weighted_value (LoE factor 0.60): 0.0352
- válido (0.30-0.90): False
- detrended_edi: 0.0587
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9993
- external: 0.9924
- CR: 1.0069
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.0984
- rmse_abm_no_ode: 4.3538
- rmse_ode: 4.2710
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6551
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4601
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


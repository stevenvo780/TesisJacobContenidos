# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-11T02:08:52.611752Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9068
- bootstrap_mean: 0.9063
- CI 95%: [0.9018, 0.9110]
- weighted_value (LoE factor 0.80): 0.7255
- válido (0.30-0.90): False
- detrended_edi: 0.9068
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 0.9998
- external: 0.9993
- CR: 1.0005
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3001
- rmse_abm_no_ode: 0.4235
- rmse_ode: 0.2014
- rmse_reduced: 3.2218
- threshold: 0.6792

### Calibración
- forcing_scale: 0.9095
- macro_coupling: 0.3151
- ode_coupling_strength: 0.2521
- abm_feedback_gamma: 0.0500
- damping: 0.8866
- ode_alpha: 0.1384
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1581
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4672
- bootstrap_mean: 0.4672
- CI 95%: [0.4672, 0.4672]
- weighted_value (LoE factor 0.80): 0.3738
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.6127
- CR: 1.6319
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1531
- rmse_abm_no_ode: 0.7265
- rmse_ode: 3.4635
- rmse_reduced: 4.0414
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4586
- macro_coupling: 0.2356
- ode_coupling_strength: 0.1885
- abm_feedback_gamma: 0.0500
- damping: 0.1494
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4043
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


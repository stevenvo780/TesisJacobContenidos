# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-10T06:33:49.138400Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0859
- bootstrap_mean: 0.0830
- CI 95%: [0.0680, 0.1031]
- weighted_value (LoE factor 0.20): 0.0172
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9678
- external: 0.9420
- CR: 1.0273
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3732
- rmse_abm_no_ode: 0.4083
- rmse_ode: 0.4439
- rmse_reduced: 0.4149
- threshold: 0.3269

### Calibración
- forcing_scale: 0.0965
- macro_coupling: 0.2541
- ode_coupling_strength: 0.2033
- abm_feedback_gamma: 0.0500
- damping: 0.1442
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4902
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0157
- bootstrap_mean: -0.0158
- CI 95%: [-0.0199, -0.0134]
- weighted_value (LoE factor 0.20): -0.0031
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8817
- external: -0.7678
- CR: 1.1484
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6239
- rmse_abm_no_ode: 1.5988
- rmse_ode: 2.0510
- rmse_reduced: 1.5946
- threshold: 1.2251

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3584
- ode_coupling_strength: 0.2867
- abm_feedback_gamma: 0.0500
- damping: 0.8903
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.6891
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


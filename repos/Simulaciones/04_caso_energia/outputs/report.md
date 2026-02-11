# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-11T02:10:33.393406Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0552
- bootstrap_mean: 0.0537
- CI 95%: [0.0461, 0.0600]
- weighted_value (LoE factor 0.20): 0.0110
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8533
- external: 0.8603
- CR: 0.9919
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4148
- rmse_abm_no_ode: 0.4227
- rmse_ode: 0.4406
- rmse_reduced: 0.4390
- threshold: 0.3269

### Calibración
- forcing_scale: 0.0167
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8607
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0172
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0118
- bootstrap_mean: -0.0121
- CI 95%: [-0.0155, -0.0099]
- weighted_value (LoE factor 0.20): -0.0024
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6257
- external: -0.5708
- CR: 1.0961
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6007
- rmse_abm_no_ode: 1.5958
- rmse_ode: 2.0440
- rmse_reduced: 1.5820
- threshold: 1.2251

### Calibración
- forcing_scale: 0.0081
- macro_coupling: 0.0747
- ode_coupling_strength: 0.0597
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0292
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


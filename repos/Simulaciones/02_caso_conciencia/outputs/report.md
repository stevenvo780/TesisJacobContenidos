# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-10T02:08:02.414960Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0183
- bootstrap_mean: 0.0181
- CI 95%: [0.0100, 0.0262]
- weighted_value (LoE factor 0.20): 0.0037
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.5380
- external: 0.6273
- CR: 0.8576
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1018
- rmse_abm_no_ode: 1.1223
- rmse_ode: 1.0791
- rmse_reduced: 1.1208
- threshold: 1.0629

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1368
- ode_coupling_strength: 0.1094
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3109
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0236
- bootstrap_mean: -0.0243
- CI 95%: [-0.0354, -0.0116]
- weighted_value (LoE factor 0.20): -0.0047
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7449
- external: 0.8105
- CR: 0.9190
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8034
- rmse_abm_no_ode: 0.7849
- rmse_ode: 1.7581
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.3491
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0671
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8711
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


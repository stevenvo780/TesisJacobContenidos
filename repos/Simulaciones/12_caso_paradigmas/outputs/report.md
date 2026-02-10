# Reporte de Validación — Paradigmas Cientificos (Ising)

- generated_at: 2026-02-10T04:21:55.723820Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0027
- bootstrap_mean: 0.0027
- CI 95%: [0.0017, 0.0039]
- weighted_value (LoE factor 0.20): 0.0005
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0998
- rmse_abm_no_ode: 1.1028
- rmse_ode: 0.6890
- rmse_reduced: 1.0999
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8154
- ode_alpha: 0.0312
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4738
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0002, 0.0000]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False
- detrended_edi: -0.0000
- trend_ratio: 1.000
- trend_r2: 0.902

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.7059
- rmse_abm_no_ode: 9.7056
- rmse_ode: 9.4482
- rmse_reduced: 8.3184
- threshold: 5.7385

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4236
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9395
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8121
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


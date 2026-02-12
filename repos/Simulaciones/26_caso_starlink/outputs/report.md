# Reporte de Validación — Constelaciones Satelitales Starlink (Saturation Growth)

- generated_at: 2026-02-12T04:08:44.359453Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4248
- bootstrap_mean: -0.4254
- CI 95%: [-0.4433, -0.4085]
- weighted_value (LoE factor 0.60): -0.2549
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9987
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0939
- rmse_abm_no_ode: 0.7678
- rmse_ode: 1.2155
- rmse_reduced: 0.8691
- threshold: 0.1419

### Calibración
- forcing_scale: 0.1884
- macro_coupling: 0.4821
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1909
- ode_alpha: 0.0380
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3264
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6903
- bootstrap_mean: 0.6903
- CI 95%: [0.6903, 0.6903]
- weighted_value (LoE factor 0.60): 0.4142
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.5734
- CR: 1.7437
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2272
- rmse_abm_no_ode: 0.7338
- rmse_ode: 2.1023
- rmse_reduced: 0.9174
- threshold: 0.1000

### Calibración
- forcing_scale: 0.6000
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2000
- ode_alpha: 0.0069
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5056
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


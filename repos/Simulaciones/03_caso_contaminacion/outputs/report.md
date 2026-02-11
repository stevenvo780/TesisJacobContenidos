# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-11T04:40:11.007462Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.0351
- CI 95%: [-2.7955, -1.4948]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9997
- external: 0.9997
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4281
- rmse_abm_no_ode: 3.0319
- rmse_ode: 1.6638
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.6915
- macro_coupling: 0.4928
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5751
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5711
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0915
- bootstrap_mean: -0.1369
- CI 95%: [-0.6145, 0.2410]
- weighted_value (LoE factor 0.20): -0.0183
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9874
- CR: 1.0117
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5961
- rmse_abm_no_ode: 3.8448
- rmse_ode: 3.0230
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7694
- ode_alpha: 0.0788
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6635
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


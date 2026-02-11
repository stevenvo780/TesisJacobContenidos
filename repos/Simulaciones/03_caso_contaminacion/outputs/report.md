# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-11T01:38:37.657665Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.0998
- CI 95%: [-2.8756, -1.5548]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9999
- CR: 0.9999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4790
- rmse_abm_no_ode: 3.0255
- rmse_ode: 1.6860
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.7054
- macro_coupling: 0.4327
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5809
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5707
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0892
- bootstrap_mean: -0.1339
- CI 95%: [-0.6034, 0.2369]
- weighted_value (LoE factor 0.20): -0.0178
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9991
- external: 0.9888
- CR: 1.0104
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5885
- rmse_abm_no_ode: 3.7973
- rmse_ode: 3.0223
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 1.0000
- macro_coupling: 0.4500
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8000
- ode_alpha: 0.0788
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6668
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


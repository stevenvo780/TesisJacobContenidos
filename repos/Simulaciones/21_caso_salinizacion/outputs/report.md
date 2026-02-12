# Reporte de Validación — Salinización de Suelos (Richards Bilineal)

- generated_at: 2026-02-12T04:06:09.600912Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0029
- bootstrap_mean: -0.0028
- CI 95%: [-0.0050, -0.0001]
- weighted_value (LoE factor 0.60): -0.0018
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9946
- external: 0.9955
- CR: 0.9991
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9551
- rmse_abm_no_ode: 1.9494
- rmse_ode: 2.7022
- rmse_reduced: 2.3702
- threshold: 0.9285

### Calibración
- forcing_scale: 0.9507
- macro_coupling: 0.1291
- ode_coupling_strength: 0.1033
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8811
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0582
- bootstrap_mean: 0.0452
- CI 95%: [-0.1124, 0.1594]
- weighted_value (LoE factor 0.60): 0.0349
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9997
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3290
- rmse_abm_no_ode: 0.3493
- rmse_ode: 1.1733
- rmse_reduced: 2.1959
- threshold: 0.4144

### Calibración
- forcing_scale: 0.8953
- macro_coupling: 0.1818
- ode_coupling_strength: 0.1455
- abm_feedback_gamma: 0.0500
- damping: 0.8397
- ode_alpha: 0.4828
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3612
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


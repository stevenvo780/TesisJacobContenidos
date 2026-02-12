# Reporte de Validación — Salinización de Suelos (Richards Bilineal)

- generated_at: 2026-02-12T00:18:53.490378Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0371
- bootstrap_mean: -0.0380
- CI 95%: [-0.0490, -0.0326]
- weighted_value (LoE factor 0.60): -0.0222
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9948
- external: 0.9953
- CR: 0.9996
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0696
- rmse_abm_no_ode: 1.9956
- rmse_ode: 2.7253
- rmse_reduced: 2.3702
- threshold: 0.9285

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8856
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0700
- bootstrap_mean: 0.0706
- CI 95%: [0.0648, 0.0768]
- weighted_value (LoE factor 0.60): 0.0420
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9983
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0619
- rmse_abm_no_ode: 2.2172
- rmse_ode: 2.9890
- rmse_reduced: 2.2180
- threshold: 0.4144

### Calibración
- forcing_scale: 0.8551
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.0770
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8064
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


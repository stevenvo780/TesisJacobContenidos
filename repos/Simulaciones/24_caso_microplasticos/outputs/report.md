# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-11T04:46:36.949748Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0583
- bootstrap_mean: -0.0566
- CI 95%: [-0.1119, 0.0092]
- weighted_value (LoE factor 0.80): -0.0466
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9970
- CR: 1.0029
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0250
- rmse_abm_no_ode: 1.5436
- rmse_ode: 1.7368
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.8030
- macro_coupling: 0.4340
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8043
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2156
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.2808
- CI 95%: [-1.4457, -1.0197]
- weighted_value (LoE factor 0.80): -0.8000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9984
- CR: 1.0016
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 10.3879
- rmse_abm_no_ode: 18.1251
- rmse_ode: 2.7855
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7351
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4304
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3879
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


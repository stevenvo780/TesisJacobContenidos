# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-10T02:49:57.322448Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1105
- bootstrap_mean: 0.1105
- CI 95%: [0.1077, 0.1137]
- weighted_value (LoE factor 0.80): 0.0884
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3821
- rmse_abm_no_ode: 1.5538
- rmse_ode: 1.6993
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9212
- macro_coupling: 0.1188
- ode_coupling_strength: 0.0950
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2154
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.4269
- bootstrap_mean: 0.4275
- CI 95%: [0.4153, 0.4460]
- weighted_value (LoE factor 0.80): 0.3415
- válido (0.30-0.90): True
- detrended_edi: 0.4269
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
- rmse_abm: 10.3984
- rmse_abm_no_ode: 18.1432
- rmse_ode: 2.7858
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7394
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4329
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3877
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


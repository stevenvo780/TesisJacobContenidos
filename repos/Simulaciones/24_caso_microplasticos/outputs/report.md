# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-10T04:18:16.998611Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3502
- bootstrap_mean: 0.3503
- CI 95%: [0.3414, 0.3600]
- weighted_value (LoE factor 0.80): 0.2802
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9968
- CR: 1.0032
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0016
- rmse_abm_no_ode: 1.5415
- rmse_ode: 1.7392
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.6689
- macro_coupling: 0.3843
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6685
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2160
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4348
- bootstrap_mean: 0.4363
- CI 95%: [0.4220, 0.4588]
- weighted_value (LoE factor 0.80): 0.3478
- válido (0.30-0.90): True
- detrended_edi: 0.4348
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9983
- CR: 1.0017
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.2148
- rmse_abm_no_ode: 16.3033
- rmse_ode: 2.7709
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7304
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4290
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3882
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-10T05:29:40.893542Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3295
- bootstrap_mean: 0.3300
- CI 95%: [0.3219, 0.3406]
- weighted_value (LoE factor 0.80): 0.2636
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9973
- CR: 1.0027
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0336
- rmse_abm_no_ode: 1.5415
- rmse_ode: 1.7358
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.5473
- macro_coupling: 0.2858
- ode_coupling_strength: 0.2286
- abm_feedback_gamma: 0.0500
- damping: 0.5464
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2166
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3394
- bootstrap_mean: 0.3401
- CI 95%: [0.3295, 0.3578]
- weighted_value (LoE factor 0.80): 0.2715
- válido (0.30-0.90): True
- detrended_edi: 0.3394
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9990
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 11.5234
- rmse_abm_no_ode: 17.4433
- rmse_ode: 2.8350
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.8755
- macro_coupling: 0.3624
- ode_coupling_strength: 0.2899
- abm_feedback_gamma: 0.0500
- damping: 0.5022
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3920
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


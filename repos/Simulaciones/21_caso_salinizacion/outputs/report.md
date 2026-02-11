# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-11T02:09:22.778554Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8223
- bootstrap_mean: 0.8285
- CI 95%: [0.7942, 0.8558]
- weighted_value (LoE factor 0.60): 0.4934
- válido (0.30-0.90): True
- detrended_edi: 0.8223
- trend_ratio: 1.000
- trend_r2: 0.854

### Symploké y CR
- internal: 0.9998
- external: 0.9986
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5231
- rmse_abm_no_ode: 0.7442
- rmse_ode: 1.0621
- rmse_reduced: 2.9447
- threshold: 0.6860

### Calibración
- forcing_scale: 0.9095
- macro_coupling: 0.3151
- ode_coupling_strength: 0.2521
- abm_feedback_gamma: 0.0500
- damping: 0.8866
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2988
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0150
- bootstrap_mean: 0.0151
- CI 95%: [0.0137, 0.0167]
- weighted_value (LoE factor 0.60): 0.0090
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9987
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
- rmse_abm: 2.1674
- rmse_abm_no_ode: 2.2003
- rmse_ode: 3.4991
- rmse_reduced: 2.2005
- threshold: 0.4144

### Calibración
- forcing_scale: 0.9347
- macro_coupling: 0.1643
- ode_coupling_strength: 0.1315
- abm_feedback_gamma: 0.0500
- damping: 0.1052
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7977
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


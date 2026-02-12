# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-12T04:03:44.912181Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0405
- bootstrap_mean: 0.0421
- CI 95%: [0.0172, 0.0722]
- weighted_value (LoE factor 0.60): 0.0243
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9761
- external: 0.9507
- CR: 1.0267
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9330
- rmse_abm_no_ode: 0.9723
- rmse_ode: 0.8379
- rmse_reduced: 0.5841
- threshold: 0.5110

### Calibración
- forcing_scale: 0.9207
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9800
- ode_alpha: 0.0964
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9359
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.5802
- bootstrap_mean: 0.5778
- CI 95%: [0.4227, 0.7092]
- weighted_value (LoE factor 0.60): 0.3481
- válido (0.30-0.90): True
- detrended_edi: 0.5802
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9990
- external: 0.9763
- CR: 1.0232
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4894
- rmse_abm_no_ode: 1.1659
- rmse_ode: 2.5509
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.9610
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9800
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1459
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


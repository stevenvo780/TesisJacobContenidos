# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-11T23:16:48.687243Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0618
- bootstrap_mean: 0.0642
- CI 95%: [0.0343, 0.1035]
- weighted_value (LoE factor 0.60): 0.0371
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9886
- external: 0.9778
- CR: 1.0111
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9235
- rmse_abm_no_ode: 0.9844
- rmse_ode: 0.8373
- rmse_reduced: 0.5841
- threshold: 0.5110

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.3716
- ode_coupling_strength: 0.2972
- abm_feedback_gamma: 0.0500
- damping: 0.9406
- ode_alpha: 0.0964
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9372
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6132
- bootstrap_mean: 0.6124
- CI 95%: [0.5023, 0.7150]
- weighted_value (LoE factor 0.60): 0.3679
- válido (0.30-0.90): True
- detrended_edi: 0.6132
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9990
- external: 0.9739
- CR: 1.0258
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4846
- rmse_abm_no_ode: 1.2530
- rmse_ode: 2.6710
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.9113
- macro_coupling: 0.4959
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8793
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1559
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


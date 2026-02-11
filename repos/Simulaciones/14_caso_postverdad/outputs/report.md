# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-11T05:13:20.279913Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.7482
- bootstrap_mean: 0.7489
- CI 95%: [0.7317, 0.7674]
- weighted_value (LoE factor 0.20): 0.1496
- válido (0.30-0.90): True

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
- rmse_abm: 0.7264
- rmse_abm_no_ode: 0.6810
- rmse_ode: 1.8715
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.8307
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7735
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2382
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.7616
- bootstrap_mean: 0.7654
- CI 95%: [0.7316, 0.8206]
- weighted_value (LoE factor 0.20): 0.1523
- válido (0.30-0.90): True
- detrended_edi: 0.7616
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.9985
- external: 0.9882
- CR: 1.0104
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9130
- rmse_abm_no_ode: 1.3403
- rmse_ode: 2.8564
- rmse_reduced: 3.8296
- threshold: 1.1553

### Calibración
- forcing_scale: 0.9589
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1440
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


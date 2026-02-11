# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-11T04:43:15.842545Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7214
- bootstrap_mean: 0.7223
- CI 95%: [0.7073, 0.7402]
- weighted_value (LoE factor 0.20): 0.1443
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9986
- CR: 1.0014
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8038
- rmse_abm_no_ode: 0.6804
- rmse_ode: 1.8781
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.6503
- macro_coupling: 0.1217
- ode_coupling_strength: 0.0974
- abm_feedback_gamma: 0.0500
- damping: 0.6428
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2384
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.7606
- bootstrap_mean: 0.7650
- CI 95%: [0.7310, 0.8163]
- weighted_value (LoE factor 0.20): 0.1521
- válido (0.30-0.90): True
- detrended_edi: 0.7606
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.9987
- external: 0.9890
- CR: 1.0098
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9167
- rmse_abm_no_ode: 1.3360
- rmse_ode: 2.8559
- rmse_reduced: 3.8296
- threshold: 1.1553

### Calibración
- forcing_scale: 0.9058
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1352
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


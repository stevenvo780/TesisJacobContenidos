# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-11T02:10:03.173659Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7117
- bootstrap_mean: 0.7134
- CI 95%: [0.6988, 0.7312]
- weighted_value (LoE factor 0.20): 0.1423
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9976
- CR: 1.0024
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8317
- rmse_abm_no_ode: 0.6632
- rmse_ode: 1.8806
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.9553
- macro_coupling: 0.2359
- ode_coupling_strength: 0.1887
- abm_feedback_gamma: 0.0500
- damping: 0.8938
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
- valor: 0.7160
- bootstrap_mean: 0.7217
- CI 95%: [0.6900, 0.7803]
- weighted_value (LoE factor 0.20): 0.1432
- válido (0.30-0.90): True
- detrended_edi: 0.7160
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.9995
- external: 0.9938
- CR: 1.0058
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0878
- rmse_abm_no_ode: 1.5228
- rmse_ode: 2.8566
- rmse_reduced: 3.8296
- threshold: 1.1553

### Calibración
- forcing_scale: 0.9228
- macro_coupling: 0.3202
- ode_coupling_strength: 0.2562
- abm_feedback_gamma: 0.0500
- damping: 0.8959
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1424
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-11T05:46:11.269627Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3407
- bootstrap_mean: 0.3409
- CI 95%: [0.3328, 0.3500]
- weighted_value (LoE factor 1.00): 0.3407
- válido (0.30-0.90): True
- detrended_edi: 0.3407
- trend_ratio: 1.000
- trend_r2: 0.996

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.8505
- rmse_abm_no_ode: 5.8633
- rmse_ode: 4.6584
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.6476
- macro_coupling: 0.0760
- ode_coupling_strength: 0.0608
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1847
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2539
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.6549
- bootstrap_mean: 0.6549
- CI 95%: [0.6159, 0.6902]
- weighted_value (LoE factor 1.00): 0.6549
- válido (0.30-0.90): True
- detrended_edi: 0.6549
- trend_ratio: 1.000
- trend_r2: 0.525

### Symploké y CR
- internal: 1.0000
- external: 0.9942
- CR: 1.0058
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8608
- rmse_abm_no_ode: 0.8686
- rmse_ode: 0.8647
- rmse_reduced: 2.4945
- threshold: 1.1902

### Calibración
- forcing_scale: 0.1112
- macro_coupling: 0.1504
- ode_coupling_strength: 0.1204
- abm_feedback_gamma: 0.0500
- damping: 0.1007
- ode_alpha: 0.4014
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7386
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


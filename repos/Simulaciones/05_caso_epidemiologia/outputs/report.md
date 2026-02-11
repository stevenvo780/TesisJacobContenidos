# Reporte de Validación — Epidemiología (COVID-19 Global)

- generated_at: 2026-02-11T22:25:34.589670Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0307
- bootstrap_mean: 0.0307
- CI 95%: [0.0302, 0.0314]
- weighted_value (LoE factor 0.60): 0.0184
- válido (0.30-0.90): False
- detrended_edi: 0.0307
- trend_ratio: 1.000
- trend_r2: 0.998

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
- rmse_abm: 1.8890
- rmse_abm_no_ode: 1.9488
- rmse_ode: 2.0249
- rmse_reduced: 4.4519
- threshold: 1.2717

### Calibración
- forcing_scale: 0.7337
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7137
- ode_alpha: 0.0040
- ode_beta: 0.3089
- assimilation_strength: 0.0000
- calibration_rmse: 0.1533
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.1288
- bootstrap_mean: 0.1291
- CI 95%: [0.1111, 0.1496]
- weighted_value (LoE factor 0.60): 0.0773
- válido (0.30-0.90): True
- detrended_edi: 0.1288
- trend_ratio: 1.000
- trend_r2: 0.815

### Symploké y CR
- internal: 0.9996
- external: 0.9903
- CR: 1.0093
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1042
- rmse_abm_no_ode: 1.2675
- rmse_ode: 1.4240
- rmse_reduced: 1.5087
- threshold: 1.4889

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.6415
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.3795
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


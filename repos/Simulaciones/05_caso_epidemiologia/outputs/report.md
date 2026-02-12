# Reporte de Validación — Epidemiología (COVID-19 Global)

- generated_at: 2026-02-12T03:57:32.480269Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3282
- bootstrap_mean: 0.3284
- CI 95%: [0.3251, 0.3322]
- weighted_value (LoE factor 0.60): 0.1969
- válido (0.30-0.90): True
- detrended_edi: 0.3282
- trend_ratio: 1.000
- trend_r2: 0.998

### Symploké y CR
- internal: 1.0000
- external: 0.9926
- CR: 1.0075
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3048
- rmse_abm_no_ode: 1.9422
- rmse_ode: 2.5098
- rmse_reduced: 4.4519
- threshold: 1.2717

### Calibración
- forcing_scale: 0.4988
- macro_coupling: 0.3897
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4819
- ode_alpha: 0.0040
- ode_beta: 0.3089
- assimilation_strength: 0.0000
- calibration_rmse: 0.1525
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1294
- bootstrap_mean: 0.1296
- CI 95%: [0.1124, 0.1487]
- weighted_value (LoE factor 0.60): 0.0777
- válido (0.30-0.90): False
- detrended_edi: 0.1294
- trend_ratio: 1.000
- trend_r2: 0.815

### Symploké y CR
- internal: 0.9995
- external: 0.9906
- CR: 1.0090
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0998
- rmse_abm_no_ode: 1.2633
- rmse_ode: 1.4345
- rmse_reduced: 1.5087
- threshold: 1.4889

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.6411
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.3794
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


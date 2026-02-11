# Reporte de Validación — Epidemiología (COVID-19 Global)

- generated_at: 2026-02-11T15:37:04.997835Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.5877
- bootstrap_mean: 0.5876
- CI 95%: [0.5850, 0.5903]
- weighted_value (LoE factor 0.20): 0.1175
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9090
- rmse_abm_no_ode: 0.0352
- rmse_ode: 1.8568
- rmse_reduced: 2.2045
- threshold: 0.5723

### Calibración
- forcing_scale: 0.7110
- macro_coupling: 0.4397
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4596
- ode_alpha: 0.1926
- ode_beta: 0.9881
- assimilation_strength: 0.0000
- calibration_rmse: 0.0409
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2699
- bootstrap_mean: 0.2687
- CI 95%: [0.1557, 0.3738]
- weighted_value (LoE factor 0.20): 0.0540
- válido (0.30-0.90): False
- detrended_edi: 0.2699
- trend_ratio: 1.000
- trend_r2: 0.815

### Symploké y CR
- internal: 0.9995
- external: 0.9947
- CR: 1.0048
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1014
- rmse_abm_no_ode: 1.2633
- rmse_ode: 4.2810
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


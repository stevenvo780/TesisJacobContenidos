# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-11T02:10:41.107086Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3430
- bootstrap_mean: 0.3436
- CI 95%: [0.3377, 0.3508]
- weighted_value (LoE factor 1.00): 0.3430
- válido (0.30-0.90): True
- detrended_edi: 0.3430
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
- rmse_abm: 5.8302
- rmse_abm_no_ode: 5.8555
- rmse_ode: 4.6536
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.6070
- macro_coupling: 0.1481
- ode_coupling_strength: 0.1185
- abm_feedback_gamma: 0.0500
- damping: 0.8878
- ode_alpha: 0.1847
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2541
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1487
- bootstrap_mean: -0.1456
- CI 95%: [-0.2036, -0.0965]
- weighted_value (LoE factor 1.00): -0.1487
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.9989
- CR: 1.0005
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1070
- rmse_abm_no_ode: 1.2068
- rmse_ode: 1.7004
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4959
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9142
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6357
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-11T19:22:40.241514Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1207
- bootstrap_mean: -0.1213
- CI 95%: [-0.1365, -0.1096]
- weighted_value (LoE factor 0.60): -0.0724
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9994
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7209
- rmse_abm_no_ode: 0.6432
- rmse_ode: 1.8719
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9039
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2383
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3245
- bootstrap_mean: 0.3393
- CI 95%: [0.2648, 0.4714]
- weighted_value (LoE factor 0.60): 0.1947
- válido (0.30-0.90): True
- detrended_edi: 0.3245
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.9985
- external: 0.9893
- CR: 1.0093
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0089
- rmse_abm_no_ode: 1.4935
- rmse_ode: 2.8595
- rmse_reduced: 3.8296
- threshold: 1.1553

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1336
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


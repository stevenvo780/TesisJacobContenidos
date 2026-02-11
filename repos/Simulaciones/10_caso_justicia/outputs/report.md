# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-11T16:01:49.032999Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.6884
- bootstrap_mean: 0.6890
- CI 95%: [0.6746, 0.7053]
- weighted_value (LoE factor 1.00): 0.6884
- válido (0.30-0.90): True
- detrended_edi: 0.6884
- trend_ratio: 1.000
- trend_r2: 0.875

### Symploké y CR
- internal: 0.9999
- external: 0.9996
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0746
- rmse_abm_no_ode: 1.1234
- rmse_ode: 0.4995
- rmse_reduced: 3.4489
- threshold: 0.9704

### Calibración
- forcing_scale: 0.9261
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1401
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2808
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.4496
- CI 95%: [-2.9730, -0.2296]
- weighted_value (LoE factor 1.00): -1.0000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.610

### Symploké y CR
- internal: 0.9999
- external: 0.9637
- CR: 1.0376
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8820
- rmse_abm_no_ode: 3.7246
- rmse_ode: 2.0994
- rmse_reduced: 1.2725
- threshold: 1.2735

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1632
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6560
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-11T22:22:10.634368Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.2043
- bootstrap_mean: 0.2057
- CI 95%: [0.1755, 0.2364]
- weighted_value (LoE factor 0.60): 0.1226
- válido (0.30-0.90): True
- detrended_edi: 0.2043
- trend_ratio: 1.000
- trend_r2: 0.805

### Symploké y CR
- internal: 0.9999
- external: 0.9950
- CR: 1.0048
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1956
- rmse_abm_no_ode: 2.7593
- rmse_ode: 5.5403
- rmse_reduced: 5.3314
- threshold: 1.4385

### Calibración
- forcing_scale: 0.9780
- macro_coupling: 0.4418
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.3499
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0111
- bootstrap_mean: -0.0096
- CI 95%: [-0.0656, 0.0448]
- weighted_value (LoE factor 0.60): -0.0066
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9939
- external: 0.9723
- CR: 1.0222
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1376
- rmse_abm_no_ode: 3.1032
- rmse_ode: 3.2905
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.7927
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


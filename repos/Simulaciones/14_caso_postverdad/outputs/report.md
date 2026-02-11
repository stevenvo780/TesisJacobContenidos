# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-11T22:22:04.181010Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0057
- bootstrap_mean: 0.0081
- CI 95%: [-0.0096, 0.0394]
- weighted_value (LoE factor 0.60): 0.0034
- válido (0.30-0.90): False
- detrended_edi: 0.0057
- trend_ratio: 1.000
- trend_r2: 0.760

### Symploké y CR
- internal: 0.9998
- external: 0.9988
- CR: 1.0009
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7088
- rmse_abm_no_ode: 1.7186
- rmse_ode: 3.1024
- rmse_reduced: 4.1071
- threshold: 1.1574

### Calibración
- forcing_scale: 0.9605
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7926
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5016
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

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


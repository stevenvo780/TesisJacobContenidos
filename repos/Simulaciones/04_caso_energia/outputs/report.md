# Reporte de Validación — Energía (Consumo Per Cápita)

- generated_at: 2026-02-12T02:03:12.264838Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.1793
- bootstrap_mean: 0.1805
- CI 95%: [0.1513, 0.2124]
- weighted_value (LoE factor 0.60): 0.1076
- válido (0.30-0.90): True
- detrended_edi: 0.1793
- trend_ratio: 1.000
- trend_r2: 0.852

### Symploké y CR
- internal: 0.9999
- external: 0.9975
- CR: 1.0024
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7767
- rmse_abm_no_ode: 2.1648
- rmse_ode: 4.8413
- rmse_reduced: 4.9588
- threshold: 1.1854

### Calibración
- forcing_scale: 0.9101
- macro_coupling: 0.2452
- ode_coupling_strength: 0.1961
- abm_feedback_gamma: 0.0500
- damping: 0.9362
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2946
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4193
- bootstrap_mean: 0.4244
- CI 95%: [0.2802, 0.5982]
- weighted_value (LoE factor 0.60): 0.2516
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9993
- external: 0.9983
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8675
- rmse_abm_no_ode: 1.4938
- rmse_ode: 1.9145
- rmse_reduced: 2.6082
- threshold: 0.3586

### Calibración
- forcing_scale: 1.4084
- macro_coupling: 0.3704
- ode_coupling_strength: 0.2963
- abm_feedback_gamma: 0.0500
- damping: 0.9293
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1827
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


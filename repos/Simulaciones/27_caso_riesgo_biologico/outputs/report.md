# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-11T04:47:51.259452Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.6206
- bootstrap_mean: 0.6267
- CI 95%: [0.5551, 0.6915]
- weighted_value (LoE factor 0.80): 0.4965
- válido (0.30-0.90): True
- detrended_edi: 0.6206
- trend_ratio: 1.000
- trend_r2: 0.602

### Symploké y CR
- internal: 0.9992
- external: 0.9867
- CR: 1.0126
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9478
- rmse_abm_no_ode: 1.7022
- rmse_ode: 0.7349
- rmse_reduced: 2.4983
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3468
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5343
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7421
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6596
- bootstrap_mean: 0.6630
- CI 95%: [0.5602, 0.8040]
- weighted_value (LoE factor 0.80): 0.5276
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9981
- CR: 1.0018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7202
- rmse_abm_no_ode: 0.8043
- rmse_ode: 1.0808
- rmse_reduced: 2.1156
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9788
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6186
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1916
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


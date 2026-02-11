# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-11T05:03:15.260268Z

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
- internal: 0.9995
- external: 0.9868
- CR: 1.0128
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9478
- rmse_abm_no_ode: 1.7030
- rmse_ode: 0.7350
- rmse_reduced: 2.4982
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3520
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5293
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7420
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6590
- bootstrap_mean: 0.6625
- CI 95%: [0.5594, 0.8039]
- weighted_value (LoE factor 0.80): 0.5272
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9980
- CR: 1.0019
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7214
- rmse_abm_no_ode: 0.8061
- rmse_ode: 1.0808
- rmse_reduced: 2.1157
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6083
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1915
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


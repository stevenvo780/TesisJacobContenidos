# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-11T02:08:45.609916Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5471
- bootstrap_mean: 0.5505
- CI 95%: [0.4700, 0.6115]
- weighted_value (LoE factor 0.80): 0.4377
- válido (0.30-0.90): True
- detrended_edi: 0.5471
- trend_ratio: 1.000
- trend_r2: 0.602

### Symploké y CR
- internal: 0.9994
- external: 0.9886
- CR: 1.0110
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1316
- rmse_abm_no_ode: 1.6996
- rmse_ode: 0.7416
- rmse_reduced: 2.4984
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3958
- macro_coupling: 0.3959
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5650
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7402
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7055
- bootstrap_mean: 0.7144
- CI 95%: [0.6263, 0.7975]
- weighted_value (LoE factor 0.80): 0.5644
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9978
- CR: 1.0021
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6230
- rmse_abm_no_ode: 0.6820
- rmse_ode: 1.0941
- rmse_reduced: 2.1155
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9700
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.5862
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1928
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


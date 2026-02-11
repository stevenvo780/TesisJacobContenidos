# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-11T01:56:27.630284Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5781
- bootstrap_mean: 0.5824
- CI 95%: [0.5109, 0.6448]
- weighted_value (LoE factor 0.80): 0.4625
- válido (0.30-0.90): True
- detrended_edi: 0.5781
- trend_ratio: 1.000
- trend_r2: 0.602

### Symploké y CR
- internal: 0.9994
- external: 0.9864
- CR: 1.0132
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0541
- rmse_abm_no_ode: 1.7488
- rmse_ode: 0.7397
- rmse_reduced: 2.4983
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3435
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5342
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7425
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7118
- bootstrap_mean: 0.7149
- CI 95%: [0.6369, 0.8102]
- weighted_value (LoE factor 0.80): 0.5694
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
- rmse_abm: 0.6098
- rmse_abm_no_ode: 0.6639
- rmse_ode: 1.0948
- rmse_reduced: 2.1156
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9771
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6208
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1918
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


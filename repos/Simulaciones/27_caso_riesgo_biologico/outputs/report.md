# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-10T04:15:40.604714Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3763
- bootstrap_mean: 0.3795
- CI 95%: [0.3044, 0.4457]
- weighted_value (LoE factor 0.80): 0.3011
- válido (0.30-0.90): True
- detrended_edi: 0.3763
- trend_ratio: 1.000
- trend_r2: 0.602

### Symploké y CR
- internal: 0.9992
- external: 0.9880
- CR: 1.0114
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0524
- rmse_abm_no_ode: 1.6874
- rmse_ode: 0.7393
- rmse_reduced: 2.4983
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3998
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5796
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7400
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0813
- bootstrap_mean: 0.0701
- CI 95%: [-0.0559, 0.1251]
- weighted_value (LoE factor 0.80): 0.0651
- válido (0.30-0.90): False

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
- rmse_abm: 0.6089
- rmse_abm_no_ode: 0.6628
- rmse_ode: 1.0949
- rmse_reduced: 2.1156
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9778
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6211
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1919
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


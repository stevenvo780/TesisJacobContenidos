# Reporte de Validación — Paradigmas Cientificos (Ising)

- generated_at: 2026-02-11T02:08:55.043380Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8135
- bootstrap_mean: 0.8133
- CI 95%: [0.8035, 0.8258]
- weighted_value (LoE factor 0.20): 0.1627
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9986
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3913
- rmse_abm_no_ode: 0.5063
- rmse_ode: 0.6294
- rmse_reduced: 2.0980
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2163
- ode_coupling_strength: 0.1730
- abm_feedback_gamma: 0.0500
- damping: 0.7749
- ode_alpha: 0.0312
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4739
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0299
- bootstrap_mean: -0.0329
- CI 95%: [-0.0513, -0.0269]
- weighted_value (LoE factor 0.20): -0.0060
- válido (0.30-0.90): False
- detrended_edi: -0.0299
- trend_ratio: 1.000
- trend_r2: 0.902

### Symploké y CR
- internal: 0.9911
- external: 0.9930
- CR: 0.9980
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.1987
- rmse_abm_no_ode: 9.1593
- rmse_ode: 9.4230
- rmse_reduced: 8.9314
- threshold: 5.7385

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1551
- ode_coupling_strength: 0.1241
- abm_feedback_gamma: 0.0500
- damping: 0.8974
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8163
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


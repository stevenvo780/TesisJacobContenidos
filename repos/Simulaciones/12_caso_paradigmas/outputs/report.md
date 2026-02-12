# Reporte de Validación — Paradigmas Científicos (R&D)

- generated_at: 2026-02-12T04:00:58.075092Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1441
- bootstrap_mean: -0.1486
- CI 95%: [-0.2072, -0.1074]
- weighted_value (LoE factor 0.60): -0.0864
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9993
- external: 0.9985
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5991
- rmse_abm_no_ode: 0.5237
- rmse_ode: 1.1051
- rmse_reduced: 2.1937
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8449
- ode_alpha: 0.4295
- ode_beta: 0.8315
- assimilation_strength: 0.0000
- calibration_rmse: 0.6517
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0060
- bootstrap_mean: -0.0069
- CI 95%: [-0.0141, -0.0043]
- weighted_value (LoE factor 0.60): -0.0036
- válido (0.30-0.90): False
- detrended_edi: -0.0060
- trend_ratio: 1.000
- trend_r2: 0.902

### Symploké y CR
- internal: 0.9413
- external: 0.9141
- CR: 1.0298
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.2452
- rmse_abm_no_ode: 9.1896
- rmse_ode: 9.3280
- rmse_reduced: 8.9315
- threshold: 5.7385

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8140
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


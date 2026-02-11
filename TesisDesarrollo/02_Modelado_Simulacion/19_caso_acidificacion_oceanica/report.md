# Reporte de Validación — Acidificación Oceánica

- generated_at: 2026-02-11T19:28:22.371545Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0207
- bootstrap_mean: -0.0212
- CI 95%: [-0.0349, -0.0103]
- weighted_value (LoE factor 0.60): -0.0124
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9995
- external: 0.8947
- CR: 1.1172
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6897
- rmse_abm_no_ode: 1.6554
- rmse_ode: 3.0983
- rmse_reduced: 1.4609
- threshold: 0.8168

### Calibración
- forcing_scale: 0.7852
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5870
- ode_alpha: 0.4549
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5304
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0003
- bootstrap_mean: -0.0005
- CI 95%: [-0.0017, 0.0000]
- weighted_value (LoE factor 0.60): -0.0002
- válido (0.30-0.90): False
- detrended_edi: -0.0003
- trend_ratio: 1.000
- trend_r2: 0.861

### Symploké y CR
- internal: 0.9993
- external: 0.8234
- CR: 1.2136
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3466
- rmse_abm_no_ode: 3.3455
- rmse_ode: 3.3420
- rmse_reduced: 3.3074
- threshold: 2.3256

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5529
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5571
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


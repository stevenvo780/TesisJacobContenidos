# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz Prestige)

- generated_at: 2026-02-12T01:19:52.698172Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0206
- bootstrap_mean: -0.0213
- CI 95%: [-0.0283, -0.0178]
- weighted_value (LoE factor 0.60): -0.0124
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9902
- external: 0.9902
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1241
- rmse_abm_no_ode: 2.0812
- rmse_ode: 2.4919
- rmse_reduced: 2.1953
- threshold: 0.9184

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9150
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.9884
- bootstrap_mean: -1.1545
- CI 95%: [-2.3975, -0.5957]
- weighted_value (LoE factor 0.60): -0.5930
- válido (0.30-0.90): False
- detrended_edi: -0.9884
- trend_ratio: 1.000
- trend_r2: 0.988

### Symploké y CR
- internal: 0.9992
- external: 0.9988
- CR: 1.0004
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4762
- rmse_abm_no_ode: 0.2395
- rmse_ode: 2.6994
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.2716
- ode_coupling_strength: 0.2172
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1733
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


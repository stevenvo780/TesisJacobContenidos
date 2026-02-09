# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-09T23:02:00.890051Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4076
- bootstrap_mean: -0.4077
- CI 95%: [-0.4132, -0.4036]
- weighted_value (LoE factor 0.20): -0.0815
- válido (0.30-0.90): False
- detrended_edi: -0.4076
- trend_ratio: 1.000
- trend_r2: 0.554

### Symploké y CR
- internal: 0.7972
- external: 0.6751
- CR: 1.1807
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 847066.3355
- rmse_abm_no_ode: 601775.7444
- rmse_ode: 7.3220
- rmse_reduced: 627276.0876
- threshold: 3.9363

### Calibración
- forcing_scale: 0.0507
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.1645
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 141876.0853
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.4203
- bootstrap_mean: -0.4205
- CI 95%: [-0.4306, -0.4134]
- weighted_value (LoE factor 0.20): -0.0841
- válido (0.30-0.90): False
- detrended_edi: -0.4203
- trend_ratio: 1.000
- trend_r2: 0.932

### Symploké y CR
- internal: 0.7987
- external: 0.6636
- CR: 1.2035
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 847272.1862
- rmse_abm_no_ode: 596565.0502
- rmse_ode: 15.2845
- rmse_reduced: 627287.1330
- threshold: 0.5326

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 136237.3317
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.


# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T20:56:06.780130Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3804
- bootstrap_mean: 0.3812
- CI 95%: [0.3664, 0.4001]
- weighted_value (LoE factor 0.60): 0.2283
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9955
- CR: 1.0045
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8141
- rmse_abm_no_ode: 1.3141
- rmse_ode: 0.6310
- rmse_reduced: 1.4367
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3130
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3029
- ode_alpha: 0.0059
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1401
- ode_rolling: None

### Interpretación
Categoría de emergencia: **trend**. No se detecta estructura macro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1788
- bootstrap_mean: -0.1785
- CI 95%: [-0.1938, -0.1629]
- weighted_value (LoE factor 0.60): -0.1073
- válido (0.30-0.90): False
- detrended_edi: -0.1788
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 0.9999
- external: 0.9987
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 22.0587
- rmse_abm_no_ode: 18.7135
- rmse_ode: 29.2853
- rmse_reduced: 35.7618
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5410
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.


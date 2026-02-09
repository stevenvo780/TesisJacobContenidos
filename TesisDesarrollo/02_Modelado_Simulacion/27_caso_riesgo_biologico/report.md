# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-09T20:55:56.762533Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.4425
- bootstrap_mean: 0.4478
- CI 95%: [0.3731, 0.5266]
- weighted_value (LoE factor 0.80): 0.3540
- válido (0.30-0.90): True
- detrended_edi: 0.4425
- trend_ratio: 1.000
- trend_r2: 0.602

### Symploké y CR
- internal: 0.9995
- external: 0.9869
- CR: 1.0127
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9485
- rmse_abm_no_ode: 1.7013
- rmse_ode: 0.7350
- rmse_reduced: 2.4982
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3542
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5317
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7419
- ode_rolling: None

### Interpretación
Los resultados **sugieren** emergencia macro significativa. El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística. No obstante, estos resultados deben interpretarse en el contexto de las limitaciones del proxy utilizado y del nivel de evidencia (LoE) del caso.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -9.5875
- CI 95%: [-14.2341, -7.2058]
- weighted_value (LoE factor 0.80): -0.8000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9985
- external: 0.9911
- CR: 1.0075
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5679
- rmse_abm_no_ode: 0.0558
- rmse_ode: 2.7807
- rmse_reduced: 2.1157
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6466
- ode_alpha: 0.0243
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0938
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.


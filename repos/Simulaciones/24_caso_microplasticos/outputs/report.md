# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-11T01:53:06.100356Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0897
- bootstrap_mean: -0.0891
- CI 95%: [-0.1496, -0.0274]
- weighted_value (LoE factor 0.80): -0.0717
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9975
- CR: 1.0025
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0554
- rmse_abm_no_ode: 1.5456
- rmse_ode: 1.7336
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.7517
- macro_coupling: 0.3701
- ode_coupling_strength: 0.2961
- abm_feedback_gamma: 0.0500
- damping: 0.7521
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2157
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.0190
- CI 95%: [-1.1892, -0.7644]
- weighted_value (LoE factor 0.80): -0.8000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9983
- CR: 1.0017
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.2274
- rmse_abm_no_ode: 16.2876
- rmse_ode: 2.7713
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7301
- macro_coupling: 0.4978
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4298
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3881
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


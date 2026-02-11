# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-11T02:09:11.228356Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.5456
- bootstrap_mean: -0.5495
- CI 95%: [-0.6303, -0.4797]
- weighted_value (LoE factor 0.80): -0.4365
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4969
- rmse_abm_no_ode: 1.5804
- rmse_ode: 1.6887
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.8930
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8813
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2155
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.1943
- CI 95%: [-2.4315, -1.7942]
- weighted_value (LoE factor 0.80): -0.8000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9988
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 14.7306
- rmse_abm_no_ode: 16.8427
- rmse_ode: 2.9360
- rmse_reduced: 4.5302
- threshold: 1.4633

### Calibración
- forcing_scale: 0.8660
- macro_coupling: 0.0974
- ode_coupling_strength: 0.0779
- abm_feedback_gamma: 0.0500
- damping: 0.5042
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3903
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


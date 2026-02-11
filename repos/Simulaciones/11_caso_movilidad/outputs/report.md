# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-11T04:42:09.973643Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -3.0333
- CI 95%: [-3.6187, -2.4163]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.2021
- CR: 4.9483
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0291
- rmse_abm_no_ode: 0.5061
- rmse_ode: 31.9070
- rmse_reduced: 0.5061
- threshold: 0.4998

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7730
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9980
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3847
- bootstrap_mean: -0.4002
- CI 95%: [-0.7702, -0.1416]
- weighted_value (LoE factor 0.20): -0.0769
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9963
- external: 0.2454
- CR: 4.0603
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.7072
- rmse_abm_no_ode: 1.4066
- rmse_ode: 11.3234
- rmse_reduced: 4.8437
- threshold: 1.8501

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4942
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6693
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 0.1471
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


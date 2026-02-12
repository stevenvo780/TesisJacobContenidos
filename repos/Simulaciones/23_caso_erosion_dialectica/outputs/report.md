# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz Prestige)

- generated_at: 2026-02-12T04:07:18.929453Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0190
- bootstrap_mean: -0.0194
- CI 95%: [-0.0237, -0.0170]
- weighted_value (LoE factor 0.60): -0.0114
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9918
- external: 0.9927
- CR: 0.9991
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0811
- rmse_abm_no_ode: 2.0423
- rmse_ode: 2.4676
- rmse_reduced: 2.1953
- threshold: 0.9184

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9103
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.9591
- CI 95%: [-3.3097, -1.0475]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.988

### Symploké y CR
- internal: 0.9967
- external: 0.9957
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4183
- rmse_abm_no_ode: 0.1472
- rmse_ode: 2.7257
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1612
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


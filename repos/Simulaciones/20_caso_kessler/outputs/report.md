# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-10T12:58:03.021481Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.9548
- CI 95%: [-3.0872, -2.8009]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.554

### Symploké y CR
- internal: 0.8216
- external: 0.7111
- CR: 1.1555
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2603547.5905
- rmse_abm_no_ode: 657132.3710
- rmse_ode: 7.3220
- rmse_reduced: 627276.0876
- threshold: 3.9363

### Calibración
- forcing_scale: 0.6916
- macro_coupling: 0.4658
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7095
- ode_alpha: 0.1645
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2572
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -3.1675
- CI 95%: [-3.3021, -3.0119]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.932

### Symploké y CR
- internal: 0.8233
- external: 0.6966
- CR: 1.1819
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2660593.4212
- rmse_abm_no_ode: 637285.7117
- rmse_ode: 15.2845
- rmse_reduced: 627287.1330
- threshold: 0.5326

### Calibración
- forcing_scale: 0.6617
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7007
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2058
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


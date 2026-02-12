# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-12T03:58:13.417681Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4051
- bootstrap_mean: -0.4062
- CI 95%: [-0.4379, -0.3781]
- weighted_value (LoE factor 1.00): -0.4051
- válido (0.30-0.90): False
- detrended_edi: -0.4051
- trend_ratio: 1.000
- trend_r2: 0.632

### Symploké y CR
- internal: 1.0000
- external: 0.9987
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8178
- rmse_abm_no_ode: 0.5821
- rmse_ode: 1.1702
- rmse_reduced: 1.5603
- threshold: 0.4260

### Calibración
- forcing_scale: 0.2196
- macro_coupling: 0.2247
- ode_coupling_strength: 0.1798
- abm_feedback_gamma: 0.0500
- damping: 0.2468
- ode_alpha: 0.0351
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3208
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0813
- bootstrap_mean: 0.0813
- CI 95%: [0.0794, 0.0834]
- weighted_value (LoE factor 1.00): 0.0813
- válido (0.30-0.90): False
- detrended_edi: 0.0813
- trend_ratio: 1.000
- trend_r2: 0.979

### Symploké y CR
- internal: 0.9994
- external: 0.3821
- CR: 2.6158
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9535
- rmse_abm_no_ode: 3.2147
- rmse_ode: 4.4047
- rmse_reduced: 3.2176
- threshold: 1.1814

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.0284
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6732
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


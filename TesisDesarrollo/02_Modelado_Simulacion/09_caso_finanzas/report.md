# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-11T17:30:06.650272Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2729
- bootstrap_mean: -0.2738
- CI 95%: [-0.2922, -0.2577]
- weighted_value (LoE factor 1.00): -0.2729
- válido (0.30-0.90): False
- detrended_edi: -0.2729
- trend_ratio: 1.000
- trend_r2: 0.648

### Symploké y CR
- internal: 1.0000
- external: 0.9974
- CR: 1.0026
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7429
- rmse_abm_no_ode: 0.5836
- rmse_ode: 1.2166
- rmse_reduced: 1.5303
- threshold: 0.4120

### Calibración
- forcing_scale: 0.2109
- macro_coupling: 0.1343
- ode_coupling_strength: 0.1075
- abm_feedback_gamma: 0.0500
- damping: 0.2426
- ode_alpha: 0.0393
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3174
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0812
- bootstrap_mean: 0.0812
- CI 95%: [0.0793, 0.0833]
- weighted_value (LoE factor 1.00): 0.0812
- válido (0.30-0.90): False
- detrended_edi: 0.0812
- trend_ratio: 1.000
- trend_r2: 0.979

### Symploké y CR
- internal: 0.9994
- external: 0.3820
- CR: 2.6162
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9537
- rmse_abm_no_ode: 3.2147
- rmse_ode: 4.4040
- rmse_reduced: 3.2176
- threshold: 1.1814

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.0285
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6731
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


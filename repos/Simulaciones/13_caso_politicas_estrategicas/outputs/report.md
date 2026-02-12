# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-12T04:01:43.023524Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0153
- bootstrap_mean: -0.0909
- CI 95%: [-0.9773, 0.4523]
- weighted_value (LoE factor 0.60): -0.0092
- válido (0.30-0.90): False
- detrended_edi: -0.0153
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9970
- external: 0.9868
- CR: 1.0103
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1944
- rmse_abm_no_ode: 0.1914
- rmse_ode: 0.5982
- rmse_reduced: 2.5670
- threshold: 0.2856

### Calibración
- forcing_scale: 0.9452
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7979
- ode_alpha: 0.2951
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2330
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2885
- bootstrap_mean: 0.2878
- CI 95%: [0.2476, 0.3228]
- weighted_value (LoE factor 0.60): 0.1731
- válido (0.30-0.90): False
- detrended_edi: 0.2885
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9983
- external: 0.9898
- CR: 1.0086
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5170
- rmse_abm_no_ode: 0.7265
- rmse_ode: 0.9059
- rmse_reduced: 0.9596
- threshold: 0.1452

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9267
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3608
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


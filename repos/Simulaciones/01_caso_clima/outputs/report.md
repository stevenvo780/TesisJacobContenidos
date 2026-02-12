# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-12T03:56:22.247086Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0089
- bootstrap_mean: 0.0089
- CI 95%: [0.0084, 0.0095]
- weighted_value (LoE factor 1.00): 0.0089
- válido (0.30-0.90): False
- detrended_edi: 0.0089
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9541
- rmse_abm_no_ode: 3.9895
- rmse_ode: 2.9654
- rmse_reduced: 7.0524
- threshold: 2.7786

### Calibración
- forcing_scale: 0.8668
- macro_coupling: 0.2593
- ode_coupling_strength: 0.2074
- abm_feedback_gamma: 0.0500
- damping: 0.8515
- ode_alpha: 0.1600
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1864
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0111
- bootstrap_mean: 0.0113
- CI 95%: [-0.0033, 0.0284]
- weighted_value (LoE factor 1.00): 0.0111
- válido (0.30-0.90): False
- detrended_edi: 0.0111
- trend_ratio: 1.000
- trend_r2: 0.525

### Symploké y CR
- internal: 1.0000
- external: 0.9948
- CR: 1.0052
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8629
- rmse_abm_no_ode: 0.8725
- rmse_ode: 0.8646
- rmse_reduced: 2.4944
- threshold: 1.1902

### Calibración
- forcing_scale: 0.1814
- macro_coupling: 0.1452
- ode_coupling_strength: 0.1161
- abm_feedback_gamma: 0.0500
- damping: 0.1082
- ode_alpha: 0.4014
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7386
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


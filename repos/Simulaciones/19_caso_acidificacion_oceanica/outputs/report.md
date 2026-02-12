# Reporte de Validación — Acidificación Oceánica

- generated_at: 2026-02-12T04:05:02.571571Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [-0.0000, 0.0001]
- weighted_value (LoE factor 0.60): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9991
- external: 0.8056
- CR: 1.2403
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7821
- rmse_abm_no_ode: 1.7822
- rmse_ode: 1.3945
- rmse_reduced: 1.7741
- threshold: 1.0725

### Calibración
- forcing_scale: 0.6615
- macro_coupling: 0.1958
- ode_coupling_strength: 0.1566
- abm_feedback_gamma: 0.0500
- damping: 0.1189
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0028
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0002
- bootstrap_mean: -0.0003
- CI 95%: [-0.0008, -0.0000]
- weighted_value (LoE factor 0.60): -0.0001
- válido (0.30-0.90): False
- detrended_edi: -0.0002
- trend_ratio: 1.000
- trend_r2: 0.861

### Symploké y CR
- internal: 0.9992
- external: 0.8328
- CR: 1.1999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3460
- rmse_abm_no_ode: 3.3455
- rmse_ode: 3.3426
- rmse_reduced: 3.3074
- threshold: 2.3256

### Calibración
- forcing_scale: 0.8828
- macro_coupling: 0.2342
- ode_coupling_strength: 0.1873
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9480
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


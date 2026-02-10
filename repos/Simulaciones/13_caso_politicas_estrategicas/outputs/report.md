# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-10T04:18:01.619667Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0040
- bootstrap_mean: 0.0040
- CI 95%: [0.0036, 0.0044]
- weighted_value (LoE factor 0.20): 0.0008
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9524
- external: 0.8615
- CR: 1.1055
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3955
- rmse_abm_no_ode: 1.4011
- rmse_ode: 0.5469
- rmse_reduced: 1.3994
- threshold: 0.3900

### Calibración
- forcing_scale: 0.6920
- macro_coupling: 0.3953
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6933
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2945
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0197
- bootstrap_mean: -0.0197
- CI 95%: [-0.0211, -0.0186]
- weighted_value (LoE factor 0.20): -0.0039
- válido (0.30-0.90): False
- detrended_edi: -0.0197
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.5240
- external: -0.3098
- CR: 1.6917
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8734
- rmse_abm_no_ode: 1.8372
- rmse_ode: 1.0069
- rmse_reduced: 1.8293
- threshold: 0.1452

### Calibración
- forcing_scale: 0.7329
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7060
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3710
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


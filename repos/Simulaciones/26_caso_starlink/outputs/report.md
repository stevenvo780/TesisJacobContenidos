# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-10T02:13:36.300448Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6336
- bootstrap_mean: 0.6329
- CI 95%: [0.5642, 0.7024]
- weighted_value (LoE factor 0.80): 0.5069
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9766
- CR: 1.0240
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4030
- rmse_abm_no_ode: 1.0997
- rmse_ode: 0.7799
- rmse_reduced: 0.6953
- threshold: 0.1000

### Calibración
- forcing_scale: 0.1652
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1655
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3349
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -520.3016
- CI 95%: [-587.7953, -456.5154]
- weighted_value (LoE factor 0.80): -0.8000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 1.000

### Symploké y CR
- internal: 0.9865
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0661
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.6290
- rmse_reduced: 0.0001
- threshold: 0.1000

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1071
- ode_coupling_strength: 0.0857
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0002
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


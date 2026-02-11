# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-11T23:32:14.381599Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False
- detrended_edi: 0.0000
- trend_ratio: 1.000
- trend_r2: 0.983

### Symploké y CR
- internal: 0.9891
- external: -0.2476
- CR: 3.9952
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 38.3760
- rmse_abm_no_ode: 38.3760
- rmse_ode: 12.7765
- rmse_reduced: 38.3355
- threshold: 2.7339

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0000
- ode_coupling_strength: 0.0000
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.1789
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 20.5869
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False
- detrended_edi: 0.0000
- trend_ratio: 1.000
- trend_r2: 0.504

### Symploké y CR
- internal: 0.9953
- external: -0.3528
- CR: 2.8208
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 41.6071
- rmse_abm_no_ode: 41.6071
- rmse_ode: 8.5470
- rmse_reduced: 41.6175
- threshold: 1.1883

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0000
- ode_coupling_strength: 0.0000
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.3657
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 27.6988
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-10T05:37:03.121786Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3156
- bootstrap_mean: 0.3085
- CI 95%: [0.1859, 0.3967]
- weighted_value (LoE factor 0.20): 0.0631
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0014
- external: 0.0012
- CR: 1.1579
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6525
- rmse_abm_no_ode: 0.9535
- rmse_ode: 0.4871
- rmse_reduced: 15.2230
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9464
- macro_coupling: 0.3235
- ode_coupling_strength: 0.2588
- abm_feedback_gamma: 0.0500
- damping: 0.5701
- ode_alpha: 0.0068
- ode_beta: 0.8095
- assimilation_strength: 0.0000
- calibration_rmse: 0.4880
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: -0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 4.5221
- rmse_abm_no_ode: 4.5221
- rmse_ode: 15.0854
- rmse_reduced: 13.8782
- threshold: 4.3680

### Calibración
- forcing_scale: 0.9852
- macro_coupling: 0.3711
- ode_coupling_strength: 0.2969
- abm_feedback_gamma: 0.0500
- damping: 0.8870
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4393
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


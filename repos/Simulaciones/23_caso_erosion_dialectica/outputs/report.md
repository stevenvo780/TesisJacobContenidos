# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-10T01:23:00.943138Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0471
- bootstrap_mean: 0.0471
- CI 95%: [0.0460, 0.0484]
- weighted_value (LoE factor 0.60): 0.0283
- válido (0.30-0.90): False
- detrended_edi: 0.0471
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 1.0000
- external: 0.9992
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9515
- rmse_abm_no_ode: 4.1468
- rmse_ode: 1.9042
- rmse_reduced: 6.8364
- threshold: 2.5948

### Calibración
- forcing_scale: 0.6455
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6226
- ode_alpha: 0.0310
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1941
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -3.8504
- CI 95%: [-4.3526, -3.2359]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.988

### Symploké y CR
- internal: 0.9975
- external: 0.9968
- CR: 1.0007
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9831
- rmse_abm_no_ode: 0.2030
- rmse_ode: 3.6060
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6882
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1477
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


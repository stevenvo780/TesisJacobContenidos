# Reporte de Validación — Kessler (Debris Orbital)

- generated_at: 2026-02-12T04:05:37.055275Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1388
- bootstrap_mean: -0.1369
- CI 95%: [-0.2414, 0.0067]
- weighted_value (LoE factor 0.60): -0.0833
- válido (0.30-0.90): False
- detrended_edi: -0.1388
- trend_ratio: 1.000
- trend_r2: 0.851

### Symploké y CR
- internal: 0.9981
- external: 0.9968
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7454
- rmse_abm_no_ode: 0.6545
- rmse_ode: 0.7637
- rmse_reduced: 1.9713
- threshold: 0.8260

### Calibración
- forcing_scale: 0.8573
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.2323
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4019
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2987
- bootstrap_mean: 0.3131
- CI 95%: [0.2607, 0.4381]
- weighted_value (LoE factor 0.60): 0.1792
- válido (0.30-0.90): False
- detrended_edi: 0.2987
- trend_ratio: 1.000
- trend_r2: 0.872

### Symploké y CR
- internal: 0.9992
- external: 0.9966
- CR: 1.0026
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7051
- rmse_abm_no_ode: 1.0053
- rmse_ode: 3.4449
- rmse_reduced: 3.2710
- threshold: 0.9270

### Calibración
- forcing_scale: 0.8797
- macro_coupling: 0.4837
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1482
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


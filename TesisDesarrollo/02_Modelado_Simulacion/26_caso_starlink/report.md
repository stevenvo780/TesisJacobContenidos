# Reporte de Validación — Constelaciones Satelitales Starlink (Saturation Growth)

- generated_at: 2026-02-12T00:19:07.660163Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.3923
- bootstrap_mean: -0.3929
- CI 95%: [-0.4096, -0.3766]
- weighted_value (LoE factor 0.60): -0.2354
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9988
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0349
- rmse_abm_no_ode: 0.7433
- rmse_ode: 1.1911
- rmse_reduced: 0.8690
- threshold: 0.1419

### Calibración
- forcing_scale: 0.1800
- macro_coupling: 0.3636
- ode_coupling_strength: 0.2909
- abm_feedback_gamma: 0.0500
- damping: 0.1840
- ode_alpha: 0.0380
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3267
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.8371
- bootstrap_mean: 0.8371
- CI 95%: [0.8371, 0.8371]
- weighted_value (LoE factor 0.60): 0.5023
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.5541
- CR: 1.8047
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1335
- rmse_abm_no_ode: 0.8194
- rmse_ode: 2.1230
- rmse_reduced: 0.9174
- threshold: 0.1000

### Calibración
- forcing_scale: 0.6000
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2000
- ode_alpha: 0.0069
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5056
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


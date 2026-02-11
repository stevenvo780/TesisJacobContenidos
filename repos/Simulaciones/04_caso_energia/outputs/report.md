# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-11T00:51:22.799491Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0388
- bootstrap_mean: 0.0388
- CI 95%: [0.0294, 0.0474]
- weighted_value (LoE factor 0.20): 0.0078
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9660
- external: 0.9500
- CR: 1.0168
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3796
- rmse_abm_no_ode: 0.3949
- rmse_ode: 0.4429
- rmse_reduced: 0.3953
- threshold: 0.3269

### Calibración
- forcing_scale: 0.1573
- macro_coupling: 0.1151
- ode_coupling_strength: 0.0920
- abm_feedback_gamma: 0.0500
- damping: 0.1948
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4887
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0150
- bootstrap_mean: -0.0151
- CI 95%: [-0.0179, -0.0125]
- weighted_value (LoE factor 0.20): -0.0030
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9290
- external: -0.8040
- CR: 1.1556
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6290
- rmse_abm_no_ode: 1.6049
- rmse_ode: 2.0513
- rmse_reduced: 1.6049
- threshold: 1.2251

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3437
- ode_coupling_strength: 0.2749
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.6871
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


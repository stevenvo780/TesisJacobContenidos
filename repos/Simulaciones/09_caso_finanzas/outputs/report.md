# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-10T01:20:05.225384Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, -0.0000]
- weighted_value (LoE factor 1.00): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.9874
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 20481509.7124
- rmse_abm_no_ode: 20481508.8624
- rmse_ode: 20481525.7721
- rmse_reduced: 20481508.9052
- threshold: 19219447.7270

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0012
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 4.7318
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0398
- bootstrap_mean: 0.0398
- CI 95%: [0.0388, 0.0410]
- weighted_value (LoE factor 1.00): 0.0398
- válido (0.30-0.90): False
- detrended_edi: 0.0398
- trend_ratio: 1.000
- trend_r2: 0.979

### Symploké y CR
- internal: 0.0000
- external: 0.9850
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 36.4203
- rmse_abm_no_ode: 37.9317
- rmse_ode: 11.2064
- rmse_reduced: 37.5564
- threshold: 1.1814

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 10.2667
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-10T06:23:00.655705Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0627
- bootstrap_mean: 0.0637
- CI 95%: [0.0524, 0.0760]
- weighted_value (LoE factor 0.60): 0.0376
- válido (0.30-0.90): False
- detrended_edi: 0.0627
- trend_ratio: 1.000
- trend_r2: 0.854

### Symploké y CR
- internal: 0.9999
- external: 0.9998
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6660
- rmse_abm_no_ode: 0.7105
- rmse_ode: 1.0472
- rmse_reduced: 2.9447
- threshold: 0.6860

### Calibración
- forcing_scale: 0.8930
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8813
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2994
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0151
- bootstrap_mean: 0.0152
- CI 95%: [0.0137, 0.0168]
- weighted_value (LoE factor 0.60): 0.0091
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9987
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1673
- rmse_abm_no_ode: 2.2005
- rmse_ode: 3.4992
- rmse_reduced: 2.2008
- threshold: 0.4144

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1643
- ode_coupling_strength: 0.1315
- abm_feedback_gamma: 0.0500
- damping: 0.1052
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7982
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


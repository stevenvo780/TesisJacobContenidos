# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-11T01:55:58.730777Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9112
- bootstrap_mean: 0.9113
- CI 95%: [0.9043, 0.9188]
- weighted_value (LoE factor 0.80): 0.7289
- válido (0.30-0.90): False
- detrended_edi: 0.9112
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 0.9997
- external: 0.9986
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2862
- rmse_abm_no_ode: 0.4971
- rmse_ode: 0.2029
- rmse_reduced: 3.2218
- threshold: 0.6792

### Calibración
- forcing_scale: 0.7721
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7822
- ode_alpha: 0.1384
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1633
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4699
- bootstrap_mean: 0.4699
- CI 95%: [0.4699, 0.4699]
- weighted_value (LoE factor 0.80): 0.3759
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.6173
- CR: 1.6198
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1420
- rmse_abm_no_ode: 0.7187
- rmse_ode: 3.4628
- rmse_reduced: 4.0410
- threshold: 0.1000

### Calibración
- forcing_scale: 0.4515
- macro_coupling: 0.2306
- ode_coupling_strength: 0.1845
- abm_feedback_gamma: 0.0500
- damping: 0.1512
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4043
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


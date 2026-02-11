# Reporte de Validación — Wikipedia (Axelrod + Lotka-Volterra)

- generated_at: 2026-02-11T05:14:31.407038Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2278
- bootstrap_mean: -0.2275
- CI 95%: [-0.2416, -0.2127]
- weighted_value (LoE factor 0.20): -0.0456
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8690
- CR: 1.1507
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4388
- rmse_abm_no_ode: 1.3855
- rmse_ode: 1.8593
- rmse_reduced: 1.1718
- threshold: 1.0224

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4928
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4456
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2310
- bootstrap_mean: 0.2652
- CI 95%: [0.1466, 0.3909]
- weighted_value (LoE factor 0.20): 0.0462
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9936
- CR: 1.0054
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.5781
- rmse_abm_no_ode: 2.5196
- rmse_ode: 3.5984
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7216
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8449
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


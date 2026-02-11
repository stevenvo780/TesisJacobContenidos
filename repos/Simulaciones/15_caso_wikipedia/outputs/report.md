# Reporte de Validación — Wikipedia (Axelrod + Lotka-Volterra)

- generated_at: 2026-02-11T04:43:37.200705Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2252
- bootstrap_mean: -0.2248
- CI 95%: [-0.2383, -0.2101]
- weighted_value (LoE factor 0.20): -0.0450
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8805
- CR: 1.1357
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4357
- rmse_abm_no_ode: 1.3856
- rmse_ode: 1.8586
- rmse_reduced: 1.1718
- threshold: 1.0224

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4540
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4932
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4458
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2306
- bootstrap_mean: 0.2570
- CI 95%: [0.1460, 0.3905]
- weighted_value (LoE factor 0.20): 0.0461
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9935
- CR: 1.0055
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.5791
- rmse_abm_no_ode: 2.5204
- rmse_ode: 3.5984
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7233
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8451
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


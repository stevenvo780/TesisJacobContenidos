# Reporte de Validación — Wikipedia (Axelrod + Lotka-Volterra)

- generated_at: 2026-02-11T02:09:57.183052Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2164
- bootstrap_mean: -0.2163
- CI 95%: [-0.2275, -0.2008]
- weighted_value (LoE factor 0.20): -0.0433
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9075
- CR: 1.1018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4254
- rmse_abm_no_ode: 1.3821
- rmse_ode: 1.8566
- rmse_reduced: 1.1718
- threshold: 1.0224

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3324
- ode_coupling_strength: 0.2660
- abm_feedback_gamma: 0.0500
- damping: 0.4613
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4477
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2121
- bootstrap_mean: 0.2584
- CI 95%: [0.1406, 0.3621]
- weighted_value (LoE factor 0.20): 0.0424
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
- rmse_abm: 2.6413
- rmse_abm_no_ode: 2.5618
- rmse_ode: 3.6028
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0698
- ode_coupling_strength: 0.0558
- abm_feedback_gamma: 0.0500
- damping: 0.7092
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8485
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


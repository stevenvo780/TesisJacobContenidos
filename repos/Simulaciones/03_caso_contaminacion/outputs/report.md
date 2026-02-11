# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-11T02:10:35.805089Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.8750
- CI 95%: [-2.5602, -1.3313]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9999
- CR: 0.9999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.2995
- rmse_abm_no_ode: 2.9640
- rmse_ode: 1.5894
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.6426
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5156
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5730
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0765
- bootstrap_mean: -0.1407
- CI 95%: [-0.6335, 0.1690]
- weighted_value (LoE factor 0.20): -0.0153
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9887
- CR: 1.0104
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5465
- rmse_abm_no_ode: 3.7741
- rmse_ode: 3.0231
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 1.0000
- macro_coupling: 0.4500
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8000
- ode_alpha: 0.0788
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6670
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-11T05:07:23.874325Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.0058
- CI 95%: [-2.7401, -1.4531]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9997
- external: 0.9997
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4171
- rmse_abm_no_ode: 3.0253
- rmse_ode: 1.6583
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.6879
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5750
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5713
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0917
- bootstrap_mean: -0.1394
- CI 95%: [-0.6513, 0.2157]
- weighted_value (LoE factor 0.20): -0.0183
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9875
- CR: 1.0117
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5965
- rmse_abm_no_ode: 3.8447
- rmse_ode: 3.0230
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7713
- ode_alpha: 0.0788
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6631
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


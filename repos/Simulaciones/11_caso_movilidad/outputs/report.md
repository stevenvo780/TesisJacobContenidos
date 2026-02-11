# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-11T00:46:29.148113Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0027
- bootstrap_mean: 0.0027
- CI 95%: [-0.0082, 0.0133]
- weighted_value (LoE factor 0.20): 0.0005
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 89.1685
- rmse_abm_no_ode: 89.4123
- rmse_ode: 32.0368
- rmse_reduced: 89.1702
- threshold: 0.4998

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.4215
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7812
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9979
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 195.5323
- rmse_abm_no_ode: 195.5323
- rmse_ode: 10.2231
- rmse_reduced: 85.8555
- threshold: 1.8501

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3627
- ode_coupling_strength: 0.2902
- abm_feedback_gamma: 0.0500
- damping: 0.6726
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 0.1467
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


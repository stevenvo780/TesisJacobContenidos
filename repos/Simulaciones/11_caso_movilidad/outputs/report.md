# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-11T05:10:22.032587Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -38.2171
- CI 95%: [-43.8263, -32.5183]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9995
- external: 0.2004
- CR: 4.9875
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 19.7374
- rmse_abm_no_ode: 0.5061
- rmse_ode: 31.9730
- rmse_reduced: 0.5061
- threshold: 0.4998

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8000
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9981
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.4323
- bootstrap_mean: -0.4433
- CI 95%: [-0.7884, -0.1797]
- weighted_value (LoE factor 0.20): -0.0865
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9964
- external: 0.2352
- CR: 4.2355
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.9376
- rmse_abm_no_ode: 1.4062
- rmse_ode: 11.4442
- rmse_reduced: 4.8437
- threshold: 1.8501

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6710
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 0.1469
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


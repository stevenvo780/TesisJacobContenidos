# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-09T20:56:59.394622Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0225
- bootstrap_mean: 0.0220
- CI 95%: [0.0002, 0.0427]
- weighted_value (LoE factor 0.20): 0.0045
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 33.8845
- rmse_abm_no_ode: 34.6640
- rmse_ode: 31.9215
- rmse_reduced: 89.1702
- threshold: 0.4998

### Calibración
- forcing_scale: 0.8052
- macro_coupling: 0.0756
- ode_coupling_strength: 0.0605
- abm_feedback_gamma: 0.0500
- damping: 0.1005
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 93.3991
- ode_rolling: None

### Interpretación
Categoría de emergencia: **trend**. No se detecta estructura macro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0033
- bootstrap_mean: 0.0032
- CI 95%: [-0.0045, 0.0118]
- weighted_value (LoE factor 0.20): 0.0007
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 183.4348
- rmse_abm_no_ode: 184.0497
- rmse_ode: 10.0609
- rmse_reduced: 85.8555
- threshold: 1.8501

### Calibración
- forcing_scale: 0.1725
- macro_coupling: 0.1178
- ode_coupling_strength: 0.0943
- abm_feedback_gamma: 0.0500
- damping: 0.0039
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 90.2730
- ode_rolling: None

### Interpretación
Categoría de emergencia: **trend**. No se detecta estructura macro significativa con los datos y parámetros actuales.


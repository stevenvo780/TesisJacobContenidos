# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-12T03:56:27.688807Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0070
- bootstrap_mean: 0.0361
- CI 95%: [-0.1249, 0.3051]
- weighted_value (LoE factor 0.60): -0.0042
- válido (0.30-0.90): False
- detrended_edi: -0.0070
- trend_ratio: 1.000
- trend_r2: 0.606

### Symploké y CR
- internal: 0.6176
- external: 0.7148
- CR: 0.8641
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2021
- rmse_abm_no_ode: 0.2007
- rmse_ode: 1.2629
- rmse_reduced: 0.4364
- threshold: 0.1933

### Calibración
- forcing_scale: 0.1879
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.9127
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1165
- bootstrap_mean: -0.1204
- CI 95%: [-0.1730, -0.0617]
- weighted_value (LoE factor 0.60): -0.0699
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6507
- external: 0.7327
- CR: 0.8880
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8759
- rmse_abm_no_ode: 0.7845
- rmse_ode: 2.1221
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.3493
- macro_coupling: 0.1984
- ode_coupling_strength: 0.1587
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.8710
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


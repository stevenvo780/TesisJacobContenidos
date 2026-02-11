# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-11T00:45:08.323888Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4366
- bootstrap_mean: -0.4378
- CI 95%: [-0.4880, -0.3938]
- weighted_value (LoE factor 0.20): -0.0873
- válido (0.30-0.90): False
- detrended_edi: -0.4366
- trend_ratio: 1.000
- trend_r2: 0.938

### Symploké y CR
- internal: 0.9984
- external: 0.9596
- CR: 1.0404
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3765
- rmse_abm_no_ode: 0.9582
- rmse_ode: 1.5376
- rmse_reduced: 0.9582
- threshold: 0.2854

### Calibración
- forcing_scale: 0.7629
- macro_coupling: 0.4890
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7769
- ode_alpha: 0.0474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1174
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9742
- external: 0.9244
- CR: 1.0540
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8889
- rmse_abm_no_ode: 1.8889
- rmse_ode: 1.5943
- rmse_reduced: 1.8889
- threshold: 0.3262

### Calibración
- forcing_scale: 0.4439
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.3692
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4024
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


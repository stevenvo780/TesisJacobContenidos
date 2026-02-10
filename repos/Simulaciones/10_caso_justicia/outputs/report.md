# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-10T04:21:38.047892Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4441
- bootstrap_mean: -0.4453
- CI 95%: [-0.4941, -0.4021]
- weighted_value (LoE factor 0.20): -0.0888
- válido (0.30-0.90): False
- detrended_edi: -0.4441
- trend_ratio: 1.000
- trend_r2: 0.938

### Symploké y CR
- internal: 0.9984
- external: 0.9597
- CR: 1.0402
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3837
- rmse_abm_no_ode: 0.9582
- rmse_ode: 1.5382
- rmse_reduced: 0.9582
- threshold: 0.2854

### Calibración
- forcing_scale: 0.6106
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6174
- ode_alpha: 0.0474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1190
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
- internal: 0.9724
- external: 0.9203
- CR: 1.0566
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
- forcing_scale: 0.4686
- macro_coupling: 0.0624
- ode_coupling_strength: 0.0499
- abm_feedback_gamma: 0.0500
- damping: 0.3928
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4023
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


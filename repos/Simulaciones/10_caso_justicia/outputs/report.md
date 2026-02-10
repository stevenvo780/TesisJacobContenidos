# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-10T05:29:28.196132Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4441
- bootstrap_mean: -0.4449
- CI 95%: [-0.4915, -0.4033]
- weighted_value (LoE factor 0.20): -0.0888
- válido (0.30-0.90): False
- detrended_edi: -0.4441
- trend_ratio: 1.000
- trend_r2: 0.938

### Symploké y CR
- internal: 0.9984
- external: 0.9598
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
- forcing_scale: 0.5613
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5688
- ode_alpha: 0.0474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1198
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
- internal: 0.9523
- external: 0.8714
- CR: 1.0928
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
- forcing_scale: 0.4881
- macro_coupling: 0.1836
- ode_coupling_strength: 0.1469
- abm_feedback_gamma: 0.0500
- damping: 0.4140
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4026
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


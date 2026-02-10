# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-10T06:33:27.577010Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1388
- bootstrap_mean: -0.1390
- CI 95%: [-0.1489, -0.1288]
- weighted_value (LoE factor 1.00): -0.1388
- válido (0.30-0.90): False
- detrended_edi: -0.1388
- trend_ratio: 1.000
- trend_r2: 0.996

### Symploké y CR
- internal: 1.0000
- external: 0.9977
- CR: 1.0022
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.0027
- rmse_abm_no_ode: 4.3931
- rmse_ode: 8.1832
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.8743
- macro_coupling: 0.3031
- ode_coupling_strength: 0.2425
- abm_feedback_gamma: 0.0500
- damping: 0.8658
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2542
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1113
- bootstrap_mean: -0.1115
- CI 95%: [-0.1202, -0.1017]
- weighted_value (LoE factor 1.00): -0.1113
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9997
- external: 0.9958
- CR: 1.0039
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3528
- rmse_abm_no_ode: 1.2174
- rmse_ode: 1.7055
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3584
- ode_coupling_strength: 0.2867
- abm_feedback_gamma: 0.0500
- damping: 0.8903
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7332
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


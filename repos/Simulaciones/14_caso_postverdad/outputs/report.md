# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-11T01:33:54.267648Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0686
- bootstrap_mean: -0.0688
- CI 95%: [-0.0771, -0.0615]
- weighted_value (LoE factor 0.20): -0.0137
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7338
- rmse_abm_no_ode: 0.6867
- rmse_ode: 1.8720
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.7342
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7305
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2383
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3564
- bootstrap_mean: 0.3693
- CI 95%: [0.2959, 0.5084]
- weighted_value (LoE factor 0.20): 0.0713
- válido (0.30-0.90): True
- detrended_edi: 0.3564
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.9988
- external: 0.9898
- CR: 1.0090
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9339
- rmse_abm_no_ode: 1.4511
- rmse_ode: 2.8600
- rmse_reduced: 3.8296
- threshold: 1.1553

### Calibración
- forcing_scale: 0.9328
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1262
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


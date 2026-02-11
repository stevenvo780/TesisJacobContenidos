# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-11T01:46:00.011713Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4200
- bootstrap_mean: 0.4206
- CI 95%: [0.4068, 0.4368]
- weighted_value (LoE factor 0.60): 0.2520
- válido (0.30-0.90): True
- detrended_edi: 0.4200
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 1.0000
- external: 0.9992
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9649
- rmse_abm_no_ode: 4.1621
- rmse_ode: 1.9049
- rmse_reduced: 6.8364
- threshold: 2.5948

### Calibración
- forcing_scale: 0.6173
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6149
- ode_alpha: 0.0310
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1940
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5591
- bootstrap_mean: 0.5587
- CI 95%: [0.5428, 0.5725]
- weighted_value (LoE factor 0.60): 0.3355
- válido (0.30-0.90): True
- detrended_edi: 0.5591
- trend_ratio: 1.000
- trend_r2: 0.988

### Symploké y CR
- internal: 0.9970
- external: 0.9965
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0769
- rmse_abm_no_ode: 0.3739
- rmse_ode: 3.6104
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7062
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1409
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


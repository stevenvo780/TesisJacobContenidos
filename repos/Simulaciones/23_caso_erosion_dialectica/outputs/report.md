# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-11T02:09:17.306304Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4255
- bootstrap_mean: 0.4277
- CI 95%: [0.4151, 0.4445]
- weighted_value (LoE factor 0.60): 0.2553
- válido (0.30-0.90): True
- detrended_edi: 0.4255
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 1.0000
- external: 0.9990
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9274
- rmse_abm_no_ode: 4.1516
- rmse_ode: 1.9032
- rmse_reduced: 6.8364
- threshold: 2.5948

### Calibración
- forcing_scale: 0.5929
- macro_coupling: 0.0541
- ode_coupling_strength: 0.0433
- abm_feedback_gamma: 0.0500
- damping: 0.5783
- ode_alpha: 0.0310
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1941
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5852
- bootstrap_mean: 0.5857
- CI 95%: [0.5677, 0.5981]
- weighted_value (LoE factor 0.60): 0.3511
- válido (0.30-0.90): True
- detrended_edi: 0.5852
- trend_ratio: 1.000
- trend_r2: 0.988

### Symploké y CR
- internal: 0.9982
- external: 0.9983
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0131
- rmse_abm_no_ode: 0.4113
- rmse_ode: 3.6037
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4059
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7080
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1502
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


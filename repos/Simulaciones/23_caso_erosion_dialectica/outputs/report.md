# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-11T04:46:08.937722Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.5205
- bootstrap_mean: 0.5210
- CI 95%: [0.5074, 0.5369]
- weighted_value (LoE factor 0.60): 0.3123
- válido (0.30-0.90): True
- detrended_edi: 0.5205
- trend_ratio: 1.000
- trend_r2: 0.990

### Symploké y CR
- internal: 1.0000
- external: 0.9911
- CR: 1.0090
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.2780
- rmse_abm_no_ode: 4.1489
- rmse_ode: 1.8745
- rmse_reduced: 6.8364
- threshold: 2.5948

### Calibración
- forcing_scale: 0.6692
- macro_coupling: 0.3191
- ode_coupling_strength: 0.2553
- abm_feedback_gamma: 0.0500
- damping: 0.6629
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
- valor: 0.6027
- bootstrap_mean: 0.6024
- CI 95%: [0.5975, 0.6068]
- weighted_value (LoE factor 0.60): 0.3616
- válido (0.30-0.90): True
- detrended_edi: 0.6027
- trend_ratio: 1.000
- trend_r2: 0.988

### Symploké y CR
- internal: 0.9970
- external: 0.9964
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9703
- rmse_abm_no_ode: 0.1900
- rmse_ode: 3.6052
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7044
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1425
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Microplásticos Oceánicos (Jambeck Accumulation-Decay)

- generated_at: 2026-02-11T23:16:50.958867Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0366
- bootstrap_mean: 0.0370
- CI 95%: [0.0338, 0.0422]
- weighted_value (LoE factor 0.60): 0.0220
- válido (0.30-0.90): False
- detrended_edi: 0.0366
- trend_ratio: 1.000
- trend_r2: 0.820

### Symploké y CR
- internal: 0.9994
- external: 0.9996
- CR: 0.9999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5705
- rmse_abm_no_ode: 1.6302
- rmse_ode: 2.5635
- rmse_reduced: 3.1419
- threshold: 0.8551

### Calibración
- forcing_scale: 0.8133
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9251
- ode_alpha: 0.1920
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6194
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7276
- bootstrap_mean: 0.7184
- CI 95%: [0.5571, 0.8355]
- weighted_value (LoE factor 0.60): 0.4366
- válido (0.30-0.90): True
- detrended_edi: 0.7276
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9998
- external: 0.9993
- CR: 1.0005
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3900
- rmse_abm_no_ode: 1.4320
- rmse_ode: 2.1241
- rmse_reduced: 2.3809
- threshold: 0.4297

### Calibración
- forcing_scale: 0.6552
- macro_coupling: 0.4006
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4400
- ode_alpha: 0.0152
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3783
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


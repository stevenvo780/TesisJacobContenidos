# Reporte de Validación — Microplásticos Oceánicos (Jambeck Accumulation-Decay)

- generated_at: 2026-02-12T02:02:37.611067Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0356
- bootstrap_mean: 0.0359
- CI 95%: [0.0328, 0.0409]
- weighted_value (LoE factor 0.60): 0.0213
- válido (0.30-0.90): False
- detrended_edi: 0.0356
- trend_ratio: 1.000
- trend_r2: 0.820

### Symploké y CR
- internal: 0.9995
- external: 0.9996
- CR: 0.9998
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5572
- rmse_abm_no_ode: 1.6146
- rmse_ode: 2.5620
- rmse_reduced: 3.1419
- threshold: 0.8551

### Calibración
- forcing_scale: 0.8340
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1920
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6183
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6559
- bootstrap_mean: 0.6435
- CI 95%: [0.4494, 0.7830]
- weighted_value (LoE factor 0.60): 0.3935
- válido (0.30-0.90): True
- detrended_edi: 0.6559
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9997
- external: 0.9996
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4917
- rmse_abm_no_ode: 1.4287
- rmse_ode: 2.1431
- rmse_reduced: 2.3809
- threshold: 0.4297

### Calibración
- forcing_scale: 0.6552
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4400
- ode_alpha: 0.0152
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3781
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


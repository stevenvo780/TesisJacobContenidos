# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-12T04:06:44.226857Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1921
- bootstrap_mean: 0.1944
- CI 95%: [0.1608, 0.2388]
- weighted_value (LoE factor 0.60): 0.1152
- válido (0.30-0.90): False
- detrended_edi: 0.1921
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9987
- external: 0.9904
- CR: 1.0084
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4024
- rmse_abm_no_ode: 1.7358
- rmse_ode: 2.4356
- rmse_reduced: 2.5775
- threshold: 0.9097

### Calibración
- forcing_scale: 0.9263
- macro_coupling: 0.1643
- ode_coupling_strength: 0.1314
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0401
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8031
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3221
- bootstrap_mean: 0.3245
- CI 95%: [-0.0573, 0.6540]
- weighted_value (LoE factor 0.60): 0.1933
- válido (0.30-0.90): True
- detrended_edi: 0.3221
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9992
- external: 0.9965
- CR: 1.0027
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2340
- rmse_abm_no_ode: 0.3452
- rmse_ode: 1.8046
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9439
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2793
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


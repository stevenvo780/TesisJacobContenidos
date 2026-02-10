# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-10T06:22:53.122613Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0703
- bootstrap_mean: 0.0709
- CI 95%: [0.0650, 0.0788]
- weighted_value (LoE factor 0.60): 0.0422
- válido (0.30-0.90): False
- detrended_edi: 0.0703
- trend_ratio: 1.000
- trend_r2: 0.960

### Symploké y CR
- internal: 1.0000
- external: 0.9996
- CR: 1.0003
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2346
- rmse_abm_no_ode: 1.3281
- rmse_ode: 0.4742
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.8930
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8813
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2116
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.5924
- CI 95%: [-3.1867, -2.1012]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9987
- external: 0.9358
- CR: 1.0672
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1908
- rmse_abm_no_ode: 0.3363
- rmse_ode: 3.7883
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2802
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


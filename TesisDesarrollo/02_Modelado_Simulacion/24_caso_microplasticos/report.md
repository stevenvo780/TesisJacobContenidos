# Reporte de Validación — Microplásticos Oceánicos (Jambeck Accumulation-Decay)

- generated_at: 2026-02-11T19:28:33.345451Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0378
- bootstrap_mean: 0.0382
- CI 95%: [0.0349, 0.0436]
- weighted_value (LoE factor 0.60): 0.0227
- válido (0.30-0.90): False
- detrended_edi: 0.0378
- trend_ratio: 1.000
- trend_r2: 0.820

### Symploké y CR
- internal: 0.9994
- external: 0.9995
- CR: 0.9999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5772
- rmse_abm_no_ode: 1.6392
- rmse_ode: 2.5645
- rmse_reduced: 3.1418
- threshold: 0.8551

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.1920
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6210
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.2832
- CI 95%: [-2.2317, -0.6307]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9999
- external: 0.9986
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1890
- rmse_abm_no_ode: 0.0845
- rmse_ode: 2.0790
- rmse_reduced: 2.3810
- threshold: 0.4297

### Calibración
- forcing_scale: 0.9199
- macro_coupling: 0.1500
- ode_coupling_strength: 0.1200
- abm_feedback_gamma: 0.0500
- damping: 0.8494
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0839
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


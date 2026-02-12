# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe Bilineal)

- generated_at: 2026-02-12T01:19:53.656779Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0093
- bootstrap_mean: -0.0094
- CI 95%: [-0.0131, -0.0057]
- weighted_value (LoE factor 0.60): -0.0056
- válido (0.30-0.90): False
- detrended_edi: -0.0093
- trend_ratio: 1.000
- trend_r2: 0.627

### Symploké y CR
- internal: 0.9947
- external: 0.9957
- CR: 0.9990
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.2728
- rmse_abm_no_ode: 2.2519
- rmse_ode: 3.0971
- rmse_reduced: 2.6686
- threshold: 0.9559

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8898
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.9191
- bootstrap_mean: -0.9343
- CI 95%: [-1.2391, -0.7447]
- weighted_value (LoE factor 0.60): -0.5515
- válido (0.30-0.90): False
- detrended_edi: -0.9191
- trend_ratio: 1.000
- trend_r2: 0.815

### Symploké y CR
- internal: 0.9999
- external: 0.9934
- CR: 1.0066
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0293
- rmse_abm_no_ode: 0.5363
- rmse_ode: 5.4628
- rmse_reduced: 2.5475
- threshold: 0.1285

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8099
- ode_alpha: 0.1365
- ode_beta: 0.6821
- assimilation_strength: 0.0000
- calibration_rmse: 0.2946
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


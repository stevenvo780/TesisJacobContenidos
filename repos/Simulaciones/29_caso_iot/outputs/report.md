# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe Bilineal)

- generated_at: 2026-02-11T22:21:34.296041Z

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
- valor: -0.2178
- bootstrap_mean: -0.2352
- CI 95%: [-0.7497, 0.1541]
- weighted_value (LoE factor 0.60): -0.1307
- válido (0.30-0.90): False
- detrended_edi: -0.2178
- trend_ratio: 1.000
- trend_r2: 0.815

### Symploké y CR
- internal: 0.9985
- external: 0.9631
- CR: 1.0367
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3851
- rmse_abm_no_ode: 1.9585
- rmse_ode: 4.3579
- rmse_reduced: 2.5475
- threshold: 0.1285

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4198
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5173
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.7153
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


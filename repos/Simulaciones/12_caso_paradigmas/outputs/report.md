# Reporte de Validación — Paradigmas Científicos (R&D)

- generated_at: 2026-02-12T02:02:28.033173Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1362
- bootstrap_mean: -0.1316
- CI 95%: [-0.2106, 0.0150]
- weighted_value (LoE factor 0.60): -0.0817
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9996
- external: 0.9958
- CR: 1.0038
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8283
- rmse_abm_no_ode: 0.7290
- rmse_ode: 1.1302
- rmse_reduced: 2.1939
- threshold: 0.1000

### Calibración
- forcing_scale: 0.8461
- macro_coupling: 0.2666
- ode_coupling_strength: 0.2133
- abm_feedback_gamma: 0.0500
- damping: 0.5767
- ode_alpha: 0.4295
- ode_beta: 0.8315
- assimilation_strength: 0.0000
- calibration_rmse: 0.6709
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0059
- bootstrap_mean: -0.0069
- CI 95%: [-0.0152, -0.0038]
- weighted_value (LoE factor 0.60): -0.0035
- válido (0.30-0.90): False
- detrended_edi: -0.0059
- trend_ratio: 1.000
- trend_r2: 0.902

### Symploké y CR
- internal: 0.9814
- external: 0.9787
- CR: 1.0027
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.3109
- rmse_abm_no_ode: 9.2567
- rmse_ode: 9.3657
- rmse_reduced: 8.9315
- threshold: 5.7385

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.4216
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8562
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


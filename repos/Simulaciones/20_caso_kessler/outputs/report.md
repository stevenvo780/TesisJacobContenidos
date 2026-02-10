# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-10T04:20:53.863340Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.9139
- CI 95%: [-3.0433, -2.7549]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.554

### Symploké y CR
- internal: 0.8232
- external: 0.7165
- CR: 1.1489
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2663144.1291
- rmse_abm_no_ode: 679582.6791
- rmse_ode: 7.3220
- rmse_reduced: 627276.0876
- threshold: 3.9363

### Calibración
- forcing_scale: 0.6266
- macro_coupling: 0.4777
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6369
- ode_alpha: 0.1645
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2650
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.8835
- CI 95%: [-3.0140, -2.7224]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.932

### Symploké y CR
- internal: 0.8223
- external: 0.6910
- CR: 1.1900
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2568378.6829
- rmse_abm_no_ode: 660535.1918
- rmse_ode: 15.2845
- rmse_reduced: 627287.1330
- threshold: 0.5326

### Calibración
- forcing_scale: 0.5978
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6296
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2107
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


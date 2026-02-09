# Reporte de Validación — Acidificación Oceánica (CO2SYS + Revelle Factor)

- generated_at: 2026-02-09T20:55:56.926114Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0892
- bootstrap_mean: -0.0890
- CI 95%: [-0.0954, -0.0831]
- weighted_value (LoE factor 0.20): -0.0178
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9974
- external: 0.4555
- CR: 2.1898
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.5396
- rmse_abm_no_ode: 1.4135
- rmse_ode: 7.9611
- rmse_reduced: 2.0224
- threshold: 1.0107

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0823
- ode_coupling_strength: 0.0658
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0170
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3061
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, -0.0000]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False
- detrended_edi: -0.0000
- trend_ratio: 1.000
- trend_r2: 0.861

### Symploké y CR
- internal: 0.9992
- external: 0.8250
- CR: 1.2111
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3431
- rmse_abm_no_ode: 3.3431
- rmse_ode: 8.8946
- rmse_reduced: 3.2742
- threshold: 2.3256

### Calibración
- forcing_scale: 0.8576
- macro_coupling: 0.1720
- ode_coupling_strength: 0.1376
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9496
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.


# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T23:02:05.553017Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3220
- bootstrap_mean: 0.3262
- CI 95%: [0.2681, 0.3952]
- weighted_value (LoE factor 0.60): 0.1932
- válido (0.30-0.90): False
- detrended_edi: 0.3220
- trend_ratio: 1.000
- trend_r2: 0.854

### Symploké y CR
- internal: 0.9998
- external: 0.9985
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4887
- rmse_abm_no_ode: 0.7207
- rmse_ode: 1.0657
- rmse_reduced: 2.9446
- threshold: 0.6860

### Calibración
- forcing_scale: 0.9459
- macro_coupling: 0.3413
- ode_coupling_strength: 0.2731
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2983
- ode_rolling: None

### Interpretación
Los resultados muestran señal de emergencia **weak**. La estructura macro es detectable pero no alcanza robustez suficiente para confirmar emergencia fuerte. Se recomienda cautela en la interpretación ontológica.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0265
- bootstrap_mean: 0.0267
- CI 95%: [0.0228, 0.0309]
- weighted_value (LoE factor 0.60): 0.0159
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9992
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1564
- rmse_abm_no_ode: 2.2152
- rmse_ode: 3.5143
- rmse_reduced: 2.2157
- threshold: 0.4144

### Calibración
- forcing_scale: 0.3832
- macro_coupling: 0.3994
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.0770
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8059
- ode_rolling: None

### Interpretación
Categoría de emergencia: **trend**. No se detecta estructura macro significativa con los datos y parámetros actuales.


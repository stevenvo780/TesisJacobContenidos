# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-09T21:46:41.274533Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1149
- bootstrap_mean: 0.1138
- CI 95%: [0.0940, 0.1308]
- weighted_value (LoE factor 0.20): 0.0230
- válido (0.30-0.90): False
- detrended_edi: 0.1149
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 0.9612
- external: 0.1463
- CR: 6.5683
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.8976
- rmse_abm_no_ode: 5.5337
- rmse_ode: 1.6554
- rmse_reduced: 5.1439
- threshold: 0.9858

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 2.2767
- ode_rolling: None

### Interpretación
Categoría de emergencia: **trend**. No se detecta estructura macro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0534
- bootstrap_mean: 0.0700
- CI 95%: [0.0361, 0.1256]
- weighted_value (LoE factor 0.20): 0.0107
- válido (0.30-0.90): False
- detrended_edi: 0.0534
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9186
- external: -0.6888
- CR: 1.3336
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5824
- rmse_abm_no_ode: 3.7846
- rmse_ode: 2.7994
- rmse_reduced: 3.8040
- threshold: 2.7353

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 2.5036
- ode_rolling: None

### Interpretación
Los resultados muestran señal de emergencia **suggestive**. La estructura macro es detectable pero no alcanza robustez suficiente para confirmar emergencia fuerte. Se recomienda cautela en la interpretación ontológica.


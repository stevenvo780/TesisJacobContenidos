# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-11T04:44:22.436502Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7472
- bootstrap_mean: 0.7478
- CI 95%: [0.7395, 0.7572]
- weighted_value (LoE factor 0.20): 0.1494
- válido (0.30-0.90): True
- detrended_edi: 0.7472
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 1.0000
- external: 0.9995
- CR: 1.0005
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9280
- rmse_abm_no_ode: 1.0779
- rmse_ode: 1.3665
- rmse_reduced: 3.6713
- threshold: 0.9858

### Calibración
- forcing_scale: 0.9377
- macro_coupling: 0.1752
- ode_coupling_strength: 0.1402
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 0.1435
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3173
- bootstrap_mean: -0.4083
- CI 95%: [-1.0119, -0.1465]
- weighted_value (LoE factor 0.20): -0.0635
- válido (0.30-0.90): False
- detrended_edi: -0.3173
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9998
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.6364
- rmse_abm_no_ode: 4.1727
- rmse_ode: 2.8097
- rmse_reduced: 2.7605
- threshold: 2.7353

### Calibración
- forcing_scale: 0.7411
- macro_coupling: 0.3853
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6592
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2778
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


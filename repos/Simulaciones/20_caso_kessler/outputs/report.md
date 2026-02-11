# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-11T01:43:31.940190Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5883
- bootstrap_mean: 0.5877
- CI 95%: [0.5348, 0.6274]
- weighted_value (LoE factor 0.20): 0.1177
- válido (0.30-0.90): True
- detrended_edi: 0.5883
- trend_ratio: 1.000
- trend_r2: 0.554

### Symploké y CR
- internal: 0.9739
- external: 0.8961
- CR: 1.0868
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.5338
- rmse_abm_no_ode: 11.1839
- rmse_ode: 7.3220
- rmse_reduced: 13.4424
- threshold: 3.9363

### Calibración
- forcing_scale: 0.7818
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7989
- ode_alpha: 0.1645
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2495
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -1.8050
- CI 95%: [-2.2273, -1.4386]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.932

### Symploké y CR
- internal: 0.9702
- external: 0.8862
- CR: 1.0948
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.9450
- rmse_abm_no_ode: 0.2417
- rmse_ode: 15.2845
- rmse_reduced: 2.1317
- threshold: 0.5326

### Calibración
- forcing_scale: 0.7560
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7891
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2024
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


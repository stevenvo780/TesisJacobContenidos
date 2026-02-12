# Reporte de Validación — Urbanización Global

- generated_at: 2026-02-12T04:04:56.353884Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8331
- bootstrap_mean: 0.8325
- CI 95%: [0.7882, 0.8733]
- weighted_value (LoE factor 0.60): 0.4999
- válido (0.30-0.90): True
- detrended_edi: 0.8331
- trend_ratio: 1.000
- trend_r2: 0.981

### Symploké y CR
- internal: 0.9994
- external: 0.9946
- CR: 1.0048
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0910
- rmse_abm_no_ode: 0.5455
- rmse_ode: 2.8358
- rmse_reduced: 2.9579
- threshold: 0.5469

### Calibración
- forcing_scale: 0.9660
- macro_coupling: 0.4837
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0042
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1134
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3366
- bootstrap_mean: 0.3369
- CI 95%: [0.3305, 0.3467]
- weighted_value (LoE factor 0.60): 0.2020
- válido (0.30-0.90): True
- detrended_edi: 0.3366
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.9997
- external: 0.9968
- CR: 1.0029
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7876
- rmse_abm_no_ode: 1.1872
- rmse_ode: 3.1943
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.9714
- macro_coupling: 0.4184
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0704
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


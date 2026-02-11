# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-11T01:41:28.033597Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.7961
- bootstrap_mean: 0.7962
- CI 95%: [0.7862, 0.8061]
- weighted_value (LoE factor 0.20): 0.1592
- válido (0.30-0.90): True
- detrended_edi: 0.7961
- trend_ratio: 1.000
- trend_r2: 0.955

### Symploké y CR
- internal: 1.0000
- external: 0.9996
- CR: 1.0004
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6145
- rmse_abm_no_ode: 0.5190
- rmse_ode: 1.9725
- rmse_reduced: 3.0142
- threshold: 0.4782

### Calibración
- forcing_scale: 0.7720
- macro_coupling: 0.0714
- ode_coupling_strength: 0.0571
- abm_feedback_gamma: 0.0500
- damping: 0.7656
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1430
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.5339
- bootstrap_mean: 0.5351
- CI 95%: [0.5161, 0.5603]
- weighted_value (LoE factor 0.20): 0.1068
- válido (0.30-0.90): True
- detrended_edi: 0.5339
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.9996
- external: 0.9887
- CR: 1.0110
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6930
- rmse_abm_no_ode: 1.2380
- rmse_ode: 2.6384
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.7739
- macro_coupling: 0.4996
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7820
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0767
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


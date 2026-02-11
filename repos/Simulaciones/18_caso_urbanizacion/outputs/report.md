# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-11T02:09:32.565810Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8106
- bootstrap_mean: 0.8121
- CI 95%: [0.7984, 0.8196]
- weighted_value (LoE factor 0.20): 0.1621
- válido (0.30-0.90): True
- detrended_edi: 0.8106
- trend_ratio: 1.000
- trend_r2: 0.955

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5710
- rmse_abm_no_ode: 0.5093
- rmse_ode: 1.9697
- rmse_reduced: 3.0142
- threshold: 0.4782

### Calibración
- forcing_scale: 0.8930
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8813
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1433
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.5470
- bootstrap_mean: 0.5492
- CI 95%: [0.5305, 0.5730]
- weighted_value (LoE factor 0.20): 0.1094
- válido (0.30-0.90): True
- detrended_edi: 0.5470
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.9993
- external: 0.9901
- CR: 1.0093
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6455
- rmse_abm_no_ode: 1.2103
- rmse_ode: 2.6358
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0706
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


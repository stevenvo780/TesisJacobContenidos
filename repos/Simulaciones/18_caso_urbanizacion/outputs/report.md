# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-11T05:17:04.939595Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8230
- bootstrap_mean: 0.8232
- CI 95%: [0.8130, 0.8333]
- weighted_value (LoE factor 0.20): 0.1646
- válido (0.30-0.90): True
- detrended_edi: 0.8230
- trend_ratio: 1.000
- trend_r2: 0.955

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5335
- rmse_abm_no_ode: 0.4620
- rmse_ode: 1.9680
- rmse_reduced: 3.0142
- threshold: 0.4782

### Calibración
- forcing_scale: 0.8433
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.7828
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1420
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6573
- bootstrap_mean: 0.6577
- CI 95%: [0.6407, 0.6801]
- weighted_value (LoE factor 0.20): 0.1315
- válido (0.30-0.90): True
- detrended_edi: 0.6573
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.9999
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
- rmse_abm: 1.2450
- rmse_abm_no_ode: 1.1835
- rmse_ode: 2.6118
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.9579
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0695
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


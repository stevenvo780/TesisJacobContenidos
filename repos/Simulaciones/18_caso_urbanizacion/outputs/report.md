# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-11T04:44:39.576138Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7275
- bootstrap_mean: 0.7276
- CI 95%: [0.7191, 0.7379]
- weighted_value (LoE factor 0.20): 0.1455
- válido (0.30-0.90): True
- detrended_edi: 0.7275
- trend_ratio: 1.000
- trend_r2: 0.955

### Symploké y CR
- internal: 0.9999
- external: 0.9947
- CR: 1.0052
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8213
- rmse_abm_no_ode: 0.4680
- rmse_ode: 1.9858
- rmse_reduced: 3.0142
- threshold: 0.4782

### Calibración
- forcing_scale: 0.7891
- macro_coupling: 0.3151
- ode_coupling_strength: 0.2521
- abm_feedback_gamma: 0.0500
- damping: 0.7804
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1435
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.5909
- bootstrap_mean: 0.5913
- CI 95%: [0.5737, 0.6170]
- weighted_value (LoE factor 0.20): 0.1182
- válido (0.30-0.90): True
- detrended_edi: 0.5909
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.9998
- external: 0.9957
- CR: 1.0041
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4860
- rmse_abm_no_ode: 1.1833
- rmse_ode: 2.6265
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.9096
- macro_coupling: 0.3100
- ode_coupling_strength: 0.2480
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0689
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


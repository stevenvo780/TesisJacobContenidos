# Reporte de Validación — Urbanización Global

- generated_at: 2026-02-11T23:11:57.935040Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8040
- bootstrap_mean: 0.8044
- CI 95%: [0.7458, 0.8578]
- weighted_value (LoE factor 0.60): 0.4824
- válido (0.30-0.90): True
- detrended_edi: 0.8040
- trend_ratio: 1.000
- trend_r2: 0.981

### Symploké y CR
- internal: 0.9998
- external: 0.9913
- CR: 1.0086
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1406
- rmse_abm_no_ode: 0.7174
- rmse_ode: 3.0450
- rmse_reduced: 2.9579
- threshold: 0.5469

### Calibración
- forcing_scale: 0.6384
- macro_coupling: 0.4216
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.0042
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1670
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.1512
- bootstrap_mean: 0.1513
- CI 95%: [0.1494, 0.1537]
- weighted_value (LoE factor 0.60): 0.0907
- válido (0.30-0.90): True
- detrended_edi: 0.1512
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 1.0000
- external: 0.9987
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0985
- rmse_abm_no_ode: 1.2942
- rmse_ode: 2.8227
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.6384
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1040
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


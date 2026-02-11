# Reporte de Validación — Urbanización Global

- generated_at: 2026-02-11T19:28:45.474753Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.9055
- bootstrap_mean: -0.9211
- CI 95%: [-1.1345, -0.7698]
- weighted_value (LoE factor 0.60): -0.5433
- válido (0.30-0.90): False
- detrended_edi: -0.9055
- trend_ratio: 1.000
- trend_r2: 0.947

### Symploké y CR
- internal: 0.9985
- external: 0.9979
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1302
- rmse_abm_no_ode: 0.5931
- rmse_ode: 3.4229
- rmse_reduced: 2.6901
- threshold: 0.6719

### Calibración
- forcing_scale: 0.6384
- macro_coupling: 0.4216
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.3132
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

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


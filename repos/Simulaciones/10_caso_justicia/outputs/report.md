# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-11T02:09:03.450009Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7005
- bootstrap_mean: 0.7022
- CI 95%: [0.6871, 0.7173]
- weighted_value (LoE factor 0.20): 0.1401
- válido (0.30-0.90): True
- detrended_edi: 0.7005
- trend_ratio: 1.000
- trend_r2: 0.938

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
- rmse_abm: 0.5798
- rmse_abm_no_ode: 0.6024
- rmse_ode: 1.4240
- rmse_reduced: 1.9358
- threshold: 0.2854

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.0474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1170
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7730
- bootstrap_mean: 0.7765
- CI 95%: [0.6597, 0.8921]
- weighted_value (LoE factor 0.20): 0.1546
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9975
- CR: 1.0024
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4288
- rmse_abm_no_ode: 0.5067
- rmse_ode: 1.3918
- rmse_reduced: 1.8889
- threshold: 0.3262

### Calibración
- forcing_scale: 0.5016
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.4162
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4017
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


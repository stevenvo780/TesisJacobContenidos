# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-11T04:45:24.198332Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8517
- bootstrap_mean: 0.8539
- CI 95%: [0.8172, 0.8906]
- weighted_value (LoE factor 0.60): 0.5110
- válido (0.30-0.90): True
- detrended_edi: 0.8517
- trend_ratio: 1.000
- trend_r2: 0.854

### Symploké y CR
- internal: 0.9995
- external: 0.9976
- CR: 1.0019
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4367
- rmse_abm_no_ode: 0.7218
- rmse_ode: 1.0718
- rmse_reduced: 2.9447
- threshold: 0.6860

### Calibración
- forcing_scale: 0.9244
- macro_coupling: 0.4745
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2983
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0273
- bootstrap_mean: 0.0275
- CI 95%: [0.0232, 0.0320]
- weighted_value (LoE factor 0.60): 0.0164
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9993
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1550
- rmse_abm_no_ode: 2.2149
- rmse_ode: 3.5161
- rmse_reduced: 2.2155
- threshold: 0.4144

### Calibración
- forcing_scale: 0.5576
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.0779
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8057
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


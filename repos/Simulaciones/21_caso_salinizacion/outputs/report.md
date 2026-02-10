# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-10T04:21:24.031311Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2356
- bootstrap_mean: 0.2397
- CI 95%: [0.2014, 0.2871]
- weighted_value (LoE factor 0.60): 0.1414
- válido (0.30-0.90): False
- detrended_edi: 0.2356
- trend_ratio: 1.000
- trend_r2: 0.854

### Symploké y CR
- internal: 1.0000
- external: 0.9989
- CR: 1.0011
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5803
- rmse_abm_no_ode: 0.7592
- rmse_ode: 1.0565
- rmse_reduced: 2.9447
- threshold: 0.6860

### Calibración
- forcing_scale: 0.6937
- macro_coupling: 0.1794
- ode_coupling_strength: 0.1435
- abm_feedback_gamma: 0.0500
- damping: 0.6874
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3046
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0246
- bootstrap_mean: 0.0247
- CI 95%: [0.0220, 0.0275]
- weighted_value (LoE factor 0.60): 0.0147
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9988
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
- rmse_abm: 2.1623
- rmse_abm_no_ode: 2.2167
- rmse_ode: 3.5067
- rmse_reduced: 2.2174
- threshold: 0.4144

### Calibración
- forcing_scale: 0.9829
- macro_coupling: 0.2026
- ode_coupling_strength: 0.1620
- abm_feedback_gamma: 0.0500
- damping: 0.0778
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8065
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


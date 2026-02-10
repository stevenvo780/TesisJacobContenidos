# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-10T04:22:17.932980Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1736
- bootstrap_mean: 0.1736
- CI 95%: [0.1693, 0.1786]
- weighted_value (LoE factor 0.80): 0.1389
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9994
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2683
- rmse_abm_no_ode: 1.5347
- rmse_ode: 1.7105
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.5991
- macro_coupling: 0.1319
- ode_coupling_strength: 0.1055
- abm_feedback_gamma: 0.0500
- damping: 0.5992
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2163
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4219
- bootstrap_mean: 0.4229
- CI 95%: [0.4096, 0.4447]
- weighted_value (LoE factor 0.80): 0.3375
- válido (0.30-0.90): True
- detrended_edi: 0.4219
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9986
- CR: 1.0014
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.8531
- rmse_abm_no_ode: 17.0432
- rmse_ode: 2.7877
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.8125
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4664
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3886
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


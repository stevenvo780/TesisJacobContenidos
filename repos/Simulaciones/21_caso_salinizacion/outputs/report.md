# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-11T01:45:02.479450Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7991
- bootstrap_mean: 0.8017
- CI 95%: [0.7625, 0.8407]
- weighted_value (LoE factor 0.60): 0.4795
- válido (0.30-0.90): True
- detrended_edi: 0.7991
- trend_ratio: 1.000
- trend_r2: 0.854

### Symploké y CR
- internal: 0.9999
- external: 0.9991
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5915
- rmse_abm_no_ode: 0.7601
- rmse_ode: 1.0556
- rmse_reduced: 2.9447
- threshold: 0.6860

### Calibración
- forcing_scale: 0.7759
- macro_coupling: 0.1856
- ode_coupling_strength: 0.1485
- abm_feedback_gamma: 0.0500
- damping: 0.7738
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3016
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0239
- bootstrap_mean: 0.0241
- CI 95%: [0.0215, 0.0268]
- weighted_value (LoE factor 0.60): 0.0144
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9987
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
- rmse_abm: 2.1641
- rmse_abm_no_ode: 2.2167
- rmse_ode: 3.5042
- rmse_reduced: 2.2172
- threshold: 0.4144

### Calibración
- forcing_scale: 0.0874
- macro_coupling: 0.1686
- ode_coupling_strength: 0.1349
- abm_feedback_gamma: 0.0500
- damping: 0.0780
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8063
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


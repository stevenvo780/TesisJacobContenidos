# Reporte de Validación — Movilidad Urbana (Vehículos)

- generated_at: 2026-02-11T22:45:19.746268Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3975
- bootstrap_mean: 0.4119
- CI 95%: [-0.1535, 0.7788]
- weighted_value (LoE factor 1.00): 0.3975
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9961
- external: 0.9260
- CR: 1.0757
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1979
- rmse_abm_no_ode: 0.3285
- rmse_ode: 1.8450
- rmse_reduced: 0.3296
- threshold: 0.1880

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7111
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9940
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.1283
- bootstrap_mean: 0.1177
- CI 95%: [-0.0729, 0.2521]
- weighted_value (LoE factor 1.00): 0.1283
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9995
- external: 0.9951
- CR: 1.0045
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1270
- rmse_abm_no_ode: 1.2929
- rmse_ode: 1.9325
- rmse_reduced: 4.8437
- threshold: 1.8501

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6590
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 0.1508
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


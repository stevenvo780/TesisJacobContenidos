# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-11T02:09:12.055978Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9781
- CR: 1.0224
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 20481532.7750
- rmse_abm_no_ode: 20481533.8109
- rmse_ode: 20481525.7728
- rmse_reduced: 20481535.7337
- threshold: 19219447.7270

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1086
- ode_coupling_strength: 0.0869
- abm_feedback_gamma: 0.0500
- damping: 0.6595
- ode_alpha: 0.0012
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5390
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0223
- bootstrap_mean: 0.0218
- CI 95%: [-0.0158, 0.0573]
- weighted_value (LoE factor 1.00): 0.0223
- válido (0.30-0.90): False
- detrended_edi: 0.0223
- trend_ratio: 1.000
- trend_r2: 0.979

### Symploké y CR
- internal: 1.0000
- external: 0.8360
- CR: 1.1961
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1453
- rmse_abm_no_ode: 1.0398
- rmse_ode: 10.2323
- rmse_reduced: 3.2169
- threshold: 1.1814

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4947
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8713
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4013
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


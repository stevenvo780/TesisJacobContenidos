# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-11T01:18:31.894576Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0139
- bootstrap_mean: 0.0138
- CI 95%: [0.0121, 0.0154]
- weighted_value (LoE factor 0.20): 0.0028
- válido (0.30-0.90): False
- detrended_edi: 0.0139
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
- rmse_abm: 0.5519
- rmse_abm_no_ode: 0.5597
- rmse_ode: 1.4309
- rmse_reduced: 1.9358
- threshold: 0.2854

### Calibración
- forcing_scale: 0.7629
- macro_coupling: 0.4890
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7769
- ode_alpha: 0.0474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1174
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1687
- bootstrap_mean: 0.1729
- CI 95%: [0.0615, 0.3044]
- weighted_value (LoE factor 0.20): 0.0337
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9969
- CR: 1.0030
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4288
- rmse_abm_no_ode: 0.5159
- rmse_ode: 1.3926
- rmse_reduced: 1.8889
- threshold: 0.3262

### Calibración
- forcing_scale: 0.4439
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.3692
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4024
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


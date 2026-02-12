# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-12T00:19:32.087200Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0116
- bootstrap_mean: 0.0117
- CI 95%: [0.0109, 0.0125]
- weighted_value (LoE factor 1.00): 0.0116
- válido (0.30-0.90): False
- detrended_edi: 0.0116
- trend_ratio: 1.000
- trend_r2: 0.983

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.8858
- rmse_abm_no_ode: 3.9316
- rmse_ode: 2.8675
- rmse_reduced: 6.9508
- threshold: 2.7339

### Calibración
- forcing_scale: 0.4913
- macro_coupling: 0.3005
- ode_coupling_strength: 0.2404
- abm_feedback_gamma: 0.0500
- damping: 0.4766
- ode_alpha: 0.1789
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1715
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0023
- bootstrap_mean: 0.0026
- CI 95%: [-0.0111, 0.0184]
- weighted_value (LoE factor 1.00): 0.0023
- válido (0.30-0.90): False
- detrended_edi: 0.0023
- trend_ratio: 1.000
- trend_r2: 0.504

### Symploké y CR
- internal: 1.0000
- external: 0.9945
- CR: 1.0055
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8802
- rmse_abm_no_ode: 0.8823
- rmse_ode: 0.8838
- rmse_reduced: 2.4621
- threshold: 1.1883

### Calibración
- forcing_scale: 0.1473
- macro_coupling: 0.1595
- ode_coupling_strength: 0.1276
- abm_feedback_gamma: 0.0500
- damping: 0.0880
- ode_alpha: 0.3657
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7543
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


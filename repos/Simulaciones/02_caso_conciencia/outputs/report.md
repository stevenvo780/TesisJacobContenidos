# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-11T23:29:33.397083Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0817
- bootstrap_mean: 0.0828
- CI 95%: [0.0690, 0.1036]
- weighted_value (LoE factor 0.60): 0.0490
- válido (0.30-0.90): False
- detrended_edi: 0.0817
- trend_ratio: 1.000
- trend_r2: 0.606

### Symploké y CR
- internal: 0.9136
- external: 0.8807
- CR: 1.0374
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8782
- rmse_abm_no_ode: 2.0452
- rmse_ode: 1.1597
- rmse_reduced: 0.4364
- threshold: 0.1933

### Calibración
- forcing_scale: 0.9461
- macro_coupling: 0.3166
- ode_coupling_strength: 0.2533
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2764
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1231
- bootstrap_mean: 0.1403
- CI 95%: [0.0855, 0.2639]
- weighted_value (LoE factor 0.60): 0.0739
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.8881
- external: 0.8830
- CR: 1.0058
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8157
- rmse_abm_no_ode: 0.9302
- rmse_ode: 2.0578
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4761
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6822
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1682
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


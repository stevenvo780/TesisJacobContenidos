# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-11T02:10:38.517284Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0804
- bootstrap_mean: 0.0723
- CI 95%: [0.0260, 0.1328]
- weighted_value (LoE factor 0.20): 0.0161
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6680
- external: 0.5756
- CR: 1.1605
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0308
- rmse_abm_no_ode: 1.0655
- rmse_ode: 1.0840
- rmse_reduced: 1.1208
- threshold: 1.0629

### Calibración
- forcing_scale: 1.0000
- macro_coupling: 0.4500
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7631
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3506
- bootstrap_mean: 0.3209
- CI 95%: [-0.2239, 0.6500]
- weighted_value (LoE factor 0.20): 0.0701
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9217
- external: 0.8843
- CR: 1.0423
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8727
- rmse_abm_no_ode: 0.9302
- rmse_ode: 1.5651
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2426
- ode_coupling_strength: 0.1941
- abm_feedback_gamma: 0.0500
- damping: 0.7073
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2138
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


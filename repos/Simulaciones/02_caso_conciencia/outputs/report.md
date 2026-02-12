# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-12T02:03:12.346333Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0849
- bootstrap_mean: 0.0860
- CI 95%: [0.0713, 0.1084]
- weighted_value (LoE factor 0.60): 0.0509
- válido (0.30-0.90): False
- detrended_edi: 0.0849
- trend_ratio: 1.000
- trend_r2: 0.606

### Symploké y CR
- internal: 0.9126
- external: 0.8817
- CR: 1.0350
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8121
- rmse_abm_no_ode: 1.9801
- rmse_ode: 1.1633
- rmse_reduced: 0.4364
- threshold: 0.1933

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2763
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
- internal: 0.8871
- external: 0.8820
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
- macro_coupling: 0.3833
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6876
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1574
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


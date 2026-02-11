# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-11T01:44:40.335208Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0211
- bootstrap_mean: 0.0220
- CI 95%: [-0.0449, 0.0964]
- weighted_value (LoE factor 0.20): 0.0042
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9891
- CR: 1.0107
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3560
- rmse_abm_no_ode: 0.3637
- rmse_ode: 0.5022
- rmse_reduced: 2.3657
- threshold: 0.3900

### Calibración
- forcing_scale: 0.7768
- macro_coupling: 0.4919
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7803
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2928
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2898
- bootstrap_mean: 0.2885
- CI 95%: [0.2373, 0.3278]
- weighted_value (LoE factor 0.20): 0.0580
- válido (0.30-0.90): False
- detrended_edi: 0.2898
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9992
- external: 0.9898
- CR: 1.0095
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4921
- rmse_abm_no_ode: 0.6929
- rmse_ode: 0.9091
- rmse_reduced: 0.9596
- threshold: 0.1452

### Calibración
- forcing_scale: 0.8218
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7948
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3646
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


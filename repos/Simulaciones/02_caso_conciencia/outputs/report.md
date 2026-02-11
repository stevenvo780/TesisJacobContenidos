# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-11T04:39:54.404965Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0132
- bootstrap_mean: 0.0124
- CI 95%: [-0.0175, 0.0413]
- weighted_value (LoE factor 0.20): 0.0026
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4509
- external: 0.5867
- CR: 0.7685
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1060
- rmse_abm_no_ode: 1.1156
- rmse_ode: 1.0885
- rmse_reduced: 1.1208
- threshold: 1.0629

### Calibración
- forcing_scale: 0.7013
- macro_coupling: 0.0992
- ode_coupling_strength: 0.0794
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3039
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3860
- bootstrap_mean: 0.3861
- CI 95%: [0.2895, 0.4643]
- weighted_value (LoE factor 0.20): 0.0772
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.7221
- external: 0.7876
- CR: 0.9169
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8252
- rmse_abm_no_ode: 0.7849
- rmse_ode: 1.7595
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.3491
- macro_coupling: 0.1136
- ode_coupling_strength: 0.0908
- abm_feedback_gamma: 0.0500
- damping: 0.0016
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8711
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


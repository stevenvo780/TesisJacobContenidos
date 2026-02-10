# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-10T06:22:59.028321Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3227
- bootstrap_mean: 0.3247
- CI 95%: [0.2828, 0.3672]
- weighted_value (LoE factor 0.80): 0.2581
- válido (0.30-0.90): False
- detrended_edi: 0.3227
- trend_ratio: 1.000
- trend_r2: 0.898

### Symploké y CR
- internal: 0.9995
- external: 0.9793
- CR: 1.0207
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8270
- rmse_abm_no_ode: 4.1736
- rmse_ode: 1.3109
- rmse_reduced: 6.3551
- threshold: 2.4845

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.3876
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5103
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0065
- bootstrap_mean: 0.0062
- CI 95%: [-0.0047, 0.0132]
- weighted_value (LoE factor 0.80): 0.0052
- válido (0.30-0.90): False
- detrended_edi: 0.0065
- trend_ratio: 1.000
- trend_r2: 0.874

### Symploké y CR
- internal: 1.0000
- external: 0.9787
- CR: 1.0217
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.8702
- rmse_abm_no_ode: 35.0982
- rmse_ode: 34.5128
- rmse_reduced: 40.8516
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5677
- macro_coupling: 0.1086
- ode_coupling_strength: 0.0869
- abm_feedback_gamma: 0.0500
- damping: 0.2868
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5971
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


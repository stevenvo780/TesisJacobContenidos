# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-11T15:05:29.025513Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1724
- bootstrap_mean: 0.1621
- CI 95%: [-0.3417, 0.5239]
- weighted_value (LoE factor 0.20): 0.0345
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9975
- external: 0.9950
- CR: 1.0025
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1827
- rmse_abm_no_ode: 1.5554
- rmse_ode: 0.8067
- rmse_reduced: 1.4290
- threshold: 1.0126

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6833
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5674
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1043
- bootstrap_mean: 0.0786
- CI 95%: [-0.0863, 0.2349]
- weighted_value (LoE factor 0.20): 0.0209
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9965
- external: 0.9971
- CR: 0.9995
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9510
- rmse_abm_no_ode: 2.9396
- rmse_ode: 3.3656
- rmse_reduced: 3.2946
- threshold: 3.2834

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.7927
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


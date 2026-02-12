# Reporte de Validación — Wikipedia (Conocimiento Colectivo)

- generated_at: 2026-02-12T04:03:03.349326Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1964
- bootstrap_mean: 0.1964
- CI 95%: [0.1924, 0.2008]
- weighted_value (LoE factor 0.60): 0.1178
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9983
- CR: 1.0016
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4126
- rmse_abm_no_ode: 3.0021
- rmse_ode: 1.6758
- rmse_reduced: 1.6761
- threshold: 1.1374

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6929
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5048
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0796
- bootstrap_mean: 0.1016
- CI 95%: [0.0479, 0.2021]
- weighted_value (LoE factor 0.60): 0.0478
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9986
- external: 0.9793
- CR: 1.0197
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3193
- rmse_abm_no_ode: 2.5200
- rmse_ode: 2.5163
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7168
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8451
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-11T05:08:42.573512Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0531
- bootstrap_mean: 0.0532
- CI 95%: [0.0140, 0.0951]
- weighted_value (LoE factor 0.20): 0.0106
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8601
- CR: 1.1627
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4522
- rmse_abm_no_ode: 1.2005
- rmse_ode: 0.4335
- rmse_reduced: 0.4775
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9373
- macro_coupling: 0.4812
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5612
- ode_alpha: 0.0068
- ode_beta: 0.8095
- assimilation_strength: 0.0000
- calibration_rmse: 0.4880
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0585
- bootstrap_mean: 0.0355
- CI 95%: [-0.2282, 0.1833]
- weighted_value (LoE factor 0.20): 0.0117
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.4425
- CR: 2.2600
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.2573
- rmse_abm_no_ode: 5.1106
- rmse_ode: 15.1313
- rmse_reduced: 4.5221
- threshold: 4.3680

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4383
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


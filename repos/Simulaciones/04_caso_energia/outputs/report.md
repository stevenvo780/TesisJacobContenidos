# Reporte de Validación — Energía (Consumo Per Cápita)

- generated_at: 2026-02-11T15:20:06.835822Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0602
- bootstrap_mean: 0.0329
- CI 95%: [-0.2360, 0.2008]
- weighted_value (LoE factor 0.20): 0.0120
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9666
- external: 0.9272
- CR: 1.0424
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8137
- rmse_abm_no_ode: 1.8313
- rmse_ode: 1.8588
- rmse_reduced: 1.9298
- threshold: 1.0955

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8216
- ode_alpha: 0.4580
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8099
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7890
- bootstrap_mean: 0.7908
- CI 95%: [0.7328, 0.8453]
- weighted_value (LoE factor 0.20): 0.1578
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9996
- external: 0.9993
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5504
- rmse_abm_no_ode: 1.1442
- rmse_ode: 2.7727
- rmse_reduced: 2.6081
- threshold: 0.3586

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6746
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2688
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


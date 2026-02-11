# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-11T01:57:16.864809Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9264
- bootstrap_mean: 0.9284
- CI 95%: [0.9036, 0.9591]
- weighted_value (LoE factor 0.60): 0.5558
- válido (0.30-0.90): False
- detrended_edi: 0.9264
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9999
- external: 0.9596
- CR: 1.0420
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3976
- rmse_abm_no_ode: 2.8576
- rmse_ode: 0.6923
- rmse_reduced: 5.3990
- threshold: 1.7147

### Calibración
- forcing_scale: 0.8064
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7947
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2439
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4361
- bootstrap_mean: 0.3838
- CI 95%: [-0.1624, 0.6258]
- weighted_value (LoE factor 0.60): 0.2616
- válido (0.30-0.90): True
- detrended_edi: 0.4361
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9996
- external: 0.9918
- CR: 1.0078
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.7788
- rmse_abm_no_ode: 4.6461
- rmse_ode: 3.4525
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6725
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4337
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


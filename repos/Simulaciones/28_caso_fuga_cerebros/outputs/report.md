# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-10T04:21:24.632429Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8814
- bootstrap_mean: 0.8821
- CI 95%: [0.8521, 0.9129]
- weighted_value (LoE factor 0.60): 0.5288
- válido (0.30-0.90): True
- detrended_edi: 0.8814
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 1.0000
- external: 0.9555
- CR: 1.0465
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3411
- rmse_abm_no_ode: 2.8750
- rmse_ode: 0.6951
- rmse_reduced: 5.3990
- threshold: 1.7147

### Calibración
- forcing_scale: 0.6498
- macro_coupling: 0.4527
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6327
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2579
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1861
- bootstrap_mean: 0.1840
- CI 95%: [0.0748, 0.2795]
- weighted_value (LoE factor 0.60): 0.1117
- válido (0.30-0.90): False
- detrended_edi: 0.1861
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9995
- external: 0.9917
- CR: 1.0079
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.7737
- rmse_abm_no_ode: 4.6365
- rmse_ode: 3.4526
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6703
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4344
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


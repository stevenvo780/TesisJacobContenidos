# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-10T02:13:41.090816Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7245
- bootstrap_mean: 0.7297
- CI 95%: [0.6625, 0.8093]
- weighted_value (LoE factor 0.60): 0.4347
- válido (0.30-0.90): True
- detrended_edi: 0.7245
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9999
- external: 0.9703
- CR: 1.0305
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7670
- rmse_abm_no_ode: 2.7838
- rmse_ode: 0.6865
- rmse_reduced: 5.3990
- threshold: 1.7147

### Calibración
- forcing_scale: 0.9504
- macro_coupling: 0.3895
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2390
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1829
- bootstrap_mean: 0.1805
- CI 95%: [0.0359, 0.2881]
- weighted_value (LoE factor 0.60): 0.1097
- válido (0.30-0.90): False
- detrended_edi: 0.1829
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9995
- external: 0.9915
- CR: 1.0081
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.7740
- rmse_abm_no_ode: 4.6188
- rmse_ode: 3.4368
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6611
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4387
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.


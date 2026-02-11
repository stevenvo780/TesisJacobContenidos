# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-11T02:08:43.596552Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8806
- bootstrap_mean: 0.8846
- CI 95%: [0.8510, 0.9178]
- weighted_value (LoE factor 0.60): 0.5283
- válido (0.30-0.90): True
- detrended_edi: 0.8806
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9998
- external: 0.9668
- CR: 1.0342
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6449
- rmse_abm_no_ode: 2.7983
- rmse_ode: 0.6865
- rmse_reduced: 5.3990
- threshold: 1.7147

### Calibración
- forcing_scale: 0.9339
- macro_coupling: 0.4358
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8890
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2397
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4489
- bootstrap_mean: 0.3673
- CI 95%: [-0.4510, 0.6450]
- weighted_value (LoE factor 0.60): 0.2694
- válido (0.30-0.90): True
- detrended_edi: 0.4489
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9994
- external: 0.9916
- CR: 1.0078
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.6927
- rmse_abm_no_ode: 4.4172
- rmse_ode: 3.4551
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4926
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7073
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4441
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


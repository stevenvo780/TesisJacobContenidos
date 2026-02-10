# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T04:22:23.481872Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8884
- bootstrap_mean: 0.8882
- CI 95%: [0.8748, 0.9008]
- weighted_value (LoE factor 0.60): 0.5330
- válido (0.30-0.90): True
- detrended_edi: 0.8884
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9699
- CR: 1.0310
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1416
- rmse_abm_no_ode: 1.2685
- rmse_ode: 6.7533
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3434
- macro_coupling: 0.4469
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3428
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1168
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6328
- bootstrap_mean: 0.6367
- CI 95%: [0.5335, 0.7516]
- weighted_value (LoE factor 0.60): 0.3797
- válido (0.30-0.90): True
- detrended_edi: 0.6328
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9998
- external: 0.9787
- CR: 1.0216
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5045
- rmse_abm_no_ode: 1.3739
- rmse_ode: 2.6688
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.6588
- macro_coupling: 0.3581
- ode_coupling_strength: 0.2865
- abm_feedback_gamma: 0.0500
- damping: 0.7095
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1862
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


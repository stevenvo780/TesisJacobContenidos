# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T02:49:50.221506Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7320
- bootstrap_mean: 0.7322
- CI 95%: [0.7237, 0.7418]
- weighted_value (LoE factor 0.60): 0.4392
- válido (0.30-0.90): True
- detrended_edi: 0.7320
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9829
- CR: 1.0174
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3379
- rmse_abm_no_ode: 1.2608
- rmse_ode: 5.7437
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3353
- macro_coupling: 0.2700
- ode_coupling_strength: 0.2160
- abm_feedback_gamma: 0.0500
- damping: 0.3342
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1169
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.5779
- bootstrap_mean: 0.5760
- CI 95%: [0.4381, 0.7047]
- weighted_value (LoE factor 0.60): 0.3468
- válido (0.30-0.90): True
- detrended_edi: 0.5779
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9991
- external: 0.9770
- CR: 1.0226
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4908
- rmse_abm_no_ode: 1.1628
- rmse_ode: 2.5682
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.8812
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1448
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-11T04:42:56.503654Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8500
- bootstrap_mean: 0.8503
- CI 95%: [0.8292, 0.8716]
- weighted_value (LoE factor 0.20): 0.1700
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9997
- external: 0.9894
- CR: 1.0105
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3548
- rmse_abm_no_ode: 0.3630
- rmse_ode: 0.5021
- rmse_reduced: 2.3657
- threshold: 0.3900

### Calibración
- forcing_scale: 0.7879
- macro_coupling: 0.4837
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7919
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2939
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.4295
- bootstrap_mean: 0.4288
- CI 95%: [0.3338, 0.5174]
- weighted_value (LoE factor 0.20): 0.0859
- válido (0.30-0.90): True
- detrended_edi: 0.4295
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9984
- external: 0.9910
- CR: 1.0075
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5475
- rmse_abm_no_ode: 0.7548
- rmse_ode: 0.9043
- rmse_reduced: 0.9596
- threshold: 0.1452

### Calibración
- forcing_scale: 0.9504
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3593
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


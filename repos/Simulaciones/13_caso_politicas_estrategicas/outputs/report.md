# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-11T02:08:45.397400Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8484
- bootstrap_mean: 0.8482
- CI 95%: [0.8249, 0.8687]
- weighted_value (LoE factor 0.20): 0.1697
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9892
- CR: 1.0106
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3587
- rmse_abm_no_ode: 0.3621
- rmse_ode: 0.5025
- rmse_reduced: 2.3657
- threshold: 0.3900

### Calibración
- forcing_scale: 0.8720
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8166
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2940
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.4212
- bootstrap_mean: 0.4237
- CI 95%: [0.3215, 0.4917]
- weighted_value (LoE factor 0.20): 0.0842
- válido (0.30-0.90): True
- detrended_edi: 0.4212
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9996
- external: 0.9944
- CR: 1.0052
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5554
- rmse_abm_no_ode: 0.7097
- rmse_ode: 0.9008
- rmse_reduced: 0.9596
- threshold: 0.1452

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3584
- ode_coupling_strength: 0.2867
- abm_feedback_gamma: 0.0500
- damping: 0.8903
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3602
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T05:36:32.148968Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8397
- bootstrap_mean: 0.8398
- CI 95%: [0.8314, 0.8496]
- weighted_value (LoE factor 0.60): 0.5038
- válido (0.30-0.90): True
- detrended_edi: 0.8397
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9782
- CR: 1.0222
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2044
- rmse_abm_no_ode: 1.2749
- rmse_ode: 6.1094
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.4452
- macro_coupling: 0.4345
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4483
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1173
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6507
- bootstrap_mean: 0.6515
- CI 95%: [0.5530, 0.7523]
- weighted_value (LoE factor 0.60): 0.3904
- válido (0.30-0.90): True
- detrended_edi: 0.6507
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9999
- external: 0.9708
- CR: 1.0300
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5213
- rmse_abm_no_ode: 1.4924
- rmse_ode: 2.8016
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.5133
- macro_coupling: 0.3768
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5751
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2365
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


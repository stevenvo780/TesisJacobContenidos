# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T15:44:56.946891Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.4609
- bootstrap_mean: 0.4614
- CI 95%: [0.4545, 0.4695]
- weighted_value (LoE factor 0.60): 0.2765
- válido (0.30-0.90): True
- detrended_edi: 0.4609
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9921
- CR: 1.0080
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6758
- rmse_abm_no_ode: 1.2534
- rmse_ode: 4.7521
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.5000
- macro_coupling: 0.2500
- ode_coupling_strength: 0.2000
- abm_feedback_gamma: 0.0500
- damping: 0.5000
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1176
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.5270
- bootstrap_mean: 0.5236
- CI 95%: [0.3767, 0.6797]
- weighted_value (LoE factor 0.60): 0.3162
- válido (0.30-0.90): True
- detrended_edi: 0.5270
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9994
- external: 0.9801
- CR: 1.0197
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4951
- rmse_abm_no_ode: 1.0468
- rmse_ode: 2.5236
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.8691
- macro_coupling: 0.4417
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8683
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1649
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Energía (Consumo Per Cápita)

- generated_at: 2026-02-12T03:57:09.185598Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3298
- bootstrap_mean: 0.3318
- CI 95%: [0.2880, 0.3796]
- weighted_value (LoE factor 0.60): 0.1979
- válido (0.30-0.90): True
- detrended_edi: 0.3298
- trend_ratio: 1.000
- trend_r2: 0.852

### Symploké y CR
- internal: 0.9994
- external: 0.9934
- CR: 1.0060
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5253
- rmse_abm_no_ode: 2.2760
- rmse_ode: 5.3403
- rmse_reduced: 4.9588
- threshold: 1.1854

### Calibración
- forcing_scale: 0.8527
- macro_coupling: 0.6000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2866
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.6503
- bootstrap_mean: 0.6451
- CI 95%: [0.4447, 0.7885]
- weighted_value (LoE factor 0.60): 0.3902
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9987
- external: 0.9970
- CR: 1.0018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4269
- rmse_abm_no_ode: 1.2207
- rmse_ode: 2.1207
- rmse_reduced: 2.6081
- threshold: 0.3586

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6596
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2256
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


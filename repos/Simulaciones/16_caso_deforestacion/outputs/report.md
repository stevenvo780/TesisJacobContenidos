# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-11T05:16:16.140077Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9076
- bootstrap_mean: 0.9077
- CI 95%: [0.9026, 0.9132]
- weighted_value (LoE factor 0.60): 0.5446
- válido (0.30-0.90): False
- detrended_edi: 0.9076
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9830
- CR: 1.0173
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3498
- rmse_abm_no_ode: 1.2607
- rmse_ode: 5.7096
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3651
- macro_coupling: 0.2681
- ode_coupling_strength: 0.2145
- abm_feedback_gamma: 0.0500
- damping: 0.3382
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1167
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8579
- bootstrap_mean: 0.8577
- CI 95%: [0.8197, 0.8970]
- weighted_value (LoE factor 0.60): 0.5147
- válido (0.30-0.90): True
- detrended_edi: 0.8579
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9990
- external: 0.9759
- CR: 1.0237
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5018
- rmse_abm_no_ode: 1.1695
- rmse_ode: 2.5797
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.9291
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1491
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-11T01:00:58.233055Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9132
- bootstrap_mean: 0.9130
- CI 95%: [0.9024, 0.9228]
- weighted_value (LoE factor 0.60): 0.5479
- válido (0.30-0.90): False
- detrended_edi: 0.9132
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9719
- CR: 1.0289
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1100
- rmse_abm_no_ode: 1.2681
- rmse_ode: 6.5983
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3371
- macro_coupling: 0.4094
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3368
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1169
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6313
- bootstrap_mean: 0.6332
- CI 95%: [0.5333, 0.7396]
- weighted_value (LoE factor 0.60): 0.3788
- válido (0.30-0.90): True
- detrended_edi: 0.6313
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9996
- external: 0.9751
- CR: 1.0250
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4870
- rmse_abm_no_ode: 1.3209
- rmse_ode: 2.6975
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.7491
- macro_coupling: 0.4518
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7957
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1653
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


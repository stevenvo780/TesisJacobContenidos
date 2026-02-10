# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T06:22:57.148853Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2530
- bootstrap_mean: 0.2533
- CI 95%: [0.2493, 0.2580]
- weighted_value (LoE factor 0.60): 0.1518
- válido (0.30-0.90): False
- detrended_edi: 0.2530
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9970
- CR: 1.0030
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9572
- rmse_abm_no_ode: 1.2814
- rmse_ode: 3.7805
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.4212
- macro_coupling: 0.1277
- ode_coupling_strength: 0.1022
- abm_feedback_gamma: 0.0500
- damping: 0.4258
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1171
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5605
- bootstrap_mean: 0.5583
- CI 95%: [0.4235, 0.6670]
- weighted_value (LoE factor 0.60): 0.3363
- válido (0.30-0.90): True
- detrended_edi: 0.5605
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9993
- external: 0.9760
- CR: 1.0238
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5027
- rmse_abm_no_ode: 1.1438
- rmse_ode: 2.6593
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1585
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


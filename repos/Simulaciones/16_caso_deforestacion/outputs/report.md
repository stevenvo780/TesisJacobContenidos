# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T03:42:03.205520Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9162
- bootstrap_mean: 0.9160
- CI 95%: [0.9086, 0.9233]
- weighted_value (LoE factor 0.60): 0.5497
- válido (0.30-0.90): False
- detrended_edi: 0.9162
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9733
- CR: 1.0275
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1063
- rmse_abm_no_ode: 1.2684
- rmse_ode: 6.4926
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3475
- macro_coupling: 0.4026
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3479
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1169
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.6399
- bootstrap_mean: 0.6425
- CI 95%: [0.5457, 0.7482]
- weighted_value (LoE factor 0.60): 0.3839
- válido (0.30-0.90): True
- detrended_edi: 0.6399
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9998
- external: 0.9753
- CR: 1.0251
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4928
- rmse_abm_no_ode: 1.3683
- rmse_ode: 2.7138
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.6571
- macro_coupling: 0.4031
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7070
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1869
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


# Reporte de Validación — Movilidad Urbana (Vehículos)

- generated_at: 2026-02-11T16:05:12.975806Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8528
- bootstrap_mean: 0.8532
- CI 95%: [0.8410, 0.8660]
- weighted_value (LoE factor 1.00): 0.8528
- válido (0.30-0.90): True
- detrended_edi: 0.8528
- trend_ratio: 1.000
- trend_r2: 0.880

### Symploké y CR
- internal: 0.9997
- external: 0.9990
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4086
- rmse_abm_no_ode: 0.4343
- rmse_ode: 0.4241
- rmse_reduced: 2.7752
- threshold: 0.6691

### Calibración
- forcing_scale: 0.8911
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0819
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1979
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.7675
- bootstrap_mean: 0.7683
- CI 95%: [0.7056, 0.8277]
- weighted_value (LoE factor 1.00): 0.7675
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9995
- external: 0.9951
- CR: 1.0045
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1263
- rmse_abm_no_ode: 1.2912
- rmse_ode: 1.9321
- rmse_reduced: 4.8437
- threshold: 1.8501

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6585
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 0.1508
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


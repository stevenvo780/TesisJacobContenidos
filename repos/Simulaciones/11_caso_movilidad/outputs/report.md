# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-11T02:08:58.838120Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -33.5369
- CI 95%: [-39.2810, -28.5877]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.2144
- CR: 4.6618
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 17.3539
- rmse_abm_no_ode: 0.5061
- rmse_ode: 32.4334
- rmse_reduced: 0.5061
- threshold: 0.4998

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8718
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9985
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6632
- bootstrap_mean: 0.6602
- CI 95%: [0.5113, 0.7619]
- weighted_value (LoE factor 0.20): 0.1326
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9947
- external: 0.8542
- CR: 1.1645
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6311
- rmse_abm_no_ode: 1.8599
- rmse_ode: 11.5407
- rmse_reduced: 4.8437
- threshold: 1.8501

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2426
- ode_coupling_strength: 0.1941
- abm_feedback_gamma: 0.0500
- damping: 0.7073
- ode_alpha: 0.0989
- ode_beta: 0.7941
- assimilation_strength: 0.0000
- calibration_rmse: 0.1617
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


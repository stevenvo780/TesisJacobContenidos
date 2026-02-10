# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-10T04:21:44.087329Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3338
- bootstrap_mean: 0.3362
- CI 95%: [0.3113, 0.3673]
- weighted_value (LoE factor 0.60): 0.2003
- válido (0.30-0.90): True
- detrended_edi: 0.3338
- trend_ratio: 1.000
- trend_r2: 0.960

### Symploké y CR
- internal: 1.0000
- external: 0.9942
- CR: 1.0058
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9140
- rmse_abm_no_ode: 1.3719
- rmse_ode: 0.4885
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.6290
- macro_coupling: 0.2176
- ode_coupling_strength: 0.1741
- abm_feedback_gamma: 0.0500
- damping: 0.6149
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2184
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.1895
- CI 95%: [-2.6714, -1.8002]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9996
- external: 0.8938
- CR: 1.1183
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4308
- rmse_abm_no_ode: 0.4505
- rmse_ode: 3.8035
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.6133
- macro_coupling: 0.4774
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6356
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2927
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


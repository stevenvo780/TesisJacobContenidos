# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-11T01:51:11.683434Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6623
- bootstrap_mean: 0.6651
- CI 95%: [0.6276, 0.7083]
- weighted_value (LoE factor 0.60): 0.3974
- válido (0.30-0.90): True
- detrended_edi: 0.6623
- trend_ratio: 1.000
- trend_r2: 0.960

### Symploké y CR
- internal: 1.0000
- external: 0.9989
- CR: 1.0011
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2020
- rmse_abm_no_ode: 1.3736
- rmse_ode: 0.4755
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.7767
- macro_coupling: 0.0833
- ode_coupling_strength: 0.0667
- abm_feedback_gamma: 0.0500
- damping: 0.7726
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2132
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4461
- bootstrap_mean: 0.4484
- CI 95%: [0.4040, 0.5003]
- weighted_value (LoE factor 0.60): 0.2677
- válido (0.30-0.90): True
- detrended_edi: 0.4461
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9990
- external: 0.9205
- CR: 1.0852
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2941
- rmse_abm_no_ode: 0.3910
- rmse_ode: 3.7946
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.7783
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7916
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2833
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


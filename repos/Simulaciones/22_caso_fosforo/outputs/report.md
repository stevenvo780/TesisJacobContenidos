# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-11T04:45:46.068286Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7935
- bootstrap_mean: 0.7957
- CI 95%: [0.7566, 0.8373]
- weighted_value (LoE factor 0.60): 0.4761
- válido (0.30-0.90): True
- detrended_edi: 0.7935
- trend_ratio: 1.000
- trend_r2: 0.960

### Symploké y CR
- internal: 0.9997
- external: 0.9925
- CR: 1.0073
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7348
- rmse_abm_no_ode: 1.3352
- rmse_ode: 0.4978
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.9253
- macro_coupling: 0.4182
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2112
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4794
- bootstrap_mean: 0.4804
- CI 95%: [0.4323, 0.5371]
- weighted_value (LoE factor 0.60): 0.2877
- válido (0.30-0.90): True
- detrended_edi: 0.4794
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9984
- external: 0.9373
- CR: 1.0652
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2162
- rmse_abm_no_ode: 0.3283
- rmse_ode: 3.7866
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9172
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2786
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


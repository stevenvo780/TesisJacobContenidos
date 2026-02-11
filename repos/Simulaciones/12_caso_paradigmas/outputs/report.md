# Reporte de Validación — Paradigmas Científicos (R&D)

- generated_at: 2026-02-11T16:09:43.399938Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.6971
- bootstrap_mean: 0.6973
- CI 95%: [0.6732, 0.7208]
- weighted_value (LoE factor 0.20): 0.1394
- válido (0.30-0.90): True
- detrended_edi: 0.6971
- trend_ratio: 1.000
- trend_r2: 0.875

### Symploké y CR
- internal: 1.0000
- external: 0.9990
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5378
- rmse_abm_no_ode: 0.1228
- rmse_ode: 3.0492
- rmse_reduced: 1.7755
- threshold: 0.3408

### Calibración
- forcing_scale: 0.1795
- macro_coupling: 0.4980
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1944
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3099
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2604
- bootstrap_mean: 0.2857
- CI 95%: [0.1999, 0.4994]
- weighted_value (LoE factor 0.20): 0.0521
- válido (0.30-0.90): False
- detrended_edi: 0.2604
- trend_ratio: 1.000
- trend_r2: 0.902

### Symploké y CR
- internal: 0.9974
- external: 0.9878
- CR: 1.0097
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.6057
- rmse_abm_no_ode: 6.6314
- rmse_ode: 6.3950
- rmse_reduced: 8.9315
- threshold: 5.7385

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8767
- ode_alpha: 0.1267
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8872
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


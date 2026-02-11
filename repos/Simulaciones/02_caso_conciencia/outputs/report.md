# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-11T14:15:27.418187Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4729
- bootstrap_mean: 0.4776
- CI 95%: [0.3388, 0.6195]
- weighted_value (LoE factor 0.20): 0.0946
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7342
- rmse_abm_no_ode: 0.8603
- rmse_ode: 1.2228
- rmse_reduced: 1.3929
- threshold: 0.2321

### Calibración
- forcing_scale: 0.6075
- macro_coupling: 0.0774
- ode_coupling_strength: 0.0619
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.3243
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6852
- bootstrap_mean: 0.6833
- CI 95%: [0.5521, 0.7732]
- weighted_value (LoE factor 0.20): 0.1370
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7119
- rmse_abm_no_ode: 0.7968
- rmse_ode: 2.1010
- rmse_reduced: 2.2615
- threshold: 0.6211

### Calibración
- forcing_scale: 0.9527
- macro_coupling: 0.4407
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0780
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


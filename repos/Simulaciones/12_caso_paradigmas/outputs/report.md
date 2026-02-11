# Reporte de Validación — Paradigmas Cientificos (Ising)

- generated_at: 2026-02-11T01:25:27.445677Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2808
- bootstrap_mean: 0.2808
- CI 95%: [0.2749, 0.2867]
- weighted_value (LoE factor 0.20): 0.0562
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9979
- CR: 1.0020
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3684
- rmse_abm_no_ode: 0.5122
- rmse_ode: 0.6316
- rmse_reduced: 2.0980
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3005
- ode_coupling_strength: 0.2404
- abm_feedback_gamma: 0.0500
- damping: 0.8216
- ode_alpha: 0.0312
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4738
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0101
- bootstrap_mean: -0.0110
- CI 95%: [-0.0199, -0.0081]
- weighted_value (LoE factor 0.20): -0.0020
- válido (0.30-0.90): False
- detrended_edi: -0.0101
- trend_ratio: 1.000
- trend_r2: 0.902

### Symploké y CR
- internal: 0.9547
- external: 0.9378
- CR: 1.0180
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.2565
- rmse_abm_no_ode: 9.1639
- rmse_ode: 9.4260
- rmse_reduced: 8.9315
- threshold: 5.7385

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8120
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.


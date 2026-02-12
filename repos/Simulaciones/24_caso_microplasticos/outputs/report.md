# Reporte de Validación — Microplásticos Oceánicos (Jambeck Accumulation-Decay)

- generated_at: 2026-02-12T04:08:01.260559Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0760
- bootstrap_mean: 0.0771
- CI 95%: [0.0693, 0.0920]
- weighted_value (LoE factor 0.60): 0.0456
- válido (0.30-0.90): False
- detrended_edi: 0.0760
- trend_ratio: 1.000
- trend_r2: 0.820

### Symploké y CR
- internal: 0.9992
- external: 0.9992
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4408
- rmse_abm_no_ode: 1.5592
- rmse_ode: 2.5636
- rmse_reduced: 3.1418
- threshold: 0.8551

### Calibración
- forcing_scale: 0.7902
- macro_coupling: 0.1899
- ode_coupling_strength: 0.1519
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1920
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6168
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8057
- bootstrap_mean: 0.8002
- CI 95%: [0.7011, 0.8799]
- weighted_value (LoE factor 0.60): 0.4834
- válido (0.30-0.90): True
- detrended_edi: 0.8057
- trend_ratio: 1.000
- trend_r2: 0.978

### Symploké y CR
- internal: 0.9998
- external: 0.9997
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3232
- rmse_abm_no_ode: 1.6636
- rmse_ode: 2.1184
- rmse_reduced: 2.3810
- threshold: 0.4297

### Calibración
- forcing_scale: 0.6576
- macro_coupling: 0.4424
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.4448
- ode_alpha: 0.0152
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3781
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


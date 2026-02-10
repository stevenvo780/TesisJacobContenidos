# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-10T05:41:26.818994Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3681
- bootstrap_mean: 0.3686
- CI 95%: [0.3597, 0.3803]
- weighted_value (LoE factor 0.80): 0.2945
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9964
- CR: 1.0036
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9802
- rmse_abm_no_ode: 1.5511
- rmse_ode: 1.7419
- rmse_reduced: 0.9685
- threshold: 0.1000

### Calibración
- forcing_scale: 0.5860
- macro_coupling: 0.3636
- ode_coupling_strength: 0.2909
- abm_feedback_gamma: 0.0500
- damping: 0.5840
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2164
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3397
- bootstrap_mean: 0.3404
- CI 95%: [0.3298, 0.3581]
- weighted_value (LoE factor 0.80): 0.2717
- válido (0.30-0.90): True
- detrended_edi: 0.3397
- trend_ratio: 1.000
- trend_r2: 0.970

### Symploké y CR
- internal: 1.0000
- external: 0.9990
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 11.5490
- rmse_abm_no_ode: 17.4895
- rmse_ode: 2.8358
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.8755
- macro_coupling: 0.3624
- ode_coupling_strength: 0.2899
- abm_feedback_gamma: 0.0500
- damping: 0.5022
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3920
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


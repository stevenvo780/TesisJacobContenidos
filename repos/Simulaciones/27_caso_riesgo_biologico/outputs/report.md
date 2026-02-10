# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-10T04:21:11.279365Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3449
- bootstrap_mean: 0.3464
- CI 95%: [0.2686, 0.4119]
- weighted_value (LoE factor 0.80): 0.2760
- válido (0.30-0.90): True
- detrended_edi: 0.3449
- trend_ratio: 1.000
- trend_r2: 0.602

### Symploké y CR
- internal: 0.9988
- external: 0.9897
- CR: 1.0091
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0660
- rmse_abm_no_ode: 1.6273
- rmse_ode: 0.7394
- rmse_reduced: 2.4983
- threshold: 0.7584

### Calibración
- forcing_scale: 0.4772
- macro_coupling: 0.4890
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6484
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7386
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1035
- bootstrap_mean: 0.0864
- CI 95%: [-0.1199, 0.1911]
- weighted_value (LoE factor 0.80): 0.0828
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9984
- CR: 1.0015
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5576
- rmse_abm_no_ode: 0.6220
- rmse_ode: 1.0993
- rmse_reduced: 2.1156
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0798
- ode_coupling_strength: 0.0639
- abm_feedback_gamma: 0.0500
- damping: 0.6458
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1937
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


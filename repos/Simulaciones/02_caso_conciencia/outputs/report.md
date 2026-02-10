# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-10T05:34:41.598848Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0504
- bootstrap_mean: 0.0498
- CI 95%: [0.0267, 0.0726]
- weighted_value (LoE factor 0.20): 0.0101
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4680
- external: 0.5557
- CR: 0.8421
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0657
- rmse_abm_no_ode: 1.1223
- rmse_ode: 1.0802
- rmse_reduced: 1.1208
- threshold: 1.0629

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5453
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7550
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0577
- bootstrap_mean: 0.0667
- CI 95%: [0.0404, 0.1373]
- weighted_value (LoE factor 0.20): 0.0115
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9226
- external: 0.8847
- CR: 1.0428
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8765
- rmse_abm_no_ode: 0.9302
- rmse_ode: 1.5649
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2246
- ode_coupling_strength: 0.1797
- abm_feedback_gamma: 0.0500
- damping: 0.7190
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1548
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


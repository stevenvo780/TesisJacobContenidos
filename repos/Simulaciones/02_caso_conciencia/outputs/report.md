# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-11T05:15:13.403229Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0176
- bootstrap_mean: 0.0176
- CI 95%: [-0.0127, 0.0476]
- weighted_value (LoE factor 0.20): 0.0035
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.5365
- external: 0.6266
- CR: 0.8562
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1011
- rmse_abm_no_ode: 1.1223
- rmse_ode: 1.0792
- rmse_reduced: 1.1208
- threshold: 1.0629

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1417
- ode_coupling_strength: 0.1133
- abm_feedback_gamma: 0.0500
- damping: 0.5129
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7647
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3820
- bootstrap_mean: 0.3662
- CI 95%: [-0.2335, 0.7587]
- weighted_value (LoE factor 0.20): 0.0764
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9099
- external: 0.8834
- CR: 1.0300
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8307
- rmse_abm_no_ode: 0.9302
- rmse_ode: 1.5653
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6601
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2050
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


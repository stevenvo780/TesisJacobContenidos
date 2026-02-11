# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-11T23:26:56.815212Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0367
- bootstrap_mean: 0.0382
- CI 95%: [0.0186, 0.0648]
- weighted_value (LoE factor 0.60): 0.0220
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9937
- external: 0.9902
- CR: 1.0035
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9444
- rmse_abm_no_ode: 0.9804
- rmse_ode: 0.8580
- rmse_reduced: 0.5841
- threshold: 0.5110

### Calibración
- forcing_scale: 0.9348
- macro_coupling: 0.2137
- ode_coupling_strength: 0.1710
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0964
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9368
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5885
- bootstrap_mean: 0.5916
- CI 95%: [0.4816, 0.7105]
- weighted_value (LoE factor 0.60): 0.3531
- válido (0.30-0.90): True
- detrended_edi: 0.5885
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9995
- external: 0.9838
- CR: 1.0160
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4835
- rmse_abm_no_ode: 1.1750
- rmse_ode: 2.5181
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3666
- ode_coupling_strength: 0.2933
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1492
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.


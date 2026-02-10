# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-10T04:20:59.895570Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: 0.0001
- CI 95%: [0.0001, 0.0001]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False
- detrended_edi: 0.0001
- trend_ratio: 1.000
- trend_r2: 0.955

### Symploké y CR
- internal: 0.0023
- external: 0.0023
- CR: 0.9819
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0437
- rmse_abm_no_ode: 2.0440
- rmse_ode: 2.0428
- rmse_reduced: 2.0406
- threshold: 0.4782

### Calibración
- forcing_scale: 0.6290
- macro_coupling: 0.2176
- ode_coupling_strength: 0.1741
- abm_feedback_gamma: 0.0500
- damping: 0.6149
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1459
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: 0.0001
- CI 95%: [0.0001, 0.0001]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False
- detrended_edi: 0.0001
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.0028
- external: 0.0015
- CR: 1.8798
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.6842
- rmse_abm_no_ode: 2.6844
- rmse_ode: 2.6833
- rmse_reduced: 2.6812
- threshold: 0.8867

### Calibración
- forcing_scale: 0.6251
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6233
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0944
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


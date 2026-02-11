# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-11T01:03:24.516777Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0002
- bootstrap_mean: 0.0002
- CI 95%: [0.0002, 0.0002]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False
- detrended_edi: 0.0002
- trend_ratio: 1.000
- trend_r2: 0.955

### Symploké y CR
- internal: 0.0033
- external: 0.0019
- CR: 1.6904
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
- forcing_scale: 0.7713
- macro_coupling: 0.0664
- ode_coupling_strength: 0.0531
- abm_feedback_gamma: 0.0500
- damping: 0.7651
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1430
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False
- detrended_edi: 0.0000
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.0046
- external: 0.0001
- CR: 33.5724
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.6843
- rmse_abm_no_ode: 2.6844
- rmse_ode: 2.6833
- rmse_reduced: 2.6812
- threshold: 0.8867

### Calibración
- forcing_scale: 0.7739
- macro_coupling: 0.4996
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7820
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0767
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.


# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-09T14:55:41.379523Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.6037
- bootstrap_mean: -0.6056
- CI 95%: [-0.6703, -0.5496]
- weighted_value (LoE factor 1.00): -0.6037
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.8755
- CR: 1.1420
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.2896
- rmse_abm_no_ode: 3.9219
- rmse_ode: 6.3540
- rmse_reduced: 7.0276
- threshold: 2.6830

### Calibración
- forcing_scale: 0.3668
- macro_coupling: 0.9542
- damping: 0.5381
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1563

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.2992
- bootstrap_mean: -0.3003
- CI 95%: [-0.3262, -0.2779]
- weighted_value (LoE factor 1.00): -0.2992
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9822
- external: 0.9153
- CR: 1.0731
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.5489
- rmse_abm_no_ode: 1.1922
- rmse_ode: 1.7244
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6911
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6353


# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-08T21:31:50.599756Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0178
- bootstrap_mean: -0.0178
- CI 95%: [-0.0186, -0.0172]
- weighted_value (LoE factor 0.20): -0.0036
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2691
- rmse_abm_no_ode: 1.2469
- rmse_ode: 3.7986
- rmse_reduced: 4.3404
- threshold: 1.2888

### Calibración
- forcing_scale: 0.5759
- macro_coupling: 0.1666
- damping: 0.8930
- ode_alpha: 0.1166
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1058

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0004
- bootstrap_mean: 0.0004
- CI 95%: [-0.0017, 0.0021]
- weighted_value (LoE factor 0.20): 0.0001
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9992
- CR: 0.9998
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1779
- rmse_abm_no_ode: 1.1784
- rmse_ode: 1.4479
- rmse_reduced: 1.4484
- threshold: 1.2251

### Calibración
- forcing_scale: 0.8523
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6665


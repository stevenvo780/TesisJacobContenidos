# Reporte de Validación — Fuga de Cerebros Global

- generated_at: 2026-02-08T20:44:17.151991Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.8967
- bootstrap_mean: -1.9002
- CI 95%: [-2.0459, -1.7569]
- weighted_value (LoE factor 0.20): -0.3793
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9993
- CR: 1.0005
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1418
- rmse_abm_no_ode: 0.3942
- rmse_ode: 1.3907
- rmse_reduced: 1.7375
- threshold: 0.2904

### Calibración
- forcing_scale: 0.1487
- macro_coupling: 0.9510
- damping: 0.1528
- ode_alpha: 0.0545
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2476

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0489
- bootstrap_mean: -0.0559
- CI 95%: [-0.1351, -0.0052]
- weighted_value (LoE factor 0.20): -0.0098
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9153
- external: 0.0195
- CR: 46.9559
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.1577
- rmse_abm_no_ode: 5.8704
- rmse_ode: 6.5732
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9587
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8349


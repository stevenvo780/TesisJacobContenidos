# Reporte de Validación — Erosión Dialéctica

- generated_at: 2026-02-08T20:52:27.531310Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4435
- bootstrap_mean: -0.4483
- CI 95%: [-0.6957, -0.2391]
- weighted_value (LoE factor 0.20): -0.0887
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: 0.0001
- CR: 8216.7154
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.3010
- rmse_abm_no_ode: 0.9013
- rmse_ode: 1.1943
- rmse_reduced: 1.5452
- threshold: 0.2495

### Calibración
- forcing_scale: 0.9824
- macro_coupling: 0.7164
- damping: 0.9500
- ode_alpha: 0.0559
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2503

## Fase real
- **overall_pass**: False

### EDI
- valor: -5.4705
- bootstrap_mean: -5.9292
- CI 95%: [-10.7924, -2.9741]
- weighted_value (LoE factor 0.20): -1.0941
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.5295
- external: 0.3356
- CR: 1.5776
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1360
- rmse_abm_no_ode: 0.1756
- rmse_ode: 2.5877
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9740
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1456


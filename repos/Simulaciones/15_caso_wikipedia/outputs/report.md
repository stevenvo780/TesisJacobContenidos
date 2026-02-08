# Reporte de Validación — Wikipedia Clima

- generated_at: 2026-02-07T14:56:33.331767Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.6468
- bootstrap_mean: 0.6470
- CI 95%: [0.6404, 0.6540]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.7515
- CR: 1.3306
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4123
- rmse_ode: 1.8845
- rmse_reduced: 6.8307
- threshold: 2.5747

### Calibración
- forcing_scale: 0.3661
- macro_coupling: 0.1000
- damping: 0.5812
- ode_alpha: 0.0241
- ode_beta: 0.8965
- assimilation_strength: 0.0000
- calibration_rmse: 0.1474

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0181
- bootstrap_mean: 0.0214
- CI 95%: [-0.0001, 0.0476]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8716
- CR: 1.1473
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.7296
- rmse_ode: 3.7844
- rmse_reduced: 3.7982
- threshold: 2.5160

### Calibración
- forcing_scale: 0.4849
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0358
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9284


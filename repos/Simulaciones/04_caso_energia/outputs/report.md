# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-07T16:07:45.329733Z

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
- **overall_pass**: True

### EDI
- valor: 0.3544
- bootstrap_mean: 0.3397
- CI 95%: [0.0241, 0.5788]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.8947
- CR: 1.1177
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9537
- rmse_ode: 2.5480
- rmse_reduced: 1.4773
- threshold: 1.2251

### Calibración
- forcing_scale: 0.8445
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6650


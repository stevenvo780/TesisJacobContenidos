# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-07T07:34:01.678490Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4616
- bootstrap_mean: 0.4632
- CI 95%: [0.4435, 0.4871]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.8376
- CR: 1.1939
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8226
- rmse_ode: 1.1754
- rmse_reduced: 5.2422
- threshold: 2.1312

### Calibración
- forcing_scale: 0.3226
- macro_coupling: 0.1119
- damping: 0.6076
- ode_alpha: 0.3767
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7709

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1248
- bootstrap_mean: 0.1263
- CI 95%: [0.0014, 0.2495]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.7327
- CR: 1.3647
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 7.5123
- rmse_ode: 8.9437
- rmse_reduced: 8.5833
- threshold: 8.1069

### Calibración
- forcing_scale: 0.7579
- macro_coupling: 1.0000
- damping: 0.8285
- ode_alpha: 0.0716
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5181


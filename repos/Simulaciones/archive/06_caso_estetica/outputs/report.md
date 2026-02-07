# Reporte de Validación — Estética (MoMA Paradigmas)

- generated_at: 2026-02-06T21:57:44.123895Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8317
- bootstrap_mean: 0.8331
- CI 95%: [0.7866, 0.8725]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9842
- CR: 1.0161
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4772
- rmse_ode: 0.7031
- rmse_reduced: 2.8355
- threshold: 0.4225

### Calibración
- forcing_scale: 0.1146
- macro_coupling: 0.3234
- damping: 0.1564
- ode_alpha: 0.4011
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5689

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0968
- bootstrap_mean: 0.0807
- CI 95%: [-0.1949, 0.3195]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9336
- CR: 1.0711
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3066
- rmse_ode: 1.3608
- rmse_reduced: 1.4467
- threshold: 0.6648

### Calibración
- forcing_scale: 0.1223
- macro_coupling: 0.0437
- damping: 0.1610
- ode_alpha: 0.3052
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8398


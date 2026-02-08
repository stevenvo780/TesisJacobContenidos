# Reporte de Validación — Salinización de Suelos

- generated_at: 2026-02-07T08:59:27.747510Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8261
- bootstrap_mean: 0.8257
- CI 95%: [0.7746, 0.8729]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9998
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3780
- rmse_ode: 0.4976
- rmse_reduced: 2.1732
- threshold: 0.6013

### Calibración
- forcing_scale: 0.6317
- macro_coupling: 0.5736
- damping: 0.9500
- ode_alpha: 0.4474
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4415

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1758
- bootstrap_mean: 0.1807
- CI 95%: [0.0995, 0.2603]
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9349
- external: 0.0356
- CR: 26.2572
- CR válido (>2.0): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8885
- rmse_ode: 0.9854
- rmse_reduced: 1.0780
- threshold: 0.1357

### Calibración
- forcing_scale: 0.7138
- macro_coupling: 0.8537
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2330


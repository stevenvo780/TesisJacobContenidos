# Reporte de Validación — Movilidad Urbana (MTA NYC)

- generated_at: 2026-02-07T00:34:20.035666Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6329
- bootstrap_mean: 0.6332
- CI 95%: [0.6267, 0.6404]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.7706
- CR: 1.2977
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 2.5217
- rmse_ode: 1.8845
- rmse_reduced: 6.8688
- threshold: 1.5448

### Calibración
- forcing_scale: 0.2409
- macro_coupling: 0.9334
- damping: 0.3930
- ode_alpha: 0.0241
- ode_beta: 0.8965
- assimilation_strength: 0.0000
- calibration_rmse: 0.1518

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0918
- bootstrap_mean: 0.0915
- CI 95%: [-0.0236, 0.2117]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8744
- CR: 1.1437
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9471
- rmse_ode: 1.8246
- rmse_reduced: 1.0428
- threshold: 0.0783

### Calibración
- forcing_scale: 0.5005
- macro_coupling: 0.8993
- damping: 0.7704
- ode_alpha: 0.4259
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5465


# Reporte de Validación — RTB Publicidad Programática

- generated_at: 2026-02-07T14:54:41.224993Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7396
- bootstrap_mean: 0.7400
- CI 95%: [0.7304, 0.7510]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9996
- CR: 1.0004
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3008
- rmse_ode: 1.0272
- rmse_reduced: 4.9964
- threshold: 1.6871

### Calibración
- forcing_scale: 0.4120
- macro_coupling: 0.7376
- damping: 0.5916
- ode_alpha: 0.0517
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1656

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9495
- bootstrap_mean: 0.9491
- CI 95%: [0.9408, 0.9579]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1465
- rmse_ode: 1.3752
- rmse_reduced: 2.9039
- threshold: 0.7042

### Calibración
- forcing_scale: 0.6332
- macro_coupling: 0.5559
- damping: 0.9500
- ode_alpha: 0.2264
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1102


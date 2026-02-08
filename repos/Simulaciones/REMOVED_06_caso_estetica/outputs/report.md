# Reporte de Validación — Estética Digital Global

- generated_at: 2026-02-07T14:00:48.657311Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7220
- bootstrap_mean: 0.7223
- CI 95%: [0.7148, 0.7303]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4926
- rmse_ode: 1.2363
- rmse_reduced: 5.3700
- threshold: 1.8240

### Calibración
- forcing_scale: 0.4140
- macro_coupling: 0.5797
- damping: 0.5973
- ode_alpha: 0.0434
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1484

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9493
- bootstrap_mean: 0.9493
- CI 95%: [0.9417, 0.9572]
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
- rmse_abm: 0.1597
- rmse_ode: 1.3532
- rmse_reduced: 3.1500
- threshold: 0.7903

### Calibración
- forcing_scale: 0.6336
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.2643
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1582


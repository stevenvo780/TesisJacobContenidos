# Reporte de Validación — Temperatura Oceánica Global

- generated_at: 2026-02-07T11:32:59.395676Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.9722
- bootstrap_mean: 0.9721
- CI 95%: [0.9697, 0.9745]
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
- rmse_abm: 0.0935
- rmse_ode: 0.6041
- rmse_reduced: 3.3592
- threshold: 0.8708

### Calibración
- forcing_scale: 0.6339
- macro_coupling: 0.1672
- damping: 0.9500
- ode_alpha: 0.1939
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0887

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9362
- bootstrap_mean: 0.9361
- CI 95%: [0.9313, 0.9410]
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
- rmse_abm: 0.2275
- rmse_ode: 0.4771
- rmse_reduced: 3.5656
- threshold: 0.9708

### Calibración
- forcing_scale: 0.6337
- macro_coupling: 0.5723
- damping: 0.9500
- ode_alpha: 0.3216
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1437


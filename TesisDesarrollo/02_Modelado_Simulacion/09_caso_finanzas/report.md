# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-07T08:14:24.748181Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.6386
- bootstrap_mean: 0.6388
- CI 95%: [0.6325, 0.6454]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.7485
- CR: 1.3359
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
- rmse_reduced: 6.6751
- threshold: 2.5747

### Calibración
- forcing_scale: 0.3661
- macro_coupling: 0.1000
- damping: 0.5812
- ode_alpha: 0.0241
- ode_beta: 0.8965
- assimilation_strength: 0.0000
- calibration_rmse: 0.1464

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8817
- bootstrap_mean: 0.8819
- CI 95%: [0.8743, 0.8895]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.8000
- CR: 1.2500
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3749
- rmse_ode: 3.9623
- rmse_reduced: 3.1701
- threshold: 1.1814

### Calibración
- forcing_scale: 0.6753
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4069


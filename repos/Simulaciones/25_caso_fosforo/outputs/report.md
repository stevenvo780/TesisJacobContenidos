# Reporte de Validación — Ciclo del Fósforo

- generated_at: 2026-02-07T15:23:28.570402Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8343
- bootstrap_mean: 0.8347
- CI 95%: [0.7863, 0.8722]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3738
- rmse_ode: 0.4620
- rmse_reduced: 2.2558
- threshold: 0.6090

### Calibración
- forcing_scale: 0.6232
- macro_coupling: 0.2742
- damping: 0.9500
- ode_alpha: 0.4434
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4432

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9015
- bootstrap_mean: 0.9036
- CI 95%: [0.8626, 0.9421]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9996
- external: 0.9998
- CR: 0.9998
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2300
- rmse_ode: 0.2994
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.6497
- macro_coupling: 0.6375
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2814


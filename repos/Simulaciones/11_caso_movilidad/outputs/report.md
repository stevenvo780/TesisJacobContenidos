# Reporte de Validación — Movilidad Urbana

- generated_at: 2026-02-07T14:34:42.427126Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7358
- bootstrap_mean: 0.7359
- CI 95%: [0.7305, 0.7419]
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
- rmse_abm: 1.3374
- rmse_ode: 2.1404
- rmse_reduced: 5.0619
- threshold: 1.6258

### Calibración
- forcing_scale: 0.3629
- macro_coupling: 0.7985
- damping: 0.5275
- ode_alpha: 0.0120
- ode_beta: 0.6462
- assimilation_strength: 0.0000
- calibration_rmse: 0.1473

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9146
- bootstrap_mean: 0.9148
- CI 95%: [0.9089, 0.9204]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 0.9999
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2912
- rmse_ode: 1.2510
- rmse_reduced: 3.4092
- threshold: 0.8521

### Calibración
- forcing_scale: 0.6038
- macro_coupling: 0.6974
- damping: 0.9041
- ode_alpha: 0.3124
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1316


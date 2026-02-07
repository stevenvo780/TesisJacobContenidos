# Reporte de Validación — Riesgo Biológico Global

- generated_at: 2026-02-07T09:11:38.631574Z

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
- valor: 0.8929
- bootstrap_mean: 0.8932
- CI 95%: [0.8861, 0.9005]
- válido (0.30-0.90): True

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
- rmse_abm: 0.2830
- rmse_ode: 1.6290
- rmse_reduced: 2.6421
- threshold: 0.5471

### Calibración
- forcing_scale: 0.6330
- macro_coupling: 0.5147
- damping: 0.9500
- ode_alpha: 0.2498
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1171


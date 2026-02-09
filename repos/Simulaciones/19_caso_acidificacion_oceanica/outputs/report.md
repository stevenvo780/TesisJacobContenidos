# Reporte de Validación — Acidificación Oceánica (CO2SYS + Revelle Factor)

- generated_at: 2026-02-09T02:37:12.347506Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9981
- external: 0.5604
- CR: 1.7811
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0374
- rmse_abm_no_ode: 1.0374
- rmse_ode: 8.3160
- rmse_reduced: 1.0373
- threshold: 1.0107

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.2222
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3188

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9980
- external: 0.5536
- CR: 1.8027
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0252
- rmse_abm_no_ode: 1.0252
- rmse_ode: 8.3531
- rmse_reduced: 1.0251
- threshold: 1.0063

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.2179
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3217


# Reporte de Validación — Wikipedia (Axelrod + Lotka-Volterra)

- generated_at: 2026-02-09T15:37:16.249537Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3171
- bootstrap_mean: 0.3172
- CI 95%: [0.3079, 0.3274]
- weighted_value (LoE factor 0.20): 0.0634
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4621
- external: 0.2874
- CR: 1.6079
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.8904
- rmse_abm_no_ode: 2.7683
- rmse_ode: 1.8747
- rmse_reduced: 2.7683
- threshold: 1.0224

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 2.2095

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.2851
- external: -0.2463
- CR: 1.1577
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 5.0287
- rmse_abm_no_ode: 5.0287
- rmse_ode: 3.6585
- rmse_reduced: 5.0287
- threshold: 2.2194

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.9966


# Reporte de Validación — Wikipedia (Axelrod + Lotka-Volterra)

- generated_at: 2026-02-09T03:08:25.942291Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4143
- bootstrap_mean: 0.4143
- CI 95%: [0.4012, 0.4287]
- weighted_value (LoE factor 0.20): 0.0829
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.6730
- external: 0.0819
- CR: 8.2125
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6215
- rmse_abm_no_ode: 2.7683
- rmse_ode: 1.7445
- rmse_reduced: 2.7683
- threshold: 1.0224

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.1149
- ode_beta: 0.1645
- assimilation_strength: 0.0000
- calibration_rmse: 2.1821

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4143
- bootstrap_mean: 0.4143
- CI 95%: [0.4012, 0.4287]
- weighted_value (LoE factor 0.20): 0.0829
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.6730
- external: 0.0819
- CR: 8.2125
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6215
- rmse_abm_no_ode: 2.7683
- rmse_ode: 1.7445
- rmse_reduced: 2.7683
- threshold: 1.0224

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.1149
- ode_beta: 0.1645
- assimilation_strength: 0.0000
- calibration_rmse: 2.1821


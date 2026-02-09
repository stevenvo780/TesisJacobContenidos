# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:31:40.344800Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -4.2796
- bootstrap_mean: -4.2850
- CI 95%: [-4.5472, -4.0525]
- weighted_value (LoE factor 0.80): -3.4237
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9323
- CR: 1.0726
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9710
- rmse_abm_no_ode: 0.7521
- rmse_ode: 5.8672
- rmse_reduced: 2.1182
- threshold: 0.1000

### Calibración
- forcing_scale: 0.2576
- macro_coupling: 0.4105
- damping: 0.2385
- ode_alpha: 0.0146
- ode_beta: 0.6916
- assimilation_strength: 0.0000
- calibration_rmse: 0.2119

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.6951
- bootstrap_mean: -3.0791
- CI 95%: [-6.1261, -1.1651]
- weighted_value (LoE factor 0.80): -2.1561
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8321
- external: 0.1526
- CR: 5.4539
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5744
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.1938
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210


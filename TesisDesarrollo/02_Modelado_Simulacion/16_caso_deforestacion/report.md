# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-09T14:20:09.050254Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -3.7153
- bootstrap_mean: -3.7162
- CI 95%: [-3.7875, -3.6555]
- weighted_value (LoE factor 0.60): -2.2292
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9277
- CR: 1.0779
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.9715
- rmse_abm_no_ode: 1.2664
- rmse_ode: 10.6172
- rmse_reduced: 3.7882
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3467
- macro_coupling: 0.5270
- damping: 0.3368
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1171

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0013
- bootstrap_mean: -1.0055
- CI 95%: [-1.1285, -0.9031]
- weighted_value (LoE factor 0.60): -0.6008
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.2937
- external: 0.5110
- CR: 0.5748
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3135
- rmse_abm_no_ode: 1.1560
- rmse_ode: 3.8452
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.9032
- macro_coupling: 0.8223
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1425


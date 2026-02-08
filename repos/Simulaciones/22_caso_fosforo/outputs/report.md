# Reporte de Validación — Ciclo del Fósforo

- generated_at: 2026-02-08T20:41:02.052001Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2123
- bootstrap_mean: -0.2137
- CI 95%: [-0.2383, -0.1911]
- weighted_value (LoE factor 0.20): -0.0425
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9980
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7211
- rmse_abm_no_ode: 1.4197
- rmse_ode: 2.3403
- rmse_reduced: 3.4527
- threshold: 0.8746

### Calibración
- forcing_scale: 0.9702
- macro_coupling: 0.5040
- damping: 0.9500
- ode_alpha: 0.3635
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3255

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.2935
- bootstrap_mean: -2.3172
- CI 95%: [-2.7600, -1.9828]
- weighted_value (LoE factor 0.20): -0.4587
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9915
- external: 0.9841
- CR: 1.0075
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0611
- rmse_abm_no_ode: 0.3222
- rmse_ode: 2.3008
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9812
- macro_coupling: 0.6333
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2771


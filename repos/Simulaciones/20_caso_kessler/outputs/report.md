# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-09T05:10:39.199087Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -3.2510
- bootstrap_mean: -3.2472
- CI 95%: [-3.3572, -3.1084]
- weighted_value (LoE factor 0.20): -0.6502
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8213
- external: 0.7879
- CR: 1.0423
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2532181.8668
- rmse_abm_no_ode: 595668.7239
- rmse_ode: 7501170013605142.0000
- rmse_reduced: 627263.5667
- threshold: 8.9265

### Calibración
- forcing_scale: 0.8343
- macro_coupling: 0.1000
- damping: 0.0852
- ode_alpha: 0.1132
- ode_beta: 0.7548
- assimilation_strength: 0.0000
- calibration_rmse: 135803.9513

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.4210
- bootstrap_mean: -3.4170
- CI 95%: [-3.5344, -3.2709]
- weighted_value (LoE factor 0.20): -0.6842
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8220
- external: 0.7978
- CR: 1.0304
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2557266.2041
- rmse_abm_no_ode: 578431.5679
- rmse_ode: 12877165873998824.0000
- rmse_reduced: 627223.1904
- threshold: 24.6834

### Calibración
- forcing_scale: 0.0513
- macro_coupling: 0.1636
- damping: 0.0000
- ode_alpha: 0.2575
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 130304.4870


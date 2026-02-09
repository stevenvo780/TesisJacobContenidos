# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-09T18:27:49.207036Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0478
- bootstrap_mean: 0.0478
- CI 95%: [0.0404, 0.0555]
- weighted_value (LoE factor 0.20): 0.0096
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9136
- external: 0.9039
- CR: 1.0107
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4025
- rmse_abm_no_ode: 0.4228
- rmse_ode: 0.4601
- rmse_reduced: 0.4390
- threshold: 0.3269

### Calibración
- forcing_scale: 0.0090
- macro_coupling: 0.1260
- ode_coupling_strength: 0.1008
- abm_feedback_gamma: 0.0500
- damping: 0.0272
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0172
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0031
- bootstrap_mean: -0.0031
- CI 95%: [-0.0037, -0.0026]
- weighted_value (LoE factor 0.20): -0.0006
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6251
- external: -0.5704
- CR: 1.0959
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6007
- rmse_abm_no_ode: 1.5958
- rmse_ode: 2.0696
- rmse_reduced: 1.5820
- threshold: 1.2251

### Calibración
- forcing_scale: 0.0078
- macro_coupling: 0.0741
- ode_coupling_strength: 0.0593
- abm_feedback_gamma: 0.0500
- damping: 0.0312
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0292
- ode_rolling: None


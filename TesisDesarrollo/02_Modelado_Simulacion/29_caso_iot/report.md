# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T18:53:36.367301Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3011
- bootstrap_mean: 0.3038
- CI 95%: [0.2640, 0.3501]
- weighted_value (LoE factor 0.80): 0.2409
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9996
- external: 0.9815
- CR: 1.0184
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9527
- rmse_abm_no_ode: 4.2250
- rmse_ode: 1.3078
- rmse_reduced: 6.3551
- threshold: 2.4845

### Calibración
- forcing_scale: 0.9036
- macro_coupling: 0.4346
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.3876
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5085
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0204
- bootstrap_mean: 0.0202
- CI 95%: [-0.0017, 0.0353]
- weighted_value (LoE factor 0.80): 0.0163
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9494
- CR: 1.0533
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 33.9301
- rmse_abm_no_ode: 34.6362
- rmse_ode: 34.4793
- rmse_reduced: 40.8516
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5887
- macro_coupling: 0.3683
- ode_coupling_strength: 0.2946
- abm_feedback_gamma: 0.0500
- damping: 0.2840
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5982
- ode_rolling: None


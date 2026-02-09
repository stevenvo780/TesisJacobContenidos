# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-09T18:54:40.598730Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0225
- bootstrap_mean: 0.0220
- CI 95%: [0.0002, 0.0427]
- weighted_value (LoE factor 0.20): 0.0045
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 33.8845
- rmse_abm_no_ode: 34.6640
- rmse_ode: 31.9215
- rmse_reduced: 89.1702
- threshold: 0.4998

### Calibración
- forcing_scale: 0.8052
- macro_coupling: 0.0756
- ode_coupling_strength: 0.0605
- abm_feedback_gamma: 0.0500
- damping: 0.1005
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 93.3991
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0067
- bootstrap_mean: 0.0065
- CI 95%: [-0.0051, 0.0191]
- weighted_value (LoE factor 0.20): 0.0013
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 177.6707
- rmse_abm_no_ode: 178.8619
- rmse_ode: 9.9827
- rmse_reduced: 85.8555
- threshold: 1.8501

### Calibración
- forcing_scale: 0.1434
- macro_coupling: 0.1451
- ode_coupling_strength: 0.1161
- abm_feedback_gamma: 0.0500
- damping: 0.0291
- ode_alpha: 0.0910
- ode_beta: 0.7528
- assimilation_strength: 0.0000
- calibration_rmse: 88.9972
- ode_rolling: None


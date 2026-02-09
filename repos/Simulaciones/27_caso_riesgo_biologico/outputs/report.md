# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-09T17:51:51.834119Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4443
- bootstrap_mean: 0.4496
- CI 95%: [0.3745, 0.5289]
- weighted_value (LoE factor 0.80): 0.3554
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9995
- external: 0.9866
- CR: 1.0131
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9454
- rmse_abm_no_ode: 1.7013
- rmse_ode: 0.7150
- rmse_reduced: 2.4982
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3542
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5317
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7419

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0769
- bootstrap_mean: -0.0771
- CI 95%: [-0.0991, -0.0653]
- weighted_value (LoE factor 0.80): -0.0615
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9978
- CR: 1.0021
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8693
- rmse_abm_no_ode: 0.8072
- rmse_ode: 1.1552
- rmse_reduced: 2.1157
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6080
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1916


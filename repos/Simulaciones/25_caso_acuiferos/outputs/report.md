# Reporte de Validación — Nivel Freático de Acuíferos

- generated_at: 2026-02-08T20:42:39.492245Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4244
- bootstrap_mean: -0.4248
- CI 95%: [-0.4373, -0.4147]
- weighted_value (LoE factor 0.20): -0.0849
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0512
- rmse_abm_no_ode: 0.7380
- rmse_ode: 3.4106
- rmse_reduced: 3.5286
- threshold: 0.9282

### Calibración
- forcing_scale: 0.7430
- macro_coupling: 0.1000
- damping: 0.7323
- ode_alpha: 0.0280
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0524

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1969
- bootstrap_mean: -0.1973
- CI 95%: [-0.2139, -0.1829]
- weighted_value (LoE factor 0.20): -0.0394
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0777
- external: 0.6621
- CR: 0.1174
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 23.1482
- rmse_abm_no_ode: 19.3404
- rmse_ode: 27.9754
- rmse_reduced: 35.7618
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5135


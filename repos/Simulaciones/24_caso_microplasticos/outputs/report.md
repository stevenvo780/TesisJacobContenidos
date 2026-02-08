# Reporte de Validación — Contaminación por Microplásticos

- generated_at: 2026-02-08T20:54:42.369692Z

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
- valor: -0.6185
- bootstrap_mean: -0.6192
- CI 95%: [-0.6398, -0.6028]
- weighted_value (LoE factor 0.20): -0.1237
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3694
- rmse_abm_no_ode: 1.4640
- rmse_ode: 2.9014
- rmse_reduced: 4.1651
- threshold: 1.2517

### Calibración
- forcing_scale: 0.4903
- macro_coupling: 0.8446
- damping: 0.4835
- ode_alpha: 0.3092
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1471


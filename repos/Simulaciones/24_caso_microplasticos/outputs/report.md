# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T01:56:40.032633Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -4.0711
- bootstrap_mean: -4.0650
- CI 95%: [-4.4834, -3.6339]
- weighted_value (LoE factor 0.80): -3.2569
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9964
- CR: 1.0036
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8558
- rmse_abm_no_ode: 0.3659
- rmse_ode: 5.1987
- rmse_reduced: 3.0108
- threshold: 0.4661

### Calibración
- forcing_scale: 0.7011
- macro_coupling: 0.4136
- damping: 0.6963
- ode_alpha: 0.0163
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0417

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3491
- bootstrap_mean: 0.3463
- CI 95%: [0.2645, 0.4061]
- weighted_value (LoE factor 0.80): 0.2792
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9884
- CR: 1.0117
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 11.7282
- rmse_abm_no_ode: 18.0173
- rmse_ode: 7.7734
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7461
- macro_coupling: 1.0000
- damping: 0.4276
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3875


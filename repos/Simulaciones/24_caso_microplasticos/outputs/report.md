# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T01:45:46.213518Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -6.6789
- bootstrap_mean: -6.6799
- CI 95%: [-6.7134, -6.6522]
- weighted_value (LoE factor 0.80): -5.3431
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8931
- CR: 1.1197
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 22.3494
- rmse_abm_no_ode: 2.9105
- rmse_ode: 33.8428
- rmse_reduced: 5.7705
- threshold: 2.0137

### Calibración
- forcing_scale: 0.2337
- macro_coupling: 0.4975
- damping: 0.2235
- ode_alpha: 0.0059
- ode_beta: 0.3455
- assimilation_strength: 0.0000
- calibration_rmse: 0.1501

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2297
- bootstrap_mean: 0.2339
- CI 95%: [0.1859, 0.3034]
- weighted_value (LoE factor 0.80): 0.1838
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9893
- CR: 1.0108
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 13.8787
- rmse_abm_no_ode: 18.0173
- rmse_ode: 10.6464
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


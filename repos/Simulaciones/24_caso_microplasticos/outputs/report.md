# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T02:06:30.992265Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1740
- bootstrap_mean: -0.1749
- CI 95%: [-0.2005, -0.1549]
- weighted_value (LoE factor 0.80): -0.1392
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9896
- CR: 1.0105
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6198
- rmse_abm_no_ode: 1.3798
- rmse_ode: 2.2194
- rmse_reduced: 1.3171
- threshold: 0.1000

### Calibración
- forcing_scale: 0.5174
- macro_coupling: 0.2414
- damping: 0.5077
- ode_alpha: 0.0010
- ode_beta: 0.8643
- assimilation_strength: 0.0000
- calibration_rmse: 0.1281

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.1205
- bootstrap_mean: -1.1260
- CI 95%: [-1.3511, -0.9517]
- weighted_value (LoE factor 0.80): -0.8964
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9851
- CR: 1.0152
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 38.2059
- rmse_abm_no_ode: 18.0173
- rmse_ode: 44.8750
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


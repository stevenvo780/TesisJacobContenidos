# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T01:58:59.629098Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.3836
- bootstrap_mean: -1.3743
- CI 95%: [-1.6280, -1.1697]
- weighted_value (LoE factor 0.80): -1.1068
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6000
- external: 0.8225
- CR: 0.7295
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 71.9315
- rmse_abm_no_ode: 30.1782
- rmse_ode: 5.1318
- rmse_reduced: 0.8996
- threshold: 0.6801

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6732
- damping: 0.7933
- ode_alpha: 0.0692
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5028

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


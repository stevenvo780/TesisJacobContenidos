# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T02:13:49.100368Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -2.7593
- bootstrap_mean: -2.7648
- CI 95%: [-2.9295, -2.6298]
- weighted_value (LoE factor 0.80): -2.2074
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9663
- CR: 1.0349
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.1871
- rmse_abm_no_ode: 1.3798
- rmse_ode: 13.3819
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
- valor: -1.2206
- bootstrap_mean: -1.2263
- CI 95%: [-1.4632, -1.0430]
- weighted_value (LoE factor 0.80): -0.9764
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9848
- CR: 1.0154
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 40.0085
- rmse_abm_no_ode: 18.0173
- rmse_ode: 47.4102
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


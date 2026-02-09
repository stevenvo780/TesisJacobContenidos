# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-09T15:14:27.800921Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0708
- bootstrap_mean: 0.0709
- CI 95%: [0.0581, 0.0821]
- weighted_value (LoE factor 0.20): 0.0142
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9243
- external: 0.9195
- CR: 1.0052
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3242
- rmse_abm_no_ode: 0.3490
- rmse_ode: 0.4691
- rmse_reduced: 0.3647
- threshold: 0.2766

### Calibración
- forcing_scale: 0.0092
- macro_coupling: 0.1316
- damping: 0.0366
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0172

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0052
- bootstrap_mean: -0.0052
- CI 95%: [-0.0062, -0.0044]
- weighted_value (LoE factor 0.20): -0.0010
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6828
- external: -0.6123
- CR: 1.1151
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6040
- rmse_abm_no_ode: 1.5958
- rmse_ode: 2.0696
- rmse_reduced: 1.5820
- threshold: 1.2251

### Calibración
- forcing_scale: 0.0078
- macro_coupling: 0.1241
- damping: 0.0312
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0292


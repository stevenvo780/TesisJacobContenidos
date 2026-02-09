# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-09T03:40:32.801146Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0451
- bootstrap_mean: 0.0452
- CI 95%: [0.0403, 0.0506]
- weighted_value (LoE factor 0.20): 0.0090
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8949
- external: 0.8744
- CR: 1.0234
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3943
- rmse_abm_no_ode: 0.4129
- rmse_ode: 0.3526
- rmse_reduced: 0.4350
- threshold: 0.2330

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0160

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0041
- bootstrap_mean: -0.0041
- CI 95%: [-0.0049, -0.0035]
- weighted_value (LoE factor 0.20): -0.0008
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4928
- external: -0.4884
- CR: 1.0090
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5972
- rmse_abm_no_ode: 1.5907
- rmse_ode: 2.0007
- rmse_reduced: 1.5767
- threshold: 1.2251

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 1.0283


# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-08T20:46:26.888717Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0188
- bootstrap_mean: -0.0188
- CI 95%: [-0.0196, -0.0182]
- weighted_value (LoE factor 0.20): -0.0038
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3722
- rmse_abm_no_ode: 1.3468
- rmse_ode: 3.8161
- rmse_reduced: 4.3404
- threshold: 1.2888

### Calibración
- forcing_scale: 0.5978
- macro_coupling: 0.2272
- damping: 0.9262
- ode_alpha: 0.1166
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1058

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0002
- bootstrap_mean: 0.0002
- CI 95%: [-0.0016, 0.0018]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.9995
- CR: 0.9999
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1760
- rmse_abm_no_ode: 1.1762
- rmse_ode: 1.4479
- rmse_reduced: 1.4484
- threshold: 1.2251

### Calibración
- forcing_scale: 0.8548
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6659


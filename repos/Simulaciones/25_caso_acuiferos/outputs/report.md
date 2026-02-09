# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T02:14:02.133384Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.9526
- bootstrap_mean: -0.9548
- CI 95%: [-1.0232, -0.8987]
- weighted_value (LoE factor 0.60): -0.5716
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9685
- CR: 1.0325
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9880
- rmse_abm_no_ode: 1.5303
- rmse_ode: 4.8407
- rmse_reduced: 1.0188
- threshold: 0.1000

### Calibración
- forcing_scale: 0.7843
- macro_coupling: 0.6272
- damping: 0.7603
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2102

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.4786
- bootstrap_mean: -1.4753
- CI 95%: [-1.8456, -1.1527]
- weighted_value (LoE factor 0.60): -0.8872
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7905
- external: 0.8286
- CR: 0.9540
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 46.4166
- rmse_abm_no_ode: 18.7266
- rmse_ode: 102.1861
- rmse_reduced: 35.7618
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5404


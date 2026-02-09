# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T01:59:10.249507Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -2.1932
- bootstrap_mean: -2.1930
- CI 95%: [-2.2758, -2.1104]
- weighted_value (LoE factor 0.60): -1.3159
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.3114
- external: 0.3828
- CR: 0.8136
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 128.9778
- rmse_abm_no_ode: 40.3918
- rmse_ode: 1.2416
- rmse_reduced: 1.0216
- threshold: 1.0214

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.9190
- damping: 0.5900
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6358

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3313
- bootstrap_mean: -0.3299
- CI 95%: [-0.3679, -0.2769]
- weighted_value (LoE factor 0.60): -0.1988
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.2068
- external: 0.5446
- CR: 0.3797
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 24.9313
- rmse_abm_no_ode: 18.7266
- rmse_ode: 31.4284
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


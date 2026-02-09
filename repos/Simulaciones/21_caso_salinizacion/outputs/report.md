# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T01:45:17.724751Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0967
- bootstrap_mean: -0.0988
- CI 95%: [-0.1524, -0.0569]
- weighted_value (LoE factor 0.60): -0.0580
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9940
- CR: 1.0058
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5729
- rmse_abm_no_ode: 1.4343
- rmse_ode: 2.3389
- rmse_reduced: 3.6068
- threshold: 1.0442

### Calibración
- forcing_scale: 0.9447
- macro_coupling: 0.2441
- damping: 0.9500
- ode_alpha: 0.3858
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4047

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.5687
- bootstrap_mean: -0.5648
- CI 95%: [-0.8957, -0.2536]
- weighted_value (LoE factor 0.60): -0.3412
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8228
- external: 0.1882
- CR: 4.3712
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.3716
- rmse_abm_no_ode: 0.8744
- rmse_ode: 0.7002
- rmse_reduced: 1.0780
- threshold: 0.1357

### Calibración
- forcing_scale: 0.9487
- macro_coupling: 0.7718
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2739


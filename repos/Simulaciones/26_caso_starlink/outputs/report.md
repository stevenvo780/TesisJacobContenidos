# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T17:52:13.761304Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0525
- bootstrap_mean: -0.0518
- CI 95%: [-0.0679, -0.0350]
- weighted_value (LoE factor 0.80): -0.0420
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9900
- CR: 1.0099
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3435
- rmse_abm_no_ode: 1.2765
- rmse_ode: 0.9059
- rmse_reduced: 0.8072
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9603
- macro_coupling: 0.4810
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2810

## Fase real
- **overall_pass**: False

### EDI
- valor: -545.7356
- bootstrap_mean: -544.7204
- CI 95%: [-615.3770, -477.9375]
- weighted_value (LoE factor 0.80): -436.5885
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9876
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0692
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.6585
- rmse_reduced: 0.0001
- threshold: 0.1000

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1071
- ode_coupling_strength: 0.0857
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0002


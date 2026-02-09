# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T02:20:57.759330Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2633
- bootstrap_mean: 0.2583
- CI 95%: [-0.0216, 0.4875]
- weighted_value (LoE factor 0.60): 0.1580
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9997
- external: 0.9991
- CR: 1.0005
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4284
- rmse_abm_no_ode: 0.5816
- rmse_ode: 0.8824
- rmse_reduced: 2.6843
- threshold: 0.7133

### Calibración
- forcing_scale: 0.9505
- macro_coupling: 0.4046
- damping: 0.9500
- ode_alpha: 0.3447
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3684

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.9775
- bootstrap_mean: -0.9931
- CI 95%: [-2.3527, -0.1354]
- weighted_value (LoE factor 0.60): -0.5865
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9099
- external: 0.1143
- CR: 7.9587
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.7290
- rmse_abm_no_ode: 0.8744
- rmse_ode: 3.0444
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

